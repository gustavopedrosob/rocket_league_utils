from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import TypeNotExists, InvalidTypesList
from rl_data_utils.utils.item.type.constants import TYPES
from rl_data_utils.utils.item.type.contains import CONTAINS_FUNCTIONS
from rl_data_utils.utils.item.type.is_functions import IS_FUNCTIONS
from rl_data_utils.utils.item.type.regexs import CONTAINS_REGEXS


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


def has_type(string: str, container: list) -> bool:
    return TypesFunctions.has(string, container)


def get_respective_type(type_, types=TYPES):
    return TypesFunctions.get_respective(type_, types)


def get_type_in_string(string: str) -> str:
    return TypesFunctions.get_in_string(string)


def is_type(string: str) -> bool:
    return TypesFunctions.is_(string)


def validate_type(string):
    return TypesFunctions.validate(string)


def validate_types_list(container):
    return TypesFunctions.validate_list(container)