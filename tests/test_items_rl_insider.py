from json import load
from rl_data_utils.item import ABCName, ABCPaintable, ABCType, ABCPrice
from rl_data_utils.item.price.price_platform_color import ABCPricePlatformColor
from rl_data_utils.items import Names, Paintables, Types
from rl_data_utils.utils.item.platform.platform import get_respective_platform


class ItemData(ABCName, ABCPaintable, ABCPricePlatformColor, ABCType):

    def __init__(self, name, paintable, prices, type_):
        self.name = name
        self.paintable = paintable
        self.prices = prices
        self.type = type_

    def to_item(self, **kwargs):
        color = kwargs.get('color', 'default')
        platform = kwargs.get('platform', 'pc')
        return Item(self.name, self.type, self.paintable, self.get_price_by_color_and_platform(color, platform))

    def get_name(self):
        return self.name

    def get_paintable(self) -> bool:
        return self.paintable

    def get_price_by_color_and_platform(self, color: str, platform: str):
        return self.prices[get_respective_platform(platform), color]

    def get_type(self):
        return self.type


class Item(ABCName, ABCPaintable, ABCPrice, ABCType):

    def __init__(self, name, type_, paintable, prices):
        self.name = name
        self.paintable = paintable
        self.prices = prices
        self.type = type_

    def get_name(self):
        return self.name

    def get_paintable(self) -> bool:
        return self.paintable

    def get_price(self) -> list[int]:
        return self.prices

    def get_type(self):
        return self.type


class InsiderItems(Names, Paintables, Types):
    pass


with open('sample-items-rl-insider.json') as file:
    json = load(file)

sample_items = InsiderItems([ItemData(**item) for item in json])
