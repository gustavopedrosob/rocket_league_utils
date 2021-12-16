from typing import Union, Final

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.bool_attribute import BoolAttribute, SetBoolAttribute


class ArchivedInfo(AttributeInfo):
    attribute_name: Final[str] = 'archived'
    order: Final[int] = 12


class Archived(BoolAttribute, ArchivedInfo):
    default_value: Final[bool] = False


InitializeArchived = Union[Archived, bool, None]


class HasArchived(ArchivedInfo):
    def __init__(self, archived: InitializeArchived = None):
        self.archived: Archived = archived

    def get_archived(self) -> Archived:
        return self._archived

    def set_archived(self, value: SetBoolAttribute):
        self._archived = Archived.initialize(value)

    archived = property(get_archived, set_archived)
