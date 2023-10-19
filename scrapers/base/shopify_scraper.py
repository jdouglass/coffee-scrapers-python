from decimal import Decimal
from config.constants import DEFAULT_IMAGE_URL
from scrapers.base.base_scraper import BaseScraper


class ShopifyScraper(BaseScraper):

    def extract_published_date(self, product):
        return product["published_at"]

    def extract_image_url(self, product):
        return product["images"][0]["src"] if product["images"] else DEFAULT_IMAGE_URL

    def extract_handle(self, product):
        return product["handle"]

    def extract_price(self, product):
        return Decimal(product["variants"][0]["price"])

    def extract_title(self, product):
        return product["title"].title()

    def is_sold_out(self, product):
        return not product["variants"][0]["available"]
