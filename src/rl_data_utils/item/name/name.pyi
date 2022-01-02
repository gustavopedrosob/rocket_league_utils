from __future__ import annotations

from functools import lru_cache
from typing import Optional, Tuple

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.str_attribute import StrItemAttribute
from rl_data_utils.item.item.constants import NAME
from rl_data_utils.item.name.constants import NAMES


class NameInfo(AttributeInfo):
    identifier = NAME
    order = 7


class Name(StrItemAttribute, NameInfo):
    possible_values = NAMES

    @staticmethod
    @lru_cache
    def _compare_two_string(string_1: str, string_2: str) -> bool: ...

    def compare(self, name: Name) -> bool: ...

    def get_car_name_and_decal_name(self) -> Optional[Tuple[str, str]]: ...

    def get_kind(self) -> Optional[str]: ...