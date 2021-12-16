from typing import Union, Iterable, Dict, List

from rl_data_utils.exceptions import RlAttributeError
from rl_data_utils.item.archived.archived import Archived
from rl_data_utils.item.blueprint.blueprint import Blueprint
from rl_data_utils.item.certified.certified import Certified
from rl_data_utils.item.color.color import Color, Colors
from rl_data_utils.item.crafting_cost.crafting_cost import CraftingCost
from rl_data_utils.item.item.constants import FULL, AttributeName
from rl_data_utils.item.name.name import Name
from rl_data_utils.item.paintable.paintable import Paintable
from rl_data_utils.item.platform.platform import Platform, Platforms
from rl_data_utils.item.price.price import Price
from rl_data_utils.item.quantity.quantity import Quantity
from rl_data_utils.item.rarity.rarity import Rarity, Rarities
from rl_data_utils.item.serie.serie import Serie, Series
from rl_data_utils.item.slot.slot import Slot
from rl_data_utils.item.tradable.tradable import Tradable

IndentifierAttribute = Union[Name, Rarity, Slot, Blueprint, Platform]

AnyAttribute = Union[Archived, Name, Slot, Color, Rarity, Certified, Quantity, Blueprint, Paintable, Platform, Price,
                     Serie, Tradable, CraftingCost]

AnyDataAttribute = Union[Colors, Rarities, Platforms, Series]

AnyAllAttribute = Union[AnyAttribute, AnyDataAttribute]

AttributeCollection = List[AnyAllAttribute]


class HasAttribute:
    def validate(self):
        """
        Validates all attributes
        :raise AttributeNotExists: If any RegexBasedAttribute attribute is invalid
        """
        for attr in self.get_attrs():
            attr.validate()

    def is_valid(self) -> bool:
        """
        Says if it's valid
        :return: If it's valid
        """
        try:
            self.validate()
        except RlAttributeError:
            return False
        else:
            return True

    def is_undefined(self) -> bool:
        """
        Says if all attributes are undefined
        :return: If all attributes are undefined
        """
        return all(attr.is_undefined() for attr in self.get_attrs())

    def get_attrs(self,
                  attrs: List[AttributeName] = FULL,
                  ignore_undefined: bool = False) -> Iterable[AnyAttribute]:
        """
        Gets all attributes
        :param ignore_undefined: If True it doesn't give you undefined attributes
        :param attrs: Attributes that you want to get
        :raise AttributeError: If attrs doesn't exist in instance
        :return: All attributes
        """
        for key in attrs:
            attr = self.get_attr(key)
            if ignore_undefined and attr.is_undefined():
                continue
            yield attr

    def get_attr(self, key: AttributeName) -> AnyAttribute:
        """
        Gets an Attribute by his key
        :param key: An attribute name
        :return: An attribute depends on key
        """
        return getattr(self, key)

    def get_attr_dict(self,
                      attrs: List[AttributeName] = FULL,
                      ignore_undefined: bool = False) -> Dict[str, AnyAttribute]:
        """
        Get all attributes with their respective names
        :param ignore_undefined: If True it doesn't give you undefined attributes
        :param attrs: Attributes that you want to get
        :raise AttributeError: If attrs doesn't exist in instance
        :return: A dict of attributes
        """
        return {attr.attribute_name: attr for attr in self.get_attrs(attrs, ignore_undefined)}

    def get_sorted_attrs(self,
                         attrs: List[AttributeName] = FULL,
                         ignore_undefined: bool = False,
                         reverse: bool = False) -> List[AnyAttribute]:
        """
        Get sorted attributes
        :param attrs: Attributes that you want to get
        :param ignore_undefined: If True it doesn't give you undefined attributes
        :param reverse: Reverses the dictionary
        :return: An sorted list of attributes
        """
        list_ = list(self.get_attrs(attrs, ignore_undefined))
        list_.sort(key=lambda attr: attr.order, reverse=reverse)
        return list_
