from rl_data_utils.item.attribute_data.attribute_data import AttributesData, AttributesManagement
from rl_data_utils.item.price.data_price import DataPrice
from rl_data_utils.item.price.price import PriceInfo


class PriceData(AttributesData, PriceInfo, AttributesManagement):
    sub_attribute = DataPrice

    def __init__(self, prices):
        self.prices = prices
        super().__init__(self.prices)

    def get_price(self,
                  color=None,
                  platform=None,
                  blueprint=None):
        data_prices = self.prices
        for attr in filter(lambda t: bool(t), (color, platform, blueprint)):
            data_prices = list(filter(
                lambda dp: attr.compare(getattr(dp, attr.identifier)), data_prices))
        data_price = data_prices[0]
        return data_price.price, data_price.crafting_cost
