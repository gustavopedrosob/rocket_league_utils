from __future__ import annotations

from functools import lru_cache

from typing import Optional, TypeVar

from rl_data_utils.item.attribute.str_attribute import StrItemAttribute
from rl_data_utils.rocket_league.rocket_league import RegexBased, Validable


RBIAT = TypeVar('RBIAT', bound=RegexBasedItemAttribute)
PK = TypeVar('PK', bound=str)


class RegexBasedItemAttribute(StrItemAttribute, RegexBased, Validable):
    def __init__(self, value: str):
        self.int_cache: Optional[int] = None
        self.value = value

    @classmethod
    @lru_cache(maxsize=None)
    def _is_exactly(cls, pattern_key: str, attribute: str) -> bool: ...

    @classmethod
    @lru_cache(maxsize=None)
    def _gen_int_cache(cls, attribute: str) -> Optional[int]: ...

    def compare(self: RBIAT, attribute: RBIAT) -> bool: ...

    def get_respective(self: RBIAT) -> RBIAT: ...

    def is_exactly(self, pattern_key: str) -> bool: ...

    def is_valid(self) -> bool: ...

    def update_int_cache(self) -> None: ...

    def validate(self) -> None: ...
