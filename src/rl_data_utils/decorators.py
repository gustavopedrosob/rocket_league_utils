from contextlib import suppress
from rl_data_utils.utils.item.certified.certified import get_respective_certified
from rl_data_utils.utils.item.color.color import get_respective_color
from rl_data_utils.utils.item.color.constants import COLORS
from rl_data_utils.utils.item.certified.constants import CERTIFICATES
from rl_data_utils.utils.item.rarity.constants import RARITIES
from rl_data_utils.utils.item.rarity.rarity import get_respective_rarity
from rl_data_utils.utils.item.type.constants import TYPES
from rl_data_utils.utils.item.type.type import get_respective_type
from rl_data_utils.utils.item_attributes.item_attributes import validate_attributes as _validate_attributes


def validate_attributes(function):
    def new_func(*args, **kwargs):
        _validate_attributes(**kwargs)
        return function(*args, **kwargs)
    return new_func


def rl_data_smart_attributes(sub_rarity=True, sub_color=True, sub_type=True, sub_certified=True, rarities=RARITIES,
                             colors=COLORS, types=TYPES, certificates=CERTIFICATES):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if sub_rarity:
                with suppress(KeyError):
                    kwargs['rarity'] = get_respective_rarity(kwargs['rarity'], rarities)
            if sub_color:
                with suppress(KeyError):
                    kwargs['color'] = get_respective_color(kwargs['color'], colors)
            if sub_type:
                with suppress(KeyError):
                    kwargs['type_'] = get_respective_type(kwargs['type_'], types)
            if sub_certified:
                with suppress(KeyError):
                    kwargs['certified'] = get_respective_certified(kwargs['certified'], certificates)
            return function(*args, **kwargs)
        return wrapper
    return decorator
