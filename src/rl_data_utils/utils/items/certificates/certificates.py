from re import IGNORECASE
from rl_data_utils.__others import _regex_found
from rl_data_utils.item.certified.certified import ABCCertified
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_with_valid_certified(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_valid_certified(), items)


def get_certificates(items: list[ABCCertified]):
    return {item.get_certified() for item in items}


def get_items_by_certified(certified: str, items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.compare_certificates(certified), items)


def get_items_by_certified_equal_to(certified: str, items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.get_certified() == certified, items)


def get_items_by_certified_contains(certified: str, items: list[ABCCertified]):
    return get_items_by_condition(lambda item: certified in item.get_certified(), items)


def get_items_by_certified_regex(certified_pattern: str, items: list[ABCCertified], flags=IGNORECASE):
    return get_items_by_condition(lambda item: _regex_found(certified_pattern, item.get_certified(), flags), items)


def get_items_aviator(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_aviator(), items)


def get_items_acrobat(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_acrobat(), items)


def get_items_victor(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_victor(), items)


def get_items_striker(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_striker(), items)


def get_items_sniper(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_sniper(), items)


def get_items_scorer(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_scorer(), items)


def get_items_playmaker(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_playmaker(), items)


def get_items_guardian(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_guardian(), items)


def get_items_paragon(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_paragon(), items)


def get_items_sweeper(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_sweeper(), items)


def get_items_turtle(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_turtle(), items)


def get_items_tactician(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_tactician(), items)


def get_items_showoff(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_show_off(), items)


def get_items_juggler(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_juggler(), items)


def get_items_goalkeeper(items: list[ABCCertified]):
    return get_items_by_condition(lambda item: item.is_goalkeeper(), items)
