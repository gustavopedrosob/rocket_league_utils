from __future__ import annotations

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.certified.constants import CERTIFICATES, NONE
from rl_data_utils.item.certified.regexs import REGEX_TABLE
from rl_data_utils.item.item.constants import CERTIFIED
from rl_data_utils.rocket_league.rocket_league import Defaultable


class CertifiedInfo(AttributeInfo):
    identifier = CERTIFIED
    order = 5


class Certified(RegexBasedItemAttribute, CertifiedInfo, Defaultable):
    regex_table = REGEX_TABLE
    possible_values = CERTIFICATES
    default_args = [NONE], dict()


class Certificates(RegexBasedListAttribute, CertifiedInfo):
    attribute_class = Certified
