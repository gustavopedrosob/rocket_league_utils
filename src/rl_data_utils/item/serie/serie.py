from __future__ import annotations

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.item.constants import SERIE
from rl_data_utils.item.serie.constants import SERIES
from rl_data_utils.item.serie.regexs import REGEX_TABLE


class SerieInfo(AttributeInfo):
    identifier = SERIE
    order = 8


class Serie(RegexBasedItemAttribute, SerieInfo):
    regex_table = REGEX_TABLE
    possible_values = SERIES


class Series(RegexBasedListAttribute, SerieInfo):
    attribute_class = Serie
