from typing import Union

from rl_data_utils.item.attribute.attribute import Name, Rarity, Slot
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject
from rl_data_utils.rocket_league.utils import initialize


class HasName:
    def __init__(self, name: Union[Name, str]):
        self.name = name

    @property
    def name(self) -> Name:
        return self._name

    @name.setter
    def name(self, name):
        self._name = initialize(Name, str, name)


class HasSlot:
    def __init__(self, slot: Union[Slot, str]):
        self.slot = slot

    @property
    def slot(self) -> Slot:
        return self._slot

    @slot.setter
    def slot(self, slot):
        self._slot = initialize(Slot, (str, tuple), slot)


class IdentityItem(RocketLeagueObject, HasName, HasSlot):
    def __init__(
            self,
            name: Union[Name, str],
            rarity: Union[Rarity, str],
            slot: Union[Slot, str]
    ):
        self.rarity = rarity
        HasSlot.__init__(self, slot)
        HasName.__init__(self, name)

    @property
    def rarity(self) -> Rarity:
        return self._rarity

    @rarity.setter
    def rarity(self, rarity):
        self._rarity = initialize(Rarity, (tuple, str), rarity)

    def compare_identity(self, other) -> bool:
        return self.name.compare(other.name) and self.rarity.compare(other.rarity) and self.slot.compare(other.slot)
