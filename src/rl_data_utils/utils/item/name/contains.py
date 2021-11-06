from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.name.regexs import CONTAINS_CREDITS


def contains_credits(name: str) -> bool:
    return _regex_found(CONTAINS_CREDITS, name)
