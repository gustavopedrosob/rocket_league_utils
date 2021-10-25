from rl_data_utils.names.is_functions import is_credits
from rl_data_utils.types.is_functions import is_decal
from rl_data_utils.__others import _regex_found
from rl_data_utils.names.constants import CARS_NAMES_WITH_DECAL


def compare_names(name_1: str, name_2: str) -> str:
    pattern = name_1.replace(' ', r'[_\- ]?')
    return _regex_found(pattern, name_2)


def have_car_in_name(name: str):
    return _regex_found('|'.join(CARS_NAMES_WITH_DECAL), name)


def is_car_decal_name(name: str, type_: str):
    return have_car_in_name(name) and is_decal(type_)


class Name:
    def __init__(self, name: str):
        self.name = name

    def have_car_in_name(self) -> bool:
        return have_car_in_name(self.name)

    def is_credits(self) -> bool:
        return is_credits(self.name)

    def compare_name(self, name: str) -> bool:
        return compare_names(self.name, name)
