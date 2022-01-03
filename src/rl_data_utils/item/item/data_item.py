from __future__ import annotations

from rl_data_utils.item.attribute_data.attribute_data import AttributesCollectionManagement
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.item.represents_item import RepresentsItem


class DataItem(RepresentsItem, AttributesCollectionManagement):
    def __init__(self,
                 archived=None,
                 name=None,
                 slot=None,
                 color=None,
                 rarity=None,
                 certified=None,
                 quantity=None,
                 blueprint=None,
                 paintable=None,
                 platform=None,
                 price=None,
                 serie=None,
                 tradable=None,
                 crafting_cost=None,
                 favorite=None):
        self.archived = archived
        self.blueprint = blueprint
        self.certified = certified
        self.color = color
        self.name = name
        self.paintable = paintable
        self.platform = platform
        self.price = price
        self.quantity = quantity
        self.rarity = rarity
        self.serie = serie
        self.slot = slot
        self.tradable = tradable
        self.crafting_cost = crafting_cost
        self.favorite = favorite

    def to_item(self, serie=None, platform=None, color=None, rarity=None):
        """
        Transform the self DataItem into a new Item
        :param serie: An optional serie
        :param platform: An optional platform
        :param color: An optional color
        :param rarity: An optional rarity
        :return: A new Item based at itself and the attributes arguments
        """
        to_update = {a.identifier: a for a in (serie, platform, color, rarity) if a}
        kwargs = self.get_attributes_dict()
        kwargs.update(to_update)
        return Item(**kwargs)
