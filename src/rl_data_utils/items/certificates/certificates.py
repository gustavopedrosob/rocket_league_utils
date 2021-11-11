from rl_data_utils.utils.items.certificates.certificates import get_certificates, get_items_by_certified, \
    get_items_by_certified_equal_to, get_items_by_certified_contains, get_items_by_certified_regex, get_items_aviator, \
    get_items_acrobat, get_items_victor, get_items_striker, get_items_sniper, get_items_scorer, get_items_playmaker, \
    get_items_guardian, get_items_paragon, get_items_sweeper, get_items_turtle, get_items_tactician, get_items_showoff, \
    get_items_juggler, get_items_goalkeeper
from rl_data_utils.items.items.items import Items
from re import IGNORECASE
from rl_data_utils.items.certificates.abc_base_certificates import ABCBaseCertificates


class Certificates(ABCBaseCertificates, Items):
    def get_items_by_certified_regex(self, certified_pattern, flags=IGNORECASE):
        return self.__class__(get_items_by_certified_regex(certified_pattern, self.items, flags))

    def get_items_by_certified(self, certified: str):
        return self.__class__(get_items_by_certified(certified, self.items))

    def get_items_by_certified_equal_to(self, certified: str):
        return self.__class__(get_items_by_certified_equal_to(certified, self.items))

    def get_items_by_certified_contains(self, certified: str):
        return self.__class__(get_items_by_certified_contains(certified, self.items))

    def get_certificates(self):
        return get_certificates(self.items)

    def get_items_aviator(self):
        return self.__class__(get_items_aviator(self.items))

    def get_items_acrobat(self):
        return self.__class__(get_items_acrobat(self.items))

    def get_items_victor(self):
        return self.__class__(get_items_victor(self.items))

    def get_items_striker(self):
        return self.__class__(get_items_striker(self.items))

    def get_items_sniper(self):
        return self.__class__(get_items_sniper(self.items))

    def get_items_scorer(self):
        return self.__class__(get_items_scorer(self.items))

    def get_items_playmaker(self):
        return self.__class__(get_items_playmaker(self.items))

    def get_items_guardian(self):
        return self.__class__(get_items_guardian(self.items))

    def get_items_paragon(self):
        return self.__class__(get_items_paragon(self.items))

    def get_items_sweeper(self):
        return self.__class__(get_items_sweeper(self.items))

    def get_items_turtle(self):
        return self.__class__(get_items_turtle(self.items))

    def get_items_tactician(self):
        return self.__class__(get_items_tactician(self.items))

    def get_items_showoff(self):
        return self.__class__(get_items_showoff(self.items))

    def get_items_juggler(self):
        return self.__class__(get_items_juggler(self.items))

    def get_items_goalkeeper(self):
        return self.__class__(get_items_goalkeeper(self.items))
