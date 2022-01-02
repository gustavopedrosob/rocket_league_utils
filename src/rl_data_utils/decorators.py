from contextlib import suppress

from rl_data_utils.item.item.constants import RARITY, COLOR, SLOT, CERTIFIED, SERIE, PLATFORM


def respective_attributes(function):
    def new_func(*args, **kwargs):
        for identifier in [RARITY, COLOR, SLOT, CERTIFIED, SERIE, PLATFORM]:
            with suppress(KeyError):
                value = kwargs[identifier]
                kwargs[identifier] = value.get_respective()
        return function(*args, **kwargs)
    return new_func
