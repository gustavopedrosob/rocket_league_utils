from rl_data_utils.exceptions import CertifiedIsNotInString
from rl_data_utils.item import Certified
from rl_data_utils.item.attribute.attribute_string import AttributeString
from rl_data_utils.item.certified.certified_info import CertifiedInfo
from rl_data_utils.item.certified.regexs import CONTAINS


class CertifiedString(AttributeString, CertifiedInfo):
    attribute_class = Certified
    contains_reg = CONTAINS
    is_not_in_string_exception = CertifiedIsNotInString

