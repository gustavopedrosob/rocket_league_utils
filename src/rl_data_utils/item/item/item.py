from rl_data_utils.utils.item_attributes.item_attributes import get_attributes_in_string
from rl_data_utils.item.blueprint.blueprint import ABCBlueprint
from rl_data_utils.item.certified.certified import ABCCertified
from rl_data_utils.item.color.color import ABCColor
from rl_data_utils.item.name.name import ABCName
from rl_data_utils.item.paintable.paintable import ABCPaintable
from rl_data_utils.item.platform.platform import ABCPlatform
from rl_data_utils.item.price.price import ABCPrice
from rl_data_utils.item.quantity.quantity import ABCQuantity
from rl_data_utils.item.rarity.rarity import ABCRarity
from rl_data_utils.item.serie.serie import ABCSerie
from rl_data_utils.item.tradable.tradable import ABCTradable
from rl_data_utils.item.type.type import ABCType


class Item(ABCBlueprint, ABCCertified, ABCColor, ABCName, ABCPaintable, ABCPlatform, ABCPrice, ABCQuantity, ABCRarity,
           ABCSerie, ABCTradable, ABCType):
    def __init__(self, name: str, type: str, color: str = None, rarity: str = None, certified: str = None,
                 quantity: int = None, blueprint: bool = None, paintable: bool = None, platform: str = None,
                 price: list[int] = None, serie: str = None, tradable: bool = None):
        self.name = name
        self.color = color
        self.type = type
        self.rarity = rarity
        self.certified = certified
        self.quantity = quantity
        self.blueprint = blueprint
        self.paintable = paintable
        self.platform = platform
        self.price = price
        self.serie = serie
        self.tradable = tradable

    def get_blueprint(self) -> bool:
        pass

    def get_paintable(self) -> bool:
        pass

    def get_platform(self) -> str:
        pass

    def get_price(self) -> list[int]:
        pass

    def get_serie(self) -> str:
        pass

    def get_tradable(self) -> bool:
        pass

    def get_certified(self):
        return self.certified

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def get_rarity(self):
        return self.rarity

    def get_type(self):
        return self.type

    def get_quantity(self) -> int:
        return self.quantity

    @staticmethod
    def from_string(string: str):
        return Item(**get_attributes_in_string(string))
