from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.color.regexs import IS_BLACK, IS_BURNT_SIENNA, IS_COBALT, IS_CRIMSON, IS_DEFAULT, \
    IS_FOREST_GREEN, IS_GREY, IS_LIME, IS_ORANGE, IS_PINK, IS_PURPLE, IS_SAFFRON, IS_SKY_BLUE, IS_TITANIUM_WHITE
from functools import lru_cache


@lru_cache()
def is_black(color: str) -> bool:
    return _regex_found(IS_BLACK, color)


@lru_cache()
def is_burnt_sienna(color: str) -> bool:
    return _regex_found(IS_BURNT_SIENNA, color)


@lru_cache()
def is_cobalt(color: str) -> bool:
    return _regex_found(IS_COBALT, color)


@lru_cache()
def is_crimson(color: str) -> bool:
    return _regex_found(IS_CRIMSON, color)


@lru_cache()
def is_default(color: str) -> bool:
    return _regex_found(IS_DEFAULT, color)


@lru_cache()
def is_forest_green(color: str) -> bool:
    return _regex_found(IS_FOREST_GREEN, color)


@lru_cache()
def is_grey(color: str) -> bool:
    return _regex_found(IS_GREY, color)


@lru_cache()
def is_lime(color: str) -> bool:
    return _regex_found(IS_LIME, color)


@lru_cache()
def is_orange(color: str) -> bool:
    return _regex_found(IS_ORANGE, color)


@lru_cache()
def is_pink(color: str) -> bool:
    return _regex_found(IS_PINK, color)


@lru_cache()
def is_purple(color: str) -> bool:
    return _regex_found(IS_PURPLE, color)


@lru_cache()
def is_saffron(color: str) -> bool:
    return _regex_found(IS_SAFFRON, color)


@lru_cache()
def is_sky_blue(color: str) -> bool:
    return _regex_found(IS_SKY_BLUE, color)


@lru_cache()
def is_titanium_white(color: str) -> bool:
    return _regex_found(IS_TITANIUM_WHITE, color)


IS_FUNCTIONS = [is_black, is_burnt_sienna, is_cobalt, is_crimson, is_default, is_forest_green, is_grey, is_lime,
                is_orange, is_pink, is_purple, is_saffron, is_sky_blue, is_titanium_white]
