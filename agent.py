from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph

from config import Config
from prompt import SYSTEM_PROMPT
from state import AgentState


class Agent:
    def __init__(self):
        self.embedding_function = ZhipuAIEmbeddings(
            model=Config.ZHIPUAI_MODEL,
            api_key=Config.ZHIPUAI_API_KEY
        )

        self.vector_store = Chroma(
            embedding_function=self.embedding_function,
            persist_directory=Config.PERSISTENT_PATH
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", SYSTEM_PROMPT),
                ("human", "{input}"),
            ]
        )

        self.model = prompt | ChatOpenAI(
            model_name=Config.OPENAI_MODEL_NAME,
            openai_api_key=Config.OPENAI_API_KEY,
            openai_api_base=Config.OPENAI_API_BASE,
            temperature=Config.TEMPERATURE
        )

        def retrieve_memory(state: AgentState):
            original_input = state.get("original_input", "")

            docs = self.vector_store.similarity_search(original_input, k=Config.TOP_K)

            memory = [doc.page_content.strip() for doc in docs]

            memory_str = "\n".join(memory)

            final_input = f"""
                用户的问题是：
                {original_input}
                
                历史对话记录是：
                {memory_str}
                
                你可以参考历史对话记录来回答用户的问题。如果你认为历史对话记录与问题不相关，则忽略历史对话记录，基于自己的知识来回答问题。
            """

            print("final_input:", final_input, end="\n\n")

            return {
                "messages": [HumanMessage(content=final_input)]
            }

        def call_model(state: AgentState):
            messages = state["messages"]

            input_content = messages[-1].content

            response = self.model.invoke({"input": input_content})

            return {"messages": [response]}

        def save_memory(state: AgentState):
            original_input = state.get("original_input", "")

            messages = state["messages"]
            response = messages[-1].content

            chat_history = f"""
                ```
                之前的问题：
                {original_input}
                
                之前的回答：
                {response}
                ```
            """

            self.vector_store.add_texts(texts=[chat_history])

            return state

        workflow = StateGraph(AgentState)

        workflow.add_node("retrieve_memory", retrieve_memory)
        workflow.add_node("call_model", call_model)
        workflow.add_node("save_memory", save_memory)

        workflow.set_entry_point("retrieve_memory")
        workflow.add_edge("retrieve_memory", "call_model")
        workflow.add_edge("call_model", "save_memory")
        workflow.set_finish_point("save_memory")

        self.app = workflow.compile()

    def invoke(self, query: str):
        try:
            result = self.app.invoke({
                "original_input": query,
                "messages": []
            })
            if result["messages"] and len(result["messages"]) > 0:
                return result["messages"][-1].content
            else:
                return "小助手繁忙中，请稍后重试..."
        except Exception as e:
            return str(e)
