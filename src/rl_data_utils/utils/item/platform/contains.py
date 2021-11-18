from functools import lru_cache

from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.platform.regexs import CONTAINS_SWITCH, CONTAINS_PS4, CONTAINS_XBOX, CONTAINS_PC


@lru_cache()
def contains_pc(platform: str) -> bool:
    return _regex_found(CONTAINS_PC, platform)


@lru_cache()
def contains_xbox(platform: str) -> bool:
    return _regex_found(CONTAINS_XBOX, platform)


@lru_cache()
def contains_ps4(platform: str) -> bool:
    return _regex_found(CONTAINS_PS4, platform)


@lru_cache()
def contains_switch(platform: str) -> bool:
    return _regex_found(CONTAINS_SWITCH, platform)


CONTAINS_FUNCTIONS = [contains_pc, contains_xbox, contains_ps4, contains_switch]
