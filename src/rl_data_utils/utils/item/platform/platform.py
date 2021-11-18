from functools import lru_cache
from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import PlatformNotExists, InvalidPlatformsList, PlatformIsNotInString
from rl_data_utils.utils.item.platform.constants import PLATFORMS


class PlatformsFunctions(AttributesFunctions):
    is_functions = IS_FUNCTIONS
    contains_functions = CONTAINS_FUNCTIONS
    contains_regex = CONTAINS_REGEXS
    attribute_not_exists_exception = PlatformNotExists
    invalid_attribute_list_exception = InvalidPlatformsList
    is_not_in_string_exception = PlatformIsNotInString


def all_are_platforms(container):
    return PlatformsFunctions.all_are(container)


@lru_cache()
def compare_platforms(platform_1: str, platform_2: str) -> bool:
    return PlatformsFunctions.compare(platform_1, platform_2)


def contains_platforms(string: str):
    return PlatformsFunctions.contains(string)


def has_platform(string: str, container: list) -> bool:
    return PlatformsFunctions.has(string, container)


def get_platform_in_string(string: str) -> str:
    return PlatformsFunctions.get_in_string(string)


def get_respective_platform(platform, platforms=PLATFORMS):
    return PlatformsFunctions.get_respective(platform, platforms)


def is_platform(string: str) -> bool:
    return PlatformsFunctions.is_(string)


def validate_platforms_list(container):
    return PlatformsFunctions.validate_list(container)


def validate_platform(string):
    return PlatformsFunctions.validate(string)
