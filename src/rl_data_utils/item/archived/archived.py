from typing import Union, Final

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.bool_attribute import BoolAttribute


class ArchivedInfo(AttributeInfo):
    attribute_name: Final[str] = 'archived'
    order: Final[int] = 12


class Archived(BoolAttribute, ArchivedInfo):
    default_value: Final[bool] = False


InitializeArchived = Union[Archived, bool, None]
