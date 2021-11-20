from rl_data_utils.utils.item_attributes.item_attributes import get_repr
from contextlib import suppress


class ItemAttribute:
    def validate(self):
        for name in ['color', 'rarity', 'slot', 'certified', 'serie']:
            with suppress(AttributeError):
                if getattr(self, 'get_' + name)() is not None:
                    getattr(self, 'validate_' + name)()

    def __eq__(self, other):
        return self.compare_items(other)

    def __repr__(self):
        return get_repr(**ItemAttribute.item_attributes_to_dict(self))

    def is_valid(self) -> bool:
        for name in ['color', 'rarity', 'slot', 'certified', 'serie']:
            with suppress(AttributeError):
                if getattr(self, 'get_' + name)() is not None:
                    is_valid = getattr(self, 'is_valid_' + name)()
                    if not is_valid:
                        return False
        return True

    def compare_attributes(self, **kwargs):
        for name in ['color', 'rarity', 'slot', 'certified', 'name']:
            with suppress((AttributeError, KeyError)):
                value = kwargs[name]
                if isinstance(value, str):
                    cr = getattr(self, 'compare_' + name)(value)
                elif isinstance(value, list):
                    cr = getattr(self, 'is_' + name + '_in_list')(value)
                elif value is None:
                    continue
                else:
                    raise TypeError()
                if cr is False:
                    return False
        return True

    def compare_items(self, item):
        return self.compare_attributes(**item.item_attributes_to_dict())

    def item_attributes_to_dict(self) -> dict:
        kwargs = {}
        for name in ['color', 'rarity', 'slot', 'certified', 'name', 'serie', 'quantity', 'tradable', 'paintable',
                     'blueprint']:
            with suppress(AttributeError):
                value = getattr(self, 'get_' + name)()
                if value is not None:
                    kwargs[name] = value
        return kwargs

