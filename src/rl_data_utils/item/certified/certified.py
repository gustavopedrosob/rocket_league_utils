from rl_data_utils.exceptions import CertifiedNotExists
from rl_data_utils.item.certified.certified_info import CertifiedInfo
from rl_data_utils.item.certified.regexs import CONTAINS
from rl_data_utils.item.attribute.str_attribute import StrAttribute


class Certified(StrAttribute, CertifiedInfo):
    _attribute_not_exists_exception = CertifiedNotExists
    _is_reg = CONTAINS
