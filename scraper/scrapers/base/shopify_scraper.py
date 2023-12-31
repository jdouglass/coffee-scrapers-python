from decimal import Decimal
from config.constants import DEFAULT_IMAGE_URL
from scrapers.base.base_scraper import BaseScraper
from config.config import USE_MOCK_DATA
import requests


class ShopifyScraper(BaseScraper):

    def extract_published_date(self, product):
        return product["published_at"]

    def extract_image_url(self, product):
        return product["images"][0]["src"] if product["images"] else DEFAULT_IMAGE_URL

    def extract_handle(self, product):
        return product["handle"]

    def extract_price(self, variant):
        return round(Decimal(variant["price"]), 2)

    def extract_title(self, product):
        return product["title"].title()

    def is_sold_out(self, variant):
        return not variant["available"]

    def extract_variant_id(self, variant):
        return variant["id"]

    def extract_size(self, variant):
        return round(variant["grams"], 2)

    def fetch_products(self):
        if USE_MOCK_DATA:
            self.products = self.load_mock_data(self.mock_data_path)
            return
        response = requests.get(self.url)
        data = response.json()
        self.products = data['products']
