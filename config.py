class Config:
    ZHIPUAI_API_KEY: str = "your zhipuai api key"
    ZHIPUAI_MODEL: str = "your zhipuai model"

    OPENAI_API_BASE: str = "your openai api base"
    OPENAI_API_KEY: str = "your openai api key"
    OPENAI_MODEL_NAME: str = "your openai model"
    TEMPERATURE: float = 0.8

    TOP_K: int = 3

    PERSISTENT_PATH: str = "./memory"
