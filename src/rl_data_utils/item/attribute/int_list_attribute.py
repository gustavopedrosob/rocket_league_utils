from rl_data_utils.item.attribute.int_attribute import IntAttribute
from rl_data_utils.item.attribute.list_attribute import ListAttribute


class IntListAttribute(ListAttribute):
    sub_attribute = IntAttribute
