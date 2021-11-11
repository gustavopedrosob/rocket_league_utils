from rl_data_utils.utils.items.items.items import get_items_by_condition, get_item_by_index
from rl_data_utils.items.certificates.abc_base_certificates import ABCBaseCertificates
from rl_data_utils.items.colors.abc_base_colors import ABCBaseColors
from rl_data_utils.items.rarities.abc_base_rarities import ABCBaseRarities
from rl_data_utils.items.types.abc_base_types import ABCBaseTypes
from rl_data_utils.items.names.abc_base_names import ABCBaseNames
from rl_data_utils.utils.item_attributes.item_attributes import get_attributes_in_string


class Items:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        for item in self.items:
            yield item

    def get_items_by_condition(self, lamb):
        return self.__class__(get_items_by_condition(lamb, self.items))

    def get_items_by(self, **kwargs):
        items = self
        if isinstance(items, ABCBaseCertificates) and 'certified' in kwargs:
            items = items.get_items_by_certified(kwargs['certified'])
        if isinstance(items, ABCBaseColors) and 'color' in kwargs:
            items = items.get_items_by_color(kwargs['color'])
        if isinstance(items, ABCBaseRarities) and 'rarity' in kwargs:
            items = items.get_items_by_rarity(kwargs['rarity'])
        if isinstance(items, ABCBaseTypes) and 'type_' in kwargs:
            items = items.get_items_by_type(kwargs['type_'])
        if isinstance(items, ABCBaseNames) and 'name' in kwargs:
            items = items.get_items_by_name(kwargs['name'])
        return items

    def get_item_by(self, index=0, **kwargs):
        return get_item_by_index(self.get_items_by(**kwargs).items, index)

    def get_items_by_string(self, string):
        kw = get_attributes_in_string(string)
        return self.get_items_by(**kw)

    def get_item_by_string(self, string, index=0):
        return get_item_by_index(self.get_items_by_string(string).items, index)

    def get_items_by_item(self, item):
        kw = item.item_attributes_to_dict()
        return self.get_items_by(**kw)

    def get_item_by_item(self, item, index=0):
        return get_item_by_index(self.get_items_by_item(item).items, index)

    def get_item_by_index(self, index=0):
        return get_item_by_index(self.items, index)
