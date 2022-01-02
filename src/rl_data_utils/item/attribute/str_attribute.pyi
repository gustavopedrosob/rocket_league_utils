from __future__ import annotations

from typing import List, ClassVar

from rl_data_utils.item.attribute.static_attribute import StaticItemAttribute


class StrItemAttribute(StaticItemAttribute):
    possible_values: ClassVar[List[str]]
