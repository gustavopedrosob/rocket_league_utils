from rl_data_utils import get_respective_rarity, get_respective_color, get_respective_type,\
    get_respective_certified
from rl_data_utils.color.constants import COLORS
from rl_data_utils.type.constants import TYPES
from rl_data_utils.rarity.constants import RARITIES
from rl_data_utils.certified.constants import CERTIFICATES
from rl_data_utils.item import utils


def validate_attributes(function):
    def new_func(*args, **kwargs):
        utils.validate_attributes(**kwargs)
        return function(*args, **kwargs)
    return new_func


def rl_data_smart_attributes(sub_rarity=True, sub_color=True, sub_type=True, sub_certified=True, rarities=RARITIES,
                             colors=COLORS, types=TYPES, certificates=CERTIFICATES):
    def decorator(function):
        def wrapper(*args, **kwargs):
            new_kwargs = {}
            if sub_rarity:
                rarity = kwargs.get('rarity')
                if rarity:
                    new_kwargs['rarity'] = get_respective_rarity(rarity, rarities)
            if sub_color:
                color = kwargs.get('color')
                if color:
                    new_kwargs['color'] = get_respective_color(color, colors)
            if sub_type:
                type_ = kwargs.get('type_')
                if type_:
                    new_kwargs['type_'] = get_respective_type(type_, types)
            if sub_certified:
                certified = kwargs.get('certified')
                if certified:
                    new_kwargs['certified'] = get_respective_certified(certified, certificates)
            kwargs.update(new_kwargs)
            return function(*args, **kwargs)
        return wrapper
    return decorator
