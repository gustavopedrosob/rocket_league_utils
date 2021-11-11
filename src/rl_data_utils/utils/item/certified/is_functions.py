from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.certified.regexs import IS_ACROBAT, IS_AVIATOR, IS_GOALKEEPER, IS_GUARDIAN, IS_JUGGLER, \
    IS_PARAGON, IS_PLAYMAKER, IS_SCORER, IS_SHOW_OFF, IS_SNIPER, IS_STRIKER, IS_SWEEPER, IS_TACTICIAN, IS_TURTLE, \
    IS_VICTOR, IS_NONE
from functools import lru_cache


@lru_cache()
def is_acrobat(certified: str) -> bool:
    return _regex_found(IS_ACROBAT, certified)


@lru_cache()
def is_aviator(certified: str) -> bool:
    return _regex_found(IS_AVIATOR, certified)


@lru_cache()
def is_goalkeeper(certified: str) -> bool:
    return _regex_found(IS_GOALKEEPER, certified)


@lru_cache()
def is_guardian(certified: str) -> bool:
    return _regex_found(IS_GUARDIAN, certified)


@lru_cache()
def is_juggler(certified: str) -> bool:
    return _regex_found(IS_JUGGLER, certified)


@lru_cache()
def is_paragon(certified: str) -> bool:
    return _regex_found(IS_PARAGON, certified)


@lru_cache()
def is_playmaker(certified: str) -> bool:
    return _regex_found(IS_PLAYMAKER, certified)


@lru_cache()
def is_scorer(certified: str) -> bool:
    return _regex_found(IS_SCORER, certified)


@lru_cache()
def is_show_off(certified: str) -> bool:
    return _regex_found(IS_SHOW_OFF, certified)


@lru_cache()
def is_sniper(certified: str) -> bool:
    return _regex_found(IS_SNIPER, certified)


@lru_cache()
def is_striker(certified: str) -> bool:
    return _regex_found(IS_STRIKER, certified)


@lru_cache()
def is_sweeper(certified: str) -> bool:
    return _regex_found(IS_SWEEPER, certified)


@lru_cache()
def is_tactician(certified: str) -> bool:
    return _regex_found(IS_TACTICIAN, certified)


@lru_cache()
def is_turtle(certified: str) -> bool:
    return _regex_found(IS_TURTLE, certified)


@lru_cache()
def is_victor(certified: str) -> bool:
    return _regex_found(IS_VICTOR, certified)


@lru_cache()
def is_none(certified: str) -> bool:
    return _regex_found(IS_NONE, certified)


IS_FUNCTIONS = [is_acrobat, is_aviator, is_goalkeeper, is_guardian, is_juggler, is_paragon, is_playmaker, is_scorer,
                is_show_off, is_sniper, is_striker, is_sweeper, is_tactician, is_turtle, is_victor, is_none]
