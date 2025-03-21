from abc import abstractmethod, ABC
from typing import List

from exceptions import UrlLimitExceeded


class AbstractStrategy(ABC):

    @abstractmethod
    def pick_value(self, values_list: List[str]) -> str:
        pass


class SequentialStrategy(AbstractStrategy):

    def __init__(self):
        self.index = 0

    def pick_value(self, values_list: List[str]) -> str:
        if self.index >= len(values_list):
            raise UrlLimitExceeded("URL limit exceeded")
        picked_value = values_list[self.index]
        self.index += 1
        return picked_value
