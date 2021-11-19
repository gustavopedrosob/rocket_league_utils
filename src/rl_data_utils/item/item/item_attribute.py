from rl_data_utils.utils.item_attributes.item_attributes import get_repr
from contextlib import suppress


class ItemAttribute:
    def validate(self):
        for name in ['color', 'rarity', 'type', 'certified']:
            with suppress(AttributeError):
                getattr(self, 'validate_' + name)()

    def __eq__(self, other):
        return self.compare_items(other)

    def __repr__(self):
        return get_repr(**self.item_attributes_to_dict())

    def is_valid(self) -> bool:
        for name in ['color', 'rarity', 'type', 'certified', 'serie']:
            with suppress(AttributeError):
                is_valid = getattr(self, 'is_valid_' + name)()
                if not is_valid:
                    return False
        return True

    def compare_items(self, item):
        for name in ['color', 'rarity', 'type', 'certified', 'name']:
            with suppress(AttributeError):
                cr = getattr(self, 'compare_' + name)(getattr(item, 'get_' + name)())
                if not cr:
                    return False
        return True

    def item_attributes_to_dict(self) -> dict:
        attrs = {}
        for name in ['color', 'rarity', 'type', 'certified', 'name', 'serie']:
            with suppress(AttributeError):
                value = getattr(self, 'get_' + name)()
                if value:
                    attrs[name] = value
        for name in ['quantity', 'tradable', 'paintable', 'blueprint']:
            with suppress(AttributeError):
                value = getattr(self, 'get_' + name)()
                attrs[name] = value
        return attrs

