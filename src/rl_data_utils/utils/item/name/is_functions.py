from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.name.regexs import IS_CREDITS


def is_credits(name: str) -> bool:
    return _regex_found(IS_CREDITS, name)
