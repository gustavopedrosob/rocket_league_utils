from __future__ import annotations

from typing import ClassVar

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.bool_attribute import BoolItemAttribute
from rl_data_utils.item.item.constants import ARCHIVED
from rl_data_utils.rocket_league.rocket_league import Defaultable


class ArchivedInfo(AttributeInfo):
    identifier = ARCHIVED
    order = 12


class Archived(BoolItemAttribute, ArchivedInfo, Defaultable):
    default_args: ClassVar = [False], dict()
