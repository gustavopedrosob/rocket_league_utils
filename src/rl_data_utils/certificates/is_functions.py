from rl_data_utils.__others import _regex_found
from rl_data_utils.certificates.regexs import *


def is_acrobat(certified: str) -> bool:
    return _regex_found(IS_ACROBAT, certified)


def is_aviator(certified: str) -> bool:
    return _regex_found(IS_AVIATOR, certified)


def is_goalkeeper(certified: str) -> bool:
    return _regex_found(IS_GOALKEEPER, certified)


def is_guardian(certified: str) -> bool:
    return _regex_found(IS_GUARDIAN, certified)


def is_juggler(certified: str) -> bool:
    return _regex_found(IS_JUGGLER, certified)


def is_paragon(certified: str) -> bool:
    return _regex_found(IS_PARAGON, certified)


def is_playmaker(certified: str) -> bool:
    return _regex_found(IS_PLAYMAKER, certified)


def is_scorer(certified: str) -> bool:
    return _regex_found(IS_SCORER, certified)


def is_show_off(certified: str) -> bool:
    return _regex_found(IS_SHOW_OFF, certified)


def is_sniper(certified: str) -> bool:
    return _regex_found(IS_SNIPER, certified)


def is_striker(certified: str) -> bool:
    return _regex_found(IS_STRIKER, certified)


def is_sweeper(certified: str) -> bool:
    return _regex_found(IS_SWEEPER, certified)


def is_tactician(certified: str) -> bool:
    return _regex_found(IS_TACTICIAN, certified)


def is_turtle(certified: str) -> bool:
    return _regex_found(IS_TURTLE, certified)


def is_victor(certified: str) -> bool:
    return _regex_found(IS_VICTOR, certified)


IS_FUNCTIONS = [is_acrobat, is_aviator, is_goalkeeper, is_guardian, is_juggler, is_paragon, is_playmaker, is_scorer,
                is_show_off, is_sniper, is_striker, is_sweeper, is_tactician, is_turtle, is_victor]
