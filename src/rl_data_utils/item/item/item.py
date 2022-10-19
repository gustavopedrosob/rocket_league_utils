from __future__ import annotations

from typing import Union

from rl_data_utils.item.attribute.attribute import Archived, Name, Slot, Color, Rarity, Certified, \
    Quantity, Blueprint, Platform, Price, Serie, Tradable, Favorite, CreditsQuantity
from rl_data_utils.item.attribute.constants import NON_CRATE, PREMIUM, CREDITS
from rl_data_utils.item.attribute_data.attribute_data import CraftingCost
from rl_data_utils.item.item.constants import NAME, SLOT, RARITY, QUANTITY, BLUEPRINT, SERIE, TRADABLE, FAVORITE, \
    ARCHIVED, COLOR, CERTIFIED
from rl_data_utils.item.item.identity_item import IdentityItem, HasName, HasSlot
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject
from rl_data_utils.rocket_league.utils import initialize


class RepresentsItem(RocketLeagueObject, HasName, HasSlot):
    def __init__(
            self,
            name: Union[Name, str],
            slot: Union[Slot, str, tuple],
            blueprint: Union[Blueprint, bool],
            color: Union[Color, str, tuple, None] = None
    ) -> None:
        HasName.__init__(self, name)
        HasSlot.__init__(self, slot)
        self.blueprint = blueprint
        self.color = color

    @property
    def blueprint(self) -> Blueprint:
        return self._blueprint

    @blueprint.setter
    def blueprint(self, blueprint: Union[Blueprint, bool]):
        self._blueprint = initialize(Blueprint, bool, blueprint)

    @property
    def color(self) -> Color:
        return self._color

    @color.setter
    def color(self, color: Union[Color, str, tuple, None]):
        self._color = initialize(Color, (str, tuple), color)

    def compare_representation(self, other) -> bool:
        return self.blueprint.compare(other.blueprint) and self.name.compare(other.name) and \
               self.slot.compare(other.slot) and self.color.compare(other.color)


class Item(IdentityItem, RepresentsItem):
    def __init__(
            self,
            name: Union[Name, str],
            slot: Union[Slot, str, tuple],
            rarity: Union[Rarity, str, tuple],
            quantity: Union[Quantity, int],
            blueprint: Union[Blueprint, bool],
            serie: Union[Serie, str, tuple],
            tradable: Union[Tradable, bool],
            favorite: Union[Favorite, bool, None] = None,
            archived: Union[Archived, bool, None] = None,
            color: Union[Color, str, tuple, None] = None,
            certified: Union[Certified, str, tuple, None] = None
    ) -> None:
        self.archived = archived
        self.certified = certified
        self.quantity = quantity
        self.serie = serie
        self.tradable = tradable
        self.favorite = favorite
        IdentityItem.__init__(self, name, rarity, slot)
        RepresentsItem.__init__(self, name, slot, blueprint, color)

    @property
    def archived(self) -> Archived:
        return self._archived

    @archived.setter
    def archived(self, archived: Union[Archived, bool, None]):
        self._archived = initialize(Archived, bool, archived)

    @property
    def certified(self) -> Certified:
        return self._certified

    @certified.setter
    def certified(self, certified: Union[Certified, str, tuple, None]):
        self._certified = initialize(Certified, (str, tuple), certified)

    @property
    def quantity(self) -> Quantity:
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: Union[Quantity, int]):
        self._quantity = initialize(Quantity, int, quantity)

    def is_non_crate(self):
        return self.serie.is_exactly(NON_CRATE)


class ItemWithPrice(Item):
    def __init__(
            self,
            name: Union[Name, str],
            slot: Union[Slot, str, tuple],
            rarity: Union[Rarity, str, tuple],
            quantity: Union[Quantity, int],
            blueprint: Union[Blueprint, bool],
            platform: Union[Platform, str, tuple],
            price: Union[Price, tuple],
            serie: Union[Serie, str, tuple],
            tradable: Union[Tradable, bool],
            crafting_cost: Union[CraftingCost, int],
            favorite: Union[Favorite, bool, None] = None,
            archived: Union[Archived, bool, None] = None,
            color: Union[Color, str, tuple, None] = None,
            certified: Union[Certified, str, tuple, None] = None
    ) -> None:
        self.platform = platform
        self.price = price
        self.crafting_cost = crafting_cost
        super().__init__(name, slot, rarity, quantity, blueprint, serie, tradable, favorite, archived, color, certified)

    @property
    def platform(self) -> Platform:
        return self._platform

    @platform.setter
    def platform(self, platform: Union[Platform, str, tuple]):
        self._platform = initialize(Platform, (str, tuple), platform)


class Credits:
    name = CREDITS
    slot = PREMIUM

    def __init__(self, quantity: Union[CreditsQuantity, int]):
        self.quantity = quantity

    @property
    def quantity(self) -> CreditsQuantity:
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: Union[CreditsQuantity, int]):
        self._quantity = initialize(CreditsQuantity, int, quantity)
