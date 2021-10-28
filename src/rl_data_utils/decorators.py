from rl_data_utils import item, get_respective_rarity, get_respective_color, get_respective_type,\
    get_respective_certified
from rl_data_utils.colors.constants import COLORS
from rl_data_utils.types.constants import TYPES
from rl_data_utils.rarities.constants import RARITIES
from rl_data_utils.certificates.constants import CERTIFICATES


def validate_attributes(function):
    def new_func(*args, **kwargs):
        item.validate_attributes(**kwargs)
        return function(*args, **kwargs)
    return new_func


def rl_data_smart_attributes(rarity=True, color=True, type_=True, certified=True, rarities=RARITIES, colors=COLORS,
                             types=TYPES, certificates=CERTIFICATES):
    def decorator(function):
        def wrapper(*args, **kwargs):
            new_kwargs = {}
            if rarity:
                new_kwargs['rarity'] = get_respective_rarity(kwargs['rarity'], rarities)
            if color:
                new_kwargs['color'] = get_respective_color(kwargs['color'], colors)
            if type_:
                new_kwargs['type_'] = get_respective_type(kwargs['type_'], types)
            if certified:
                new_kwargs['certified'] = get_respective_certified(kwargs['certified'], certificates)
            kwargs.update(new_kwargs)
            return function(*args, **kwargs)
        return wrapper
    return decorator
