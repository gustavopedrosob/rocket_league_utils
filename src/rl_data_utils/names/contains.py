from rl_data_utils.__others import _regex_found
from rl_data_utils.names.regexs import *


def contains_credits(name: str) -> bool:
    return _regex_found(CONTAINS_CREDITS, name)
