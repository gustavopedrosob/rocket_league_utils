from abc import abstractmethod, ABC
from contextlib import suppress
from rl_data_utils.item.item.item_attribute import ItemAttribute


class ItemDataAttribute(ABC, ItemAttribute):
    def validate(self):
        super().validate()
        for name in ['color', 'rarity', 'serie']:
            with suppress(AttributeError):
                value = getattr(self, 'get_list_' + name)()
                if value is not None:
                    getattr(self, 'validate_' + name + '_list')()

    @abstractmethod
    def to_item(self, **kwargs):
        pass

    def is_valid(self) -> bool:
        is_valid = super().is_valid()
        if is_valid is False:
            return False
        for name in ['color', 'rarity', 'serie']:
            with suppress(AttributeError):
                value = getattr(self, 'get_list_' + name)()
                if value is not None:
                    is_valid = getattr(self, 'is_valid_list_' + name)()
                    if is_valid is False:
                        return False
        return True

    def compare_attributes(self, **kwargs):
        cr = super().compare_attributes(**kwargs)
        if cr is False:
            return False
        for name in ['color', 'rarity', 'serie']:
            with suppress((AttributeError, KeyError)):
                value = kwargs[name]
                if isinstance(value, str):
                    cr = getattr(self, 'contains_' + name)(value)
                elif value is None:
                    continue
                else:
                    raise TypeError()
                if cr is False:
                    return False
        return True

    def item_attributes_to_dict(self) -> dict:
        kwargs = super().item_attributes_to_dict()
        for name in ['color', 'rarity', 'serie']:
            with suppress(AttributeError):
                value = getattr(self, 'get_list_' + name)()
                if value is None:
                    kwargs[name] = value
        return kwargs
