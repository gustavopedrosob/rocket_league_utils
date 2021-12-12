from typing import Union

from rl_data_utils.item.attribute.attribute_info import AttributeInfo


class AttributeString(AttributeInfo):
    def __init__(self, string: str):
        self.string: str = string


InitializeAttributeString = Union[AttributeString, str]
