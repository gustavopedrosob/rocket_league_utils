from rl_data_utils.exceptions import SerieIsNotInString
from rl_data_utils.item.attribute.attribute_string import AttributeString
from rl_data_utils.item.serie.regexs import CONTAINS
from rl_data_utils.item.serie.serie import Serie
from rl_data_utils.item.serie.serie_info import SerieInfo


class SerieString(AttributeString, SerieInfo):
    attribute_class = Serie
    contains_reg = CONTAINS
    is_not_in_string_exception = SerieIsNotInString
