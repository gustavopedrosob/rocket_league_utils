from rl_data_utils.utils.item.name.is_functions import is_credits
from rl_data_utils.item.name.abc_base_name import ABCBaseName
from rl_data_utils.item.item.item_attribute import ItemAttribute
from rl_data_utils.utils.item.name.name import compare_names, get_decal_and_car_name, get_string_decal_and_car_name, \
    have_car_in_name


class ABCName(ABCBaseName, ItemAttribute):
    def have_car_in_name(self) -> bool:
        return have_car_in_name(self.get_name())

    def is_credits(self) -> bool:
        return is_credits(self.get_name())

    def compare_name(self, name: str) -> bool:
        return compare_names(self.get_name(), name)
    
    def get_decal_and_car_name(self):
        return get_decal_and_car_name(self.get_name())

    def get_string_decal_and_car_name(self):
        return get_string_decal_and_car_name(self.get_name())


class Name(ABCName):
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name
