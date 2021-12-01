from rl_data_utils.item.attribute.attribute import Attribute
from rl_data_utils.item.attribute.attribute_info import AttributeInfo


class BoolAttribute(Attribute, AttributeInfo):
    attribute_type = bool
    undefined_value = None
