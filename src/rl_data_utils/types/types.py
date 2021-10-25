from rl_data_utils.types.is_functions import *
from rl_data_utils.types.constants import *
from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import TypeNotExists, InvalidTypesList
from rl_data_utils.types.contains import CONTAINS_FUNCTIONS
from rl_data_utils.types.regexs import CONTAINS_REGEXS


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


class Type:
    def __init__(self, type_: str):
        self.type = type_

    def compare_types(self, type_: str) -> bool:
        return compare_types(self.type, type_)

    def get_respective_type(self) -> str:
        return get_respective_type(self.type)

    def is_antenna(self) -> bool:
        return is_antenna(self.type)

    def is_avatar_border(self) -> bool:
        return is_avatar_border(self.type)

    def is_banner(self) -> bool:
        return is_banner(self.type)

    def is_boost(self) -> bool:
        return is_boost(self.type)

    def is_car(self) -> bool:
        return is_car(self.type)

    def is_decal(self) -> bool:
        return is_decal(self.type)

    def is_engine_audio(self) -> bool:
        return is_engine_audio(self.type)

    def is_gift_pack(self) -> bool:
        return is_gift_pack(self.type)

    def is_goal_explosion(self) -> bool:
        return is_goal_explosion(self.type)

    def is_paint_finish(self) -> bool:
        return is_paint_finish(self.type)

    def is_player_anthem(self):
        return is_player_anthem(self.type)

    def is_topper(self) -> bool:
        return is_topper(self.type)

    def is_trail(self) -> bool:
        return is_trail(self.type)

    def is_wheel(self) -> bool:
        return is_wheel(self.type)

    def validate_type(self):
        validate_type(self.type)
