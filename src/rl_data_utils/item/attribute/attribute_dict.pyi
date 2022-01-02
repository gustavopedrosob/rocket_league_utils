from __future__ import annotations

from typing import Any, TypeVar, Generic, List, Tuple

from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute

K = TypeVar('K', bound=RegexBasedItemAttribute)
V = TypeVar('V', bound=Any)


class AttributeDict(Generic[K, V]):
    def __init__(self, dictionary: List[Tuple[K, V]]):
        self.dictionary = dictionary

    def __getitem__(self, item: K) -> V: ...

    def __setitem__(self, key: K, value: V) -> None: ...
