''''
A URL shortener is a service to generate, retrieve and delete short URLs mapped
to original URLs (e.g.: http://goo.gl , Bitly Connections Platform | Short URLs,
 QR Codes, and More  etc.) The goal is to create a library that allows managing URL
 shortening, similar to Bitly Connections Platform | Short URLs, QR Codes, and More .
'''
from typing import List

from exceptions import UrlLimitExceeded
from strategy import AbstractStrategy

URL_PREFIX = "https://www.rev.me/"


class URLShortener:

    def __init__(self, predefined_input: List, strategy: AbstractStrategy):
        self.url_list = {}
        self.predefined_input = predefined_input
        self.strategy = strategy

    def get_url_limit(self) -> int:
        return len(self.predefined_input)

    def get_rest_defined_urls(self) -> List:
        return self.predefined_input

    def add_new_url(self, full_url: str) -> str:
        if len(self.predefined_input) == 0:
            raise UrlLimitExceeded("URL limit exceeded")

        shortened_url = self.shorten_url(full_url)
        self.url_list[shortened_url] = full_url
        return shortened_url

    def shorten_url(self, full_url: str) -> str:
        selected_input = self.strategy.pick_value(self.predefined_input)
        short_url = f"{URL_PREFIX}{selected_input}"
        return short_url

    def find_full_url(self, short_url: str) -> str:
        full_url = self.url_list.get(short_url)
        if not full_url:
            raise Exception("URL not found")
        else:
            return full_url


if __name__ == "__main__":
    pass
