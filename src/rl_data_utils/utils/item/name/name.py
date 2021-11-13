from rl_data_utils.__others import _regex_found
from rl_data_utils.exceptions import NameHaveNotCarName
from rl_data_utils.utils.item.name.constants import CARS_NAMES_WITH_DECAL
from rl_data_utils.utils.item.type.is_functions import is_decal
from functools import lru_cache
from contextlib import suppress


@lru_cache()
def compare_names(name_1: str, name_2: str) -> str:
    try:
        name_1 = get_string_decal_and_car_name(name_1)
    except NameHaveNotCarName:
        pass
    else:
        with suppress(NameHaveNotCarName):
            name_2 = get_string_decal_and_car_name(name_2)
    name_1 = f'^{name_1}$'.replace(' ', r'[_\- ]?')
    return _regex_found(name_1, name_2)


@lru_cache()
def get_decal_and_car_name(name: str):
    from re import search, sub, IGNORECASE
    result = search('|'.join(CARS_NAMES_WITH_DECAL), name, IGNORECASE)
    try:
        car_name = result.group(0)
    except AttributeError:
        raise NameHaveNotCarName(name)
    # remove car_name from string
    name = name.replace(car_name, '')
    # remove separators from name
    name = sub(r'[()[\]:]', r'', name)
    decal_name = name.strip()
    return decal_name, car_name


def get_string_decal_and_car_name(name: str) -> str:
    car_name, decal_name = get_decal_and_car_name(name)
    return f'{car_name} {decal_name}'


def has_car_decal_name_separator(name: str) -> bool:
    return _regex_found(r'[(\)\[\]:]', name)


def have_car_in_name(name: str):
    return _regex_found('|'.join(CARS_NAMES_WITH_DECAL), name)


def is_car_decal_name(name: str, type_: str = None) -> bool:
    if name and type_:
        return is_car_decal_name_by_name_and_type(name, type_)
    else:
        return is_car_decal_name_by_name(name)


def is_car_decal_name_by_name(name: str) -> bool:
    return have_car_in_name(name) and has_car_decal_name_separator(name)


def is_car_decal_name_by_name_and_type(name: str, type_: str) -> bool:
    return is_car_decal_name_by_name(name) and is_decal(type_)
