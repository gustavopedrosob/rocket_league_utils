from statistics import mean
from rl_data_utils.item.attribute.int_list_attribute import IntListAttribute
from rl_data_utils.item.price.price_info import PriceInfo
from rl_data_utils.item.quantity.credits_quantity import CreditsQuantity


class Price(IntListAttribute, PriceInfo):
    sub_attribute = CreditsQuantity

    def get_average(self) -> CreditsQuantity:
        return mean([attr.attribute for attr in self.attribute])
