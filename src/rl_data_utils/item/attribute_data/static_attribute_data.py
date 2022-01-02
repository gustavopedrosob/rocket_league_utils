from __future__ import annotations

from rl_data_utils.item.attribute.static_attribute import StaticItemAttribute
from rl_data_utils.item.attribute_data.attribute_data import AttributesData, AttributesManagement


class StaticAttributeData(AttributesManagement[StaticItemAttribute], AttributesData):
    pass
