from typing import TypeVar, Generic, Type

from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.rocket_league.rocket_league import RegexBased

A = TypeVar('A', bound=RegexBasedItemAttribute)


class AttributeString(Generic[A], RegexBased):
    def __init__(self, attribute_string: Type[A], string: str):
        self.attribute_string = attribute_string
        self.string = string

    def get(self) -> A: ...

    def get_exactly(self, pattern_key: str) -> A: ...
