from rl_data_utils.color.abc_base_color import ABCBaseColor
from rl_data_utils.type.abc_base_type import ABCBaseType
from rl_data_utils.rarity.abc_base_rarity import ABCBaseRarity
from rl_data_utils.certified.abc_base_certified import ABCBaseCertified
from rl_data_utils.quantity.abc_base_quantity import ABCBaseQuantity
from rl_data_utils.name.abc_base_name import ABCBaseName
from rl_data_utils.__others import filter_container_by_condition
from rl_data_utils.exceptions import ItemNotFound
from typing import Any


class ItemAttribute:
    def validate(self):
        if isinstance(self, ABCBaseColor):
            self.validate_color()
        if isinstance(self, ABCBaseRarity):
            self.validate_rarity()
        if isinstance(self, ABCBaseType):
            self.validate_type()
        if isinstance(self, ABCBaseCertified):
            self.validate_certified()

    def __eq__(self, other):
        return self.compare_items(other)

    def compare_items(self, item: Any[ABCBaseColor, ABCBaseRarity, ABCBaseType, ABCBaseCertified, ABCBaseName]):
        comparisons_results = []
        if isinstance(self, ABCBaseColor) and isinstance(item, ABCBaseColor):
            cc = self.compare_colors(item.get_color())
            comparisons_results.append(cc)
        if isinstance(self, ABCBaseRarity) and isinstance(item, ABCBaseRarity):
            rc = self.compare_rarities(item.get_rarity())
            comparisons_results.append(rc)
        if isinstance(self, ABCBaseType) and isinstance(item, ABCBaseType):
            tc = self.compare_types(item.get_type())
            comparisons_results.append(tc)
        if isinstance(self, ABCBaseCertified) and isinstance(item, ABCBaseCertified):
            cc = self.compare_certificates(item.get_certified())
            comparisons_results.append(cc)
        if isinstance(self, ABCBaseName) and isinstance(item, ABCBaseName):
            cn = self.compare_name(item.get_name())
            comparisons_results.append(cn)
        return all(comparisons_results)

    def item_attributes_to_dict(self) -> dict:
        attrs = {}
        if isinstance(self, ABCBaseColor):
            attrs['color'] = self.get_color()
        if isinstance(self, ABCBaseRarity):
            attrs['rarity'] = self.get_rarity()
        if isinstance(self, ABCBaseType):
            attrs['type_'] = self.get_type()
        if isinstance(self, ABCBaseCertified):
            attrs['certified'] = self.get_certified()
        if isinstance(self, ABCBaseName):
            attrs['name'] = self.get_name()
        if isinstance(self, ABCBaseQuantity):
            attrs['quantity'] = self.get_quantity()
        return attrs


def get_items_by_condition(lamb, items):
    return filter_container_by_condition(lamb, items)


def get_item_by_index(items, index=0):
    try:
        return items[index]
    except IndexError:
        raise ItemNotFound("Probably your search results in nothing.")

