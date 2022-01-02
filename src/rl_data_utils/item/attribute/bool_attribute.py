from __future__ import annotations

from rl_data_utils.item.attribute.static_attribute import StaticItemAttribute


class BoolItemAttribute(StaticItemAttribute):
    possible_values = True, False
