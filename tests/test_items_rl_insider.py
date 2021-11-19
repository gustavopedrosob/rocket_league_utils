from json import load

from rl_data_utils.item import ABCName, ABCPaintable, ABCType
from rl_data_utils.item.price.price_platform_color import ABCPricePlatformColor
from rl_data_utils.items import Names, Paintables, Types
from rl_data_utils.utils.item.platform.platform import get_respective_platform


class Item(ABCName, ABCPaintable, ABCPricePlatformColor, ABCType):
    def get_name(self):
        return self.name

    def get_paintable(self) -> bool:
        return self.paintable

    def get_price_by_color_and_platform(self, color: str, platform: str):
        return self.prices[get_respective_platform(platform), color]

    def get_type(self):
        return self.type

    def __init__(self, name, paintable, prices, type_):
        self.name = name
        self.paintable = paintable
        self.prices = prices
        self.type = type_


class InsiderItems(Names, Paintables, Types):
    pass


with open('sample-items-rl-insider.json') as file:
    json = load(file)

sample_items = InsiderItems([Item(**item) for item in json])
