# Elder Companion Chatbot

## Overview
This project is a Streamlit-based chatbot named "暖心伙伴" (Warm Companion), designed to provide emotional support and companionship for the elderly. It leverages LangChain and OpenAI models to generate warm, empathetic responses.

## Features
- **Emotional Support**: Engages in daily conversations to alleviate loneliness.
- **Memory Retrieval**: Uses Chroma vector store to recall past interactions.
- **User-Friendly Interface**: Simple and intuitive chat interface built with Streamlit.

## Configuration
- **ZhipuAI**: Configured for embeddings and model interactions.
- **OpenAI**: Used for generating responses with customizable temperature.
- **Persistent Storage**: Stores chat history in a local vector database (`./memory`).

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Update `config.py` with your API keys and model details.
3. Run the application:
   ```bash
   streamlit run main.py
   ```

## Usage
- Start the app and interact with the chatbot in the browser.
- The bot will remember past conversations to provide context-aware responses.

## License
MIT License (see `LICENSE` file for details).

## Thought
Man is the drifting boat and home is the warm shore.

人是漂泊的船，家是温暖的岸。
