from __future__ import annotations

from abc import ABCMeta

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.rocket_league.rocket_league import Comparable, Randomizable, RocketLeagueObject


class ItemAttribute(RocketLeagueObject, Comparable, Randomizable, AttributeInfo, metaclass=ABCMeta):
    pass
