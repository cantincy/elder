# Elder Companion Chatbot

## Overview
This project is a Streamlit-based chatbot named "暖心伙伴" (Warm Companion), designed to provide emotional support and companionship for the elderly. It leverages LangChain, LangGraph, and advanced AI models to generate warm, empathetic responses with persistent memory capabilities.

## Features
- **Emotional Support**: Engages in daily conversations to alleviate loneliness with warm, empathetic responses
- **Memory Retrieval**: Uses Chroma vector store with Ollama embeddings to recall past interactions
- **LangGraph Workflow**: Implements a sophisticated three-step workflow (retrieve → generate → save)
- **User-Friendly Interface**: Simple and intuitive chat interface built with Streamlit
- **Context-Aware Responses**: Combines historical context with current queries for personalized interactions

## Architecture

### Tech Stack
- **Streamlit**: Web UI framework for the chat interface
- **LangChain**: Core LLM framework for model interactions
- **LangGraph**: Workflow orchestration for agent state management
- **Chroma**: Vector database for persistent memory storage
- **Ollama**: Local embedding model (embeddinggemma:latest)
- **OpenAI API**: Primary language model (GLM-4-9B via SiliconFlow)

### Workflow
The agent follows a three-step LangGraph workflow:

1. **Retrieve Memory**: Searches the vector database for relevant historical conversations using semantic similarity
2. **Call Model**: Generates responses using the LLM with system prompt and retrieved context
3. **Save Memory**: Stores the current conversation into the vector database for future reference

### File Structure
```
elder/
├── main.py          # Streamlit application entry point
├── agent.py         # Core Agent class with LangGraph workflow
├── config.py        # Configuration settings
├── state.py         # Agent state definitions
├── prompt.py        # System prompt for elderly care
├── requirements.txt # Python dependencies
└── memory/          # Chroma vector database storage (auto-created)
```

## Configuration

### Model Settings
- **Embedding Model**: Ollama `embeddinggemma:latest` (local)
- **Language Model**: THUDM/GLM-4-9B-0414 (via SiliconFlow API)
- **Temperature**: 0.8 (balanced creativity)
- **Top-K Retrieval**: 3 most relevant memories

### Storage
- **Vector Database**: Chroma with persistent storage at `./memory`
- **Session State**: In-memory chat history for current session

## Setup

### Prerequisites
- Python 3.8+
- Ollama running locally with `embeddinggemma:latest` model
- Valid SiliconFlow API key

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start Ollama service (if not running):
```bash
ollama serve
```

3. Pull the embedding model:
```bash
ollama pull embeddinggemma:latest
```

4. Update `config.py` with your API configuration:
```python
api_key: str = "your-siliconflow-api-key"
base_url: str = "https://api.siliconflow.cn/v1"
```

5. Run the application:
```bash
streamlit run main.py
```

## Usage

### Starting the Application
Launch the app using Streamlit:
```bash
streamlit run main.py
```

The application will open in your browser at `http://localhost:8501`

### Interacting with the Chatbot
- Type your message in the chat input box
- The AI will respond with warm, empathetic messages
- All conversations are automatically saved to memory
- Historical context is retrieved to provide personalized responses

### Features for Elderly Users
- Simple, intuitive interface with large text
- Warm, conversational tone with emotional support
- Memory of past conversations for continuity
- Health reminders (non-medical)
- Positive reinforcement and encouragement

## System Prompt Design

The system prompt is carefully designed for elderly care:
- **Role**: Warm companion like family or old friend
- **Language**: Simple, clear, avoiding technical terms
- **Tone**: Patient, sincere, empathetic, and respectful
- **Style**: Natural, warm, with gentle particles (呀, 呢, 哦)
- **Guidelines**: No medical advice, positive atmosphere, user-focused

## License
MIT License (see `LICENSE` file for details).

## Thought
Man is the drifting boat and home is the warm shore.

人是漂泊的船，家是温暖的岸。
