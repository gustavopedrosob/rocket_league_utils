from re import search, IGNORECASE

from rl_data_utils.utils.item.serie.constants import SERIES


def _regex_found(pattern, string, flags=IGNORECASE) -> bool:
    return bool(search(pattern, string, flags))


def filter_container_by_condition(lamb, container) -> list:
    return list(filter(lamb, container))


def _regex_found_any_in_list(pattern: str, container: list[str], flags=IGNORECASE):
    return any([_regex_found(pattern, string, flags) for string in container])


class AttributesFunctions:
    is_functions = []
    contains_functions = []
    contains_regex = []
    attribute_not_exists_exception = None
    invalid_attribute_list_exception = None
    is_not_in_string_exception = None

    @classmethod
    def is_(cls, string: str) -> bool:
        return any(map(lambda f: f(string), cls.is_functions))

    @classmethod
    def compare(cls, string_1: str, string_2: str) -> bool:
        cls.validate(string_1)
        cls.validate(string_2)
        return any(map(lambda f: f(string_1) and f(string_2), cls.is_functions))

    @classmethod
    def all_are(cls, container):
        return all(map(lambda e: cls.is_(e), container))

    @classmethod
    def validate(cls, string):
        if not cls.is_(string):
            raise cls.attribute_not_exists_exception(string)

    @classmethod
    def validate_list(cls, container):
        if not cls.all_are(container):
            raise cls.invalid_attribute_list_exception()

    @classmethod
    def get_respective(cls, string: str, container):
        cls.validate(string)
        cls.validate_list(container)
        for e in container:
            if cls.compare(string, e):
                return e

    @classmethod
    def contains(cls, string):
        return any(map(lambda f: f(string), cls.contains_functions))

    @classmethod
    def has(cls, string, container):
        cls.validate(string)
        cls.validate_list(container)
        return any(map(lambda e: cls.compare(string, e), container))

    @classmethod
    def get_in_string(cls, string):
        result = search('|'.join(cls.contains_regex), string, IGNORECASE)
        try:
            return result.group(0)
        except AttributeError:
            raise cls.is_not_in_string_exception()
