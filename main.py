import streamlit as st

from agent import Agent

# 页面配置
st.set_page_config(
    page_title="暖心伙伴",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)


@st.cache_resource(ttl=3600)
def get_agent() -> Agent:
    return Agent()


def main():
    st.subheader("✨暖心伙伴")
    st.caption("时时刻刻陪伴您的小伙伴 ～")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    else:
        for message in st.session_state['chat_history']:
            if message["role"] == 'user':
                with st.chat_message('user', avatar="👤"):
                    st.success(message["content"])
            else:
                with st.chat_message('ai', avatar="✨"):
                    st.info(message["content"])

    # 聊天输入区域
    if user_query := st.chat_input("💭 快来和我聊天吧..."):
        # 显示用户消息
        with st.chat_message('user', avatar="👤"):
            st.success(user_query)

        st.session_state['chat_history'].append(
            {"role": "user", "content": user_query}
        )

        # 显示加载状态
        with st.spinner("小伙伴思考中..."):
            agent = get_agent()
            response = agent.invoke(user_query)
        print(response)

        # 显示AI回复
        with st.chat_message('ai', avatar="✨"):
            st.info(response)

        st.session_state['chat_history'].append(
            {"role": "ai", "content": response}
        )


if __name__ == "__main__":
    main()
