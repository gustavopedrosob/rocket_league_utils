from rl_data_utils.names.is_functions import is_credits
from rl_data_utils.types.is_functions import is_decal
from rl_data_utils.__others import _regex_found
from rl_data_utils.names.constants import CARS_NAMES_WITH_DECAL


def compare_names(name_1: str, name_2: str, type_1: str = None, type_2: str = None) -> str:
    if is_car_decal_name(name_1, type_1):
        name_1 = get_string_decal_and_car_name(name_1)
    if is_car_decal_name(name_2, type_2):
        name_2 = get_string_decal_and_car_name(name_2)
    name_1 = f'^{name_1}$'.replace(' ', r'[_\- ]?')
    return _regex_found(name_1, name_2)


def get_decal_and_car_name(name: str):
    from re import search, sub, IGNORECASE
    result = search('|'.join(CARS_NAMES_WITH_DECAL), name, IGNORECASE)
    car_name = result.group(0)
    # remove car_name from string
    name = name.replace(car_name, '')
    # remove separators from name
    name = sub(r'[(\)\[\]:]', r'', name)
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


class Name:
    def __init__(self, name: str):
        self.name = name

    def have_car_in_name(self) -> bool:
        return have_car_in_name(self.name)

    def is_credits(self) -> bool:
        return is_credits(self.name)

    def compare_name(self, name: str) -> bool:
        return compare_names(self.name, name)
