from __future__ import annotations

from typing import Union, List, Tuple

from rl_data_utils.item.attribute.attribute import Name, Slot, Rarity, Color, Platform, Certified, Serie
from rl_data_utils.item.attribute_data.attribute_data import Slots, Rarities, Colors, Platforms, Certificates, Series
from rl_data_utils.item.item.identity_item import IdentityItem, HasName
from rl_data_utils.rocket_league.utils import initialize


class DataIdentityItem(HasName):
    def __init__(
            self,
            name: Union[Name, str],
            slots: Union[Slots, List[Slot], List[str]],
            rarities: Union[Rarities, List[Rarity], List[str]]
    ):
        HasName.__init__(self, name)
        self.slots = slots
        self.rarities = rarities

    @property
    def slots(self) -> Slots:
        return self._slots

    @slots.setter
    def slots(self, slots: Union[Slots, List[Slot], List[Union[Tuple[int, int], str]]]):
        self._slots = initialize(Slots, list, slots)
        
    @property
    def rarities(self) -> Rarities:
        return self._rarities

    @rarities.setter
    def rarities(self, rarities: Union[Rarities, List[Rarity], List[Union[Tuple[int, int], str]]]):
        self._rarities = initialize(Rarities, list, rarities)

    def match(self, identity_item: IdentityItem):
        self.slots.match(identity_item.slot)
        self.rarities.match(identity_item.rarity)


class DataItem(IdentityItem):
    def __init__(
            self,
            name: Name,
            slot: Slot,
            rarity: Rarity,
            colors: Union[Colors, List[Color], List[Union[Tuple[int, int], str]], None],
            certificates: Union[Certificates, List[Certified], List[Union[Tuple[int, int], str]], None],
            platforms: Union[Platforms, List[Platform], List[Union[Tuple[int, int], str]], None],
            series: Union[Series, List[Serie], List[Union[Tuple[int, int], str]], None]
    ):
        self.series = series
        self.certificates = certificates
        self.platforms = platforms
        self.colors = colors
        super().__init__(name, slot, rarity)
    
    @property
    def series(self) -> Series:
        return self._series

    @series.setter
    def series(self, series: Union[Series, List[Serie], List[Union[Tuple[int, int], str]]]):
        self._series = initialize(Series, list, series)
        
    @property
    def certificates(self) -> certificates:
        return self._certificates

    @certificates.setter
    def certificates(self, certificates: Union[Certificates, List[Certified], List[Union[Tuple[int, int], str]]]):
        self._certificates = initialize(Certificates, list, certificates)

    @property
    def platforms(self) -> Platforms:
        return self._platforms

    @platforms.setter
    def platforms(self, platforms: Union[Platforms, List[Platform], List[Union[Tuple[int, int], str]]]):
        self._platforms = initialize(Platforms, list, platforms)
    
    @property
    def colors(self) -> Colors:
        return self._colors

    @colors.setter
    def colors(self, colors: Union[Colors, List[Color], List[Union[Tuple[int, int], str]]]):
        self._colors = initialize(Color, list, colors)

    def match(self, item: Item):
        self.colors.match(item.color)
        self.platforms.match(item.platform)
        self.series.match(item.serie)
        self.certificates.match(item.certified)

    # def to_item(self, serie=None, platform=None, color=None, rarity=None):
    #     """
    #     Transform the self DataItem into a new Item
    #     :param serie: An optional serie
    #     :param platform: An optional platform
    #     :param color: An optional color
    #     :param rarity: An optional rarity
    #     :return: A new Item based at itself and the attributes arguments
    #     """
    #     to_update = {a.identifier: each for each in (serie, platform, color, rarity) if each}
    #     kwargs = self.get_attributes_dict()
    #     kwargs.update(to_update)
    #     return Item(**kwargs)
