from rl_data_utils.type.is_functions import *
from rl_data_utils.type.constants import *
from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import TypeNotExists, InvalidTypesList
from rl_data_utils.type.contains import CONTAINS_FUNCTIONS
from rl_data_utils.type.regexs import CONTAINS_REGEXS
from rl_data_utils.type.abc_base_type import ABCBaseType
from rl_data_utils.item.item_attribute import ItemAttribute


class TypesFunctions(AttributesFunctions):
    is_functions = IS_FUNCTIONS
    contains_functions = CONTAINS_FUNCTIONS
    contains_regex = CONTAINS_REGEXS
    attribute_not_exists_exception = TypeNotExists
    invalid_attribute_list_exception = InvalidTypesList


def all_are_types(container):
    return TypesFunctions.all_are(container)


def compare_types(type_1: str, type_2: str) -> bool:
    return TypesFunctions.compare(type_1, type_2)


def contains_types(string: str) -> bool:
    return TypesFunctions.contains(string)


def contains_types_in_list(string: str, container: list) -> bool:
    return TypesFunctions.contains_in_list(string, container)


def get_respective_type(type_, types=TYPES):
    return TypesFunctions.get_respective(type_, types)


def get_type_in_string(string: str) -> str:
    return TypesFunctions.get_in_string(string)


def is_type(string: str) -> bool:
    return TypesFunctions.is_(string)


def is_type_list(container) -> bool:
    return TypesFunctions.validate_list(container)


def validate_type(string):
    return TypesFunctions.validate(string)


def validate_types_list(container):
    return TypesFunctions.validate_list(container)


class ABCType(ABCBaseType, ItemAttribute):
    def compare_types(self, type_: str) -> bool:
        return compare_types(self.get_type(), type_)

    def get_respective_type(self) -> str:
        return get_respective_type(self.get_type())

    def is_antenna(self) -> bool:
        return is_antenna(self.get_type())

    def is_avatar_border(self) -> bool:
        return is_avatar_border(self.get_type())

    def is_banner(self) -> bool:
        return is_banner(self.get_type())

    def is_boost(self) -> bool:
        return is_boost(self.get_type())

    def is_car(self) -> bool:
        return is_car(self.get_type())

    def is_decal(self) -> bool:
        return is_decal(self.get_type())

    def is_engine_audio(self) -> bool:
        return is_engine_audio(self.get_type())

    def is_gift_pack(self) -> bool:
        return is_gift_pack(self.get_type())

    def is_goal_explosion(self) -> bool:
        return is_goal_explosion(self.get_type())

    def is_paint_finish(self) -> bool:
        return is_paint_finish(self.get_type())

    def is_player_anthem(self):
        return is_player_anthem(self.get_type())

    def is_topper(self) -> bool:
        return is_topper(self.get_type())

    def is_trail(self) -> bool:
        return is_trail(self.get_type())

    def is_wheel(self) -> bool:
        return is_wheel(self.get_type())

    def validate_type(self):
        validate_type(self.get_type())


class Type(ABCType):
    def __init__(self, type_: str):
        self.type = type_

    def get_type(self):
        return self.type

    def set_type(self, type_: str):
        self.type = type_
