from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import CertifiedNotExists, InvalidCertificatesList
from rl_data_utils.utils.item.certified.constants import CERTIFICATES
from rl_data_utils.utils.item.certified.contains import CONTAINS_FUNCTIONS
from rl_data_utils.utils.item.certified.regexs import CONTAINS_REGEXS
from rl_data_utils.utils.item.certified.is_functions import IS_FUNCTIONS


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
