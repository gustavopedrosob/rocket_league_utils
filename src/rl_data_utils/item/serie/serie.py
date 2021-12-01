from rl_data_utils.exceptions import SerieNotExists
from rl_data_utils.item.attribute.str_attribute import StrAttribute
from rl_data_utils.item.serie.regexs import CONTAINS
from rl_data_utils.item.serie.serie_info import SerieInfo


class Serie(StrAttribute, SerieInfo):
    _attribute_not_exists_exception = SerieNotExists
    _is_reg = CONTAINS
