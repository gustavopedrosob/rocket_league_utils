from collections import Callable

from contextlib import suppress

from rl_data_utils.item.certified.certified import CertifiedString
from rl_data_utils.item.color.color import ColorString
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.rarity.rarity import RarityString
from rl_data_utils.item.slot.slot import SlotString


def validate_attributes(function: Callable) -> Callable:
    def new_func(*args, **kwargs):
        Item(**kwargs).validate()
        return function(*args, **kwargs)
    return new_func


def respective_attributes(function: Callable) -> Callable:
    def new_func(*args, **kwargs):
        for cls in [RarityString, ColorString, SlotString, CertifiedString]:
            with suppress(KeyError):
                kwargs[cls.attribute_name] = cls(kwargs[cls.attribute_name]).get_respective()
        return function(*args, **kwargs)
    return new_func
