from rl_data_utils.item.abc_item import get_items_by_condition
from rl_data_utils.items.abc_items import ABCItems
from rl_data_utils.certified.certified import ABCCertified, validate_certified
from rl_data_utils.__others import _regex_found
from re import IGNORECASE


class ABCCertificates(ABCItems):
    def get_items_by_certified_regex(self, certified_pattern, flags=IGNORECASE):
        return get_items_by_certified_regex(certified_pattern, self.get_items(), flags)

    def get_items_by_certified(self, certified: str):
        return get_items_by_certified(certified, self.get_items())

    def get_items_by_certified_equal_to(self, certified: str):
        return get_items_by_certified_equal_to(certified, self.get_items())

    def get_items_by_certified_contains(self, certified: str):
        return get_items_by_certified_contains(certified, self.get_items())

    def get_certificates(self):
        return get_certificates(self.get_items())

    def get_items_aviator(self):
        return get_items_aviator(self.get_items())

    def get_items_acrobat(self):
        return get_items_acrobat(self.get_items())

    def get_items_victor(self):
        return get_items_victor(self.get_items())

    def get_items_striker(self):
        return get_items_striker(self.get_items())

    def get_items_sniper(self):
        return get_items_sniper(self.get_items())

    def get_items_scorer(self):
        return get_items_scorer(self.get_items())

    def get_items_playmaker(self):
        return get_items_playmaker(self.get_items())

    def get_items_guardian(self):
        return get_items_guardian(self.get_items())

    def get_items_paragon(self):
        return get_items_paragon(self.get_items())

    def get_items_sweeper(self):
        return get_items_sweeper(self.get_items())

    def get_items_turtle(self):
        return get_items_turtle(self.get_items())

    def get_items_tactician(self):
        return get_items_tactician(self.get_items())

    def get_items_showoff(self):
        return get_items_showoff(self.get_items())

    def get_items_juggler(self):
        return get_items_juggler(self.get_items())

    def get_items_goalkeeper(self):
        return get_items_goalkeeper(self.get_items())


def get_certificates(items: list[ABCCertified]):
    return {item.get_certified() for item in items}


def get_items_by_certified(certified: str, items: list[ABCCertified]):
    validate_certified(certified)
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
