class Config:
    ollama_embedding_model: str = "embeddinggemma:latest"
    ollama_embedding_url: str = "http://127.0.0.1:11434"

    model_name: str = "your model name"
    base_url: str = "your base url"
    api_key: str = "your api key"

    temperature: float = 0.8

    top_k: int = 3

    persistent_path: str = "./memory"
