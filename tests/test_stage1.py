import unittest
import pytest

from main import URLShortener, URL_PREFIX, UrlLimitExceeded
from strategy import SequentialStrategy


class Stage1Tests(unittest.TestCase):

    STAGE1_URL_TO_TEST = "https://www.revolut.com/rewards-personalised-cashback-and-discounts/"

    def test_url_shortening(self):
        predefined_urls = ["aaaaa"]
        strategy = SequentialStrategy()
        url_shortener = URLShortener(predefined_urls, strategy)
        short_url = url_shortener.add_new_url(self.STAGE1_URL_TO_TEST)
        self.assertEqual(short_url, f"{URL_PREFIX}aaaaa")

    def test_find_long_url_by_short_url(self):
        predefined_urls = ["aaaaa"]
        strategy = SequentialStrategy()
        url_shortener = URLShortener(predefined_urls, strategy)
        short_url = url_shortener.add_new_url(self.STAGE1_URL_TO_TEST)

        long_url = url_shortener.find_full_url(short_url)
        self.assertEqual(long_url, self.STAGE1_URL_TO_TEST)

    def test_url_limit(self):
        predefined_urls = ["aaaaa"]
        strategy = SequentialStrategy()
        url_shortener = URLShortener(predefined_urls, strategy)
        url_limit = url_shortener.get_url_limit()
        for _ in range(url_limit):
            # should not throw an exception
            url_shortener.add_new_url(self.STAGE1_URL_TO_TEST)
        with pytest.raises(UrlLimitExceeded):
            url_shortener.add_new_url(self.STAGE1_URL_TO_TEST)

    def test_sequential_strategy(self):
        predefined_urls = ["aaaaa", "bbbbb", "ccccc"]
        strategy = SequentialStrategy()
        url_shortener = URLShortener(predefined_urls, strategy)
        short_url = url_shortener.add_new_url(self.STAGE1_URL_TO_TEST)
        self.assertEqual(short_url, f"{URL_PREFIX}aaaaa")
        short_url = url_shortener.add_new_url(self.STAGE1_URL_TO_TEST)
        self.assertEqual(short_url, f"{URL_PREFIX}bbbbb")
        short_url = url_shortener.add_new_url(self.STAGE1_URL_TO_TEST)
        self.assertEqual(short_url, f"{URL_PREFIX}ccccc")
        with pytest.raises(UrlLimitExceeded):
            short_url = url_shortener.add_new_url(self.STAGE1_URL_TO_TEST)


if __name__ == '__main__':
    unittest.main()
