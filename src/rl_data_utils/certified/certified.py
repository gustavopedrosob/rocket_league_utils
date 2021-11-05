from rl_data_utils.certified.is_functions import *
from rl_data_utils.certified.contains import CONTAINS_FUNCTIONS
from rl_data_utils.certified.constants import CERTIFICATES
from rl_data_utils.certified.regexs import CONTAINS_REGEXS
from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import CertifiedNotExists, InvalidCertificatesList
from rl_data_utils.certified.abc_base_certified import ABCBaseCertified
from rl_data_utils.item.item_attribute import ItemAttribute


class CertificatesFunctions(AttributesFunctions):
    is_functions = IS_FUNCTIONS
    contains_functions = CONTAINS_FUNCTIONS
    contains_regex = CONTAINS_REGEXS
    attribute_not_exists_exception = CertifiedNotExists
    invalid_attribute_list_exception = InvalidCertificatesList


def all_are_certificates(container):
    return CertificatesFunctions.all_are(container)


def compare_certificates(certify_1: str, certify_2: str) -> bool:
    return CertificatesFunctions.compare(certify_1, certify_2)


def contains_certificates(string: str) -> bool:
    return CertificatesFunctions.contains(string)


def contains_certificates_in_list(string: str, container: list) -> bool:
    return CertificatesFunctions.contains_in_list(string, container)


def get_certified_in_string(string: str) -> str:
    return CertificatesFunctions.get_in_string(string)


def get_respective_certified(certified, certificates=CERTIFICATES):
    return CertificatesFunctions.get_respective(certified, certificates)


def is_certified(string: str) -> bool:
    return CertificatesFunctions.is_(string)


def is_certificates_list(container) -> bool:
    return CertificatesFunctions.validate_list(container)


def validate_certificates_list(container):
    return CertificatesFunctions.validate_list(container)


def validate_certified(string):
    return CertificatesFunctions.validate(string)


class ABCCertified(ABCBaseCertified, ItemAttribute):
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

    def validate_certified(self):
        validate_certified(self.get_certified())


class Certified(ABCCertified):
    def __init__(self, certified: str):
        self.certified = certified

    def get_certified(self):
        return self.certified

    def set_certified(self, certified: str):
        self.certified = certified
