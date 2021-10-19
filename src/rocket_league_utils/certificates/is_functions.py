from rocket_league_utils.__others import _regex_found
from rocket_league_utils.certificates.constants import *


def is_aviator(certified: str) -> bool:
    return "aviator" in certified.lower()


def is_acrobat(certified: str) -> bool:
    return "acrobat" in certified.lower()


def is_victor(certified: str) -> bool:
    return "victor" in certified.lower()


def is_striker(certified: str) -> bool:
    return "striker" in certified.lower()


def is_sniper(certified: str) -> bool:
    return "sniper" in certified.lower()


def is_scorer(certified: str) -> bool:
    return "scorer" in certified.lower()


def is_playmaker(certified: str) -> bool:
    return "playmaker" in certified.lower()


def is_guardian(certified: str) -> bool:
    return "guardian" in certified.lower()


def is_paragon(certified: str) -> bool:
    return "paragon" in certified.lower()


def is_sweeper(certified: str) -> bool:
    return "sweeper" in certified.lower()


def is_turtle(certified: str) -> bool:
    return "turtle" in certified.lower()


def is_tactician(certified: str) -> bool:
    return "tactician" in certified.lower()


def is_show_off(certified: str) -> bool:
    return _regex_found(r"show[_\- ]?off", certified)


def is_juggler(certified: str) -> bool:
    return "juggler" in certified.lower()


def is_goalkeeper(certified: str) -> bool:
    return "goalkeeper" in certified.lower()
