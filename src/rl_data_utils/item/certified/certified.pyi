from __future__ import annotations

from typing import Literal, ClassVar

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.certified.constants import NONE
from rl_data_utils.rocket_league.rocket_league import Defaultable

CertifiedPatternKey = Literal["Aviator", "Acrobat", "Goalkeeper", "Guardian", "Juggler", "None", "Paragon", "Playmaker",
                              "Scorer", "Show-off", "Sniper", "Striker", "Sweeper", "Tactician", "Turtle", "Victor"]


class CertifiedInfo(AttributeInfo): ...


class Certified(RegexBasedItemAttribute, CertifiedInfo, Defaultable):
    default_args: ClassVar = [NONE], dict()


class Certificates(RegexBasedListAttribute[Certified], CertifiedInfo): ...
