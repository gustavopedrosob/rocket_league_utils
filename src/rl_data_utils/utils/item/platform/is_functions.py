from functools import lru_cache

from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.platform.regexs import IS_SWITCH, IS_PS4, IS_XBOX, IS_PC


@lru_cache()
def is_pc(platform: str) -> bool:
    return _regex_found(IS_PC, platform)


@lru_cache()
def is_xbox(platform: str) -> bool:
    return _regex_found(IS_XBOX, platform)


@lru_cache()
def is_ps4(platform: str) -> bool:
    return _regex_found(IS_PS4, platform)


@lru_cache()
def is_switch(platform: str) -> bool:
    return _regex_found(IS_SWITCH, platform)


IS_FUNCTIONS = [is_pc, is_xbox, is_ps4, is_switch]
