from typing import Union, Literal, Final

from rl_data_utils.exceptions import CertifiedNotExists, CertifiedIsNotInString
from rl_data_utils.item.attribute.attribute_dict import AttributeDict
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedAttribute, SetRegexBasedAttribute
from rl_data_utils.item.attribute.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.attribute_string.regex_based_attribute_string import RegexBasedAttributeString
from rl_data_utils.item.certified.constants import CERTIFICATES
from rl_data_utils.item.certified.regexs import CONTAINS

CertifiedPatternKey = Literal["Aviator", "Acrobat", "Goalkeeper", "Guardian", "Juggler", "None", "Paragon", "Playmaker",
                              "Scorer", "Show-off", "Sniper", "Striker", "Sweeper", "Tactician", "Turtle", "Victor"]


class CertifiedInfo(AttributeInfo):
    attribute_name: Final[str] = 'certified'
    order: Final[int] = 5


class Certified(RegexBasedAttribute, CertifiedInfo):
    _attribute_not_exists_exception = CertifiedNotExists
    _is_reg = CONTAINS
    constants = CERTIFICATES


Certified.default_value = Certified.undefined_value


InitializeCertified = Union[Certified, str, None]


class Certificates(RegexBasedListAttribute, CertifiedInfo):
    sub_attribute = Certified
    default_value = CERTIFICATES


class CertifiedDict(AttributeDict):
    _cls_attribute = Certified
    _cls_list_attribute = Certificates


class CertifiedString(RegexBasedAttributeString, CertifiedInfo):
    attribute_class = Certified
    attributes_class = Certificates
    contains_reg = CONTAINS
    is_not_in_string_exception = CertifiedIsNotInString


class HasCertified(CertifiedInfo):
    def __init__(self, certified: InitializeCertified = None):
        self.certified: Certified = certified

    def get_certified(self) -> Certified:
        return self._certified

    def set_certified(self, value: SetRegexBasedAttribute):
        self._certified = Certified.initialize(value)

    certified = property(get_certified, set_certified)
