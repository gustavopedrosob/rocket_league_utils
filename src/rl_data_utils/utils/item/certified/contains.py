from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.certified.regexs import CONTAINS_ACROBAT, CONTAINS_AVIATOR, CONTAINS_GOALKEEPER, \
    CONTAINS_GUARDIAN, CONTAINS_JUGGLER, CONTAINS_NONE, CONTAINS_PARAGON, CONTAINS_PLAYMAKER, CONTAINS_SCORER, \
    CONTAINS_SHOW_OFF, CONTAINS_SNIPER, CONTAINS_STRIKER, CONTAINS_SWEEPER, CONTAINS_TACTICIAN, CONTAINS_TURTLE, \
    CONTAINS_VICTOR


def contains_acrobat(certified: str) -> bool:
    return _regex_found(CONTAINS_ACROBAT, certified)


def contains_aviator(certified: str) -> bool:
    return _regex_found(CONTAINS_AVIATOR, certified)


def contains_goalkeeper(certified: str) -> bool:
    return _regex_found(CONTAINS_GOALKEEPER, certified)


def contains_guardian(certified: str) -> bool:
    return _regex_found(CONTAINS_GUARDIAN, certified)


def contains_juggler(certified: str) -> bool:
    return _regex_found(CONTAINS_JUGGLER, certified)


def contains_none(certified: str) -> bool:
    return _regex_found(CONTAINS_NONE, certified)


def contains_paragon(certified: str) -> bool:
    return _regex_found(CONTAINS_PARAGON, certified)


def contains_playmaker(certified: str) -> bool:
    return _regex_found(CONTAINS_PLAYMAKER, certified)


def contains_scorer(certified: str) -> bool:
    return _regex_found(CONTAINS_SCORER, certified)


def contains_show_off(certified: str) -> bool:
    return _regex_found(CONTAINS_SHOW_OFF, certified)


def contains_sniper(certified: str) -> bool:
    return _regex_found(CONTAINS_SNIPER, certified)


def contains_striker(certified: str) -> bool:
    return _regex_found(CONTAINS_STRIKER, certified)


def contains_sweeper(certified: str) -> bool:
    return _regex_found(CONTAINS_SWEEPER, certified)


def contains_tactician(certified: str) -> bool:
    return _regex_found(CONTAINS_TACTICIAN, certified)


def contains_turtle(certified: str) -> bool:
    return _regex_found(CONTAINS_TURTLE, certified)


def contains_victor(certified: str) -> bool:
    return _regex_found(CONTAINS_VICTOR, certified)


CONTAINS_FUNCTIONS = [contains_acrobat, contains_aviator, contains_goalkeeper, contains_guardian, contains_juggler,
                      contains_none, contains_paragon, contains_playmaker, contains_scorer,
                      contains_show_off, contains_sniper, contains_striker, contains_sweeper, contains_tactician,
                      contains_turtle, contains_victor]
