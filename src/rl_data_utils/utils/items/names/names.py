from re import IGNORECASE
from rl_data_utils.__others import _regex_found
from rl_data_utils.item.name.name import ABCName
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_by_name_regex(name_pattern: str, items: list[ABCName], flags=IGNORECASE):
    return get_items_by_condition(lambda item: _regex_found(name_pattern, item.get_name(), flags), items)


def get_names(items: list[ABCName]):
    return {item.get_name() for item in items}


def get_items_by_name(name: str, items: list[ABCName]):
    return get_items_by_condition(lambda item: item.compare_name(name), items)


def get_items_by_name_equal_to(name: str, items: list[ABCName]):
    return get_items_by_condition(lambda item: item.get_name() == name, items)


def get_items_by_name_contains(name: str, items: list[ABCName]):
    return get_items_by_condition(lambda item: name in item.get_name(), items)
