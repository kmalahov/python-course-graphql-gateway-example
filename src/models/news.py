from datetime import datetime

from pydantic import BaseModel, Field


class NewsModel(BaseModel):
    """
    Модель для описания новостей.
    """

    author: str = Field(title="Автор")
    source: str = Field(title="Источник")
    title: str = Field(title="Заголовок")
    description: str = Field(title="Описание")
    url: str = Field(title="Ссылка")
    url_to_image: str = Field(title="Ссылка на изображение")
    published_at: datetime = Field(title="Дата публикации")
    content: str = Field(title="Содержание")
