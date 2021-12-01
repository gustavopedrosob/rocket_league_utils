from rl_data_utils.item import Serie
from rl_data_utils.item.attribute.str_list_attribute import StrListAttribute
from rl_data_utils.item.serie.serie_info import SerieInfo


class Series(StrListAttribute, SerieInfo):
    sub_attribute = Serie
