from rl_data_utils.utils.items.certificates.certificates import get_certificates, get_items_by_certified, \
    get_items_by_certified_equal_to, get_items_by_certified_contains, get_items_by_certified_regex, get_items_aviator, \
    get_items_acrobat, get_items_victor, get_items_striker, get_items_sniper, get_items_scorer, get_items_playmaker, \
    get_items_guardian, get_items_paragon, get_items_sweeper, get_items_turtle, get_items_tactician, get_items_showoff, \
    get_items_juggler, get_items_goalkeeper
from rl_data_utils.items.items.items import ABCItems
from re import IGNORECASE
from rl_data_utils.items.certificates.abc_base_certificates import ABCBaseCertificates


class ABCCertificates(ABCBaseCertificates, ABCItems):
    def get_items_by_certified_regex(self, certified_pattern, flags=IGNORECASE):
        return get_items_by_certified_regex(certified_pattern, self.get_items(), flags)

    def get_items_by_certified(self, certified: str, items=None):
        if items is None:
            items = self.get_items()
        return get_items_by_certified(certified, items)

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
