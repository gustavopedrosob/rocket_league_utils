from rl_data_utils.item.certified.abc_base_certified import ABCBaseCertified
from rl_data_utils.item.item.item_attribute import ItemAttribute
from rl_data_utils.utils.item.certified.certified import compare_certificates, get_respective_certified,\
    validate_certified, is_certified
from rl_data_utils.utils.item.certified.is_functions import is_acrobat, is_aviator, is_goalkeeper, is_guardian,\
    is_juggler, is_paragon, is_playmaker, is_scorer, is_show_off, is_sniper, is_striker, is_sweeper, is_tactician,\
    is_turtle, is_victor, is_none


class ABCCertified(ABCBaseCertified, ItemAttribute):
    def is_valid_certified(self):
        return is_certified(self.get_certified())

    def compare_certificates(self, certified: str) -> bool:
        return compare_certificates(self.get_certified(), certified)

    def get_respective_certified(self) -> str:
        return get_respective_certified(self.get_certified())

    def is_acrobat(self) -> bool:
        return is_acrobat(self.get_certified())

    def is_aviator(self) -> bool:
        return is_aviator(self.get_certified())

    def is_goalkeeper(self) -> bool:
        return is_goalkeeper(self.get_certified())

    def is_guardian(self) -> bool:
        return is_guardian(self.get_certified())

    def is_juggler(self) -> bool:
        return is_juggler(self.get_certified())

    def is_paragon(self) -> bool:
        return is_paragon(self.get_certified())

    def is_playmaker(self) -> bool:
        return is_playmaker(self.get_certified())

    def is_scorer(self) -> bool:
        return is_scorer(self.get_certified())

    def is_show_off(self) -> bool:
        return is_show_off(self.get_certified())

    def is_sniper(self) -> bool:
        return is_sniper(self.get_certified())

    def is_striker(self) -> bool:
        return is_striker(self.get_certified())

    def is_sweeper(self) -> bool:
        return is_sweeper(self.get_certified())

    def is_tactician(self) -> bool:
        return is_tactician(self.get_certified())

    def is_turtle(self) -> bool:
        return is_turtle(self.get_certified())

    def is_victor(self) -> bool:
        return is_victor(self.get_certified())

    def is_none(self) -> bool:
        return is_none(self.get_certified())

    def validate_certified(self):
        validate_certified(self.get_certified())


class Certified(ABCCertified):
    def __init__(self, certified: str):
        self.certified = certified

    def get_certified(self):
        return self.certified

    def set_certified(self, certified: str):
        self.certified = certified
