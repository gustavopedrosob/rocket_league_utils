from rl_data_utils.__others import _regex_found
from rl_data_utils.item.attribute.attribute_string import AttributeString
from rl_data_utils.item.name.regexs import *


class NameString(AttributeString):
    def contains_credits(self) -> bool:
        return _regex_found(CONTAINS_CREDITS, self.string)
