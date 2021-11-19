from contextlib import suppress
from rl_data_utils.exceptions import ItemNotFound
from rl_data_utils.utils.item_attributes.item_attributes import get_attributes_in_string
from rl_data_utils.utils.items.items.items import get_items_by_condition, get_item_by_index


class Items:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        for item in self.items:
            yield item

    def get_items_valid(self):
        items = self
        for name in ['certified', 'color', 'rarity', 'type', 'serie']:
            with suppress(AttributeError):
                items = getattr(items, 'get_items_with_valid_' + name)()
        return items

    def get_items_by_condition(self, lamb):
        return self.__class__(get_items_by_condition(lamb, self.items))

    def get_items_by(self, **kwargs):
        items = self
        get_something = False
        for name in ['certified', 'color', 'rarity', 'type', 'name']:
            try:
                items = getattr(items, 'get_items_by_' + name)(kwargs[name])
                get_something = True
            except (KeyError, AttributeError):
                pass
        if not get_something:
            raise ItemNotFound()
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
