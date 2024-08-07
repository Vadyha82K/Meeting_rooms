from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = """
    Простое и прозрачное приложение, которое позволяет
    сотрудникам резервировать переговорные комнаты
    """
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()