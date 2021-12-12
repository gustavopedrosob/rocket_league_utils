from typing import Union, Final, Optional, List

from rl_data_utils.exceptions import SerieNotExists, SerieIsNotInString
from rl_data_utils.item.attribute.attribute_dict import AttributeDict
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedAttribute
from rl_data_utils.item.attribute.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.attribute_string.regex_based_attribute_string import RegexBasedAttributeString
from rl_data_utils.item.serie.constants import SERIES
from rl_data_utils.item.serie.regexs import CONTAINS


class SerieInfo(AttributeInfo):
    attribute_name: Final[str] = 'serie'
    order: Final[int] = 8


class Serie(RegexBasedAttribute, SerieInfo):
    _attribute_not_exists_exception = SerieNotExists
    _is_reg = CONTAINS
    constants = SERIES


Serie.default_value = Serie.undefined_value


InitializeSerie = Union[Serie, str, None]


SetSeries = Optional[List[InitializeSerie]]


class Series(RegexBasedListAttribute, SerieInfo):
    sub_attribute = Serie
    default_value = SERIES


class SerieDict(AttributeDict):
    _cls_attribute = Serie
    _cls_list_attribute = Series


class SerieString(RegexBasedAttributeString, SerieInfo):
    attribute_class = Serie
    attributes_class = Series
    contains_reg = CONTAINS
    is_not_in_string_exception = SerieIsNotInString
