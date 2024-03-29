from datetime import datetime

import pytest

from dataloaders import NewsLoader
from models.news import NewsModel


class TestNewsLoader:
    @pytest.fixture
    def loader(self):
        return NewsLoader()

    def test_load_one_news(self, loader):
        news: list[NewsModel] = loader.load("RU").get()

        assert len(news) == 1
        news_item = news[0]
        assert news_item.author == "https://www.rt.com/about-us"
        assert news_item.source == "RT"
        assert news_item.title == "Russia's Space Agency Announces New Mars Mission"
        assert (
            news_item.description
            == "Roscosmos reveals plans for a groundbreaking mission to Mars, aimed at exploring the planet's surface and atmosphere."
        )
        assert (
            news_item.url == "https://www.rt.com/science/space-agency-new-mars-mission"
        )

    def test_load_many_news(self, loader):
        news: list[list[NewsModel]] = loader.load_many(["RU", "IE", "RS"]).get()
        assert len(news) == 3
