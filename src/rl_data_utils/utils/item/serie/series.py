from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import SerieNotExists, InvalidSeriesList
from rl_data_utils.utils.item.serie.constants import SERIES
from rl_data_utils.utils.item.serie.contains import CONTAINS_FUNCTIONS
from rl_data_utils.utils.item.serie.regexs import CONTAINS_REGEXS
from rl_data_utils.utils.item.serie.is_functions import IS_FUNCTIONS
from functools import lru_cache


class SeriesFunctions(AttributesFunctions):
    is_functions = IS_FUNCTIONS
    contains_functions = CONTAINS_FUNCTIONS
    contains_regex = CONTAINS_REGEXS
    attribute_not_exists_exception = SerieNotExists
    invalid_attribute_list_exception = InvalidSeriesList


def all_are_series(container):
    return SeriesFunctions.all_are(container)


@lru_cache()
def compare_series(certify_1: str, certify_2: str) -> bool:
    return SeriesFunctions.compare(certify_1, certify_2)


def contains_series(string: str) -> bool:
    return SeriesFunctions.contains(string)


def has_serie(string: str, container: list) -> bool:
    return SeriesFunctions.has(string, container)


def get_serie_in_string(string: str) -> str:
    return SeriesFunctions.get_in_string(string)


def get_respective_serie(serie, series=SERIES):
    return SeriesFunctions.get_respective(serie, series)


def is_serie(string: str) -> bool:
    return SeriesFunctions.is_(string)


def validate_series_list(container):
    return SeriesFunctions.validate_list(container)


def validate_serie(string):
    return SeriesFunctions.validate(string)
