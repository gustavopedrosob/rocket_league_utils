from typing import Union, Final

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.bool_attribute import BoolAttribute


class BlueprintInfo(AttributeInfo):
    attribute_name: Final[str] = 'blueprint'
    order: Final[int] = 11


class Blueprint(BoolAttribute, BlueprintInfo):
    default_value = False


InitializeBlueprint = Union[Blueprint, bool, None]
