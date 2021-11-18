from abc import abstractmethod, ABC
from rl_data_utils.utils.item.color.constants import BLACK, BURNT_SIENNA, COBALT, CRIMSON, DEFAULT, FOREST_GREEN, GREY,\
    LIME, ORANGE, PINK, PURPLE, SAFFRON, SKY_BLUE, TITANIUM_WHITE


class ABCPriceColor(ABC):
    @abstractmethod
    def get_price_by_color(self, color: str):
        pass
    
    def get_price_by_color_black(self):
        return self.get_price_by_color(BLACK)

    def get_price_by_color_burnt_sienna(self):
        return self.get_price_by_color(BURNT_SIENNA)

    def get_price_by_color_cobalt(self):
        return self.get_price_by_color(COBALT)

    def get_price_by_color_crimson(self):
        return self.get_price_by_color(CRIMSON)

    def get_price_by_color_default(self):
        return self.get_price_by_color(DEFAULT)

    def get_price_by_color_forest_green(self):
        return self.get_price_by_color(FOREST_GREEN)

    def get_price_by_color_grey(self):
        return self.get_price_by_color(GREY)

    def get_price_by_color_lime(self):
        return self.get_price_by_color(LIME)

    def get_price_by_color_orange(self):
        return self.get_price_by_color(ORANGE)

    def get_price_by_color_pink(self):
        return self.get_price_by_color(PINK)

    def get_price_by_color_purple(self):
        return self.get_price_by_color(PURPLE)

    def get_price_by_color_saffron(self):
        return self.get_price_by_color(SAFFRON)

    def get_price_by_color_sky_blue(self):
        return self.get_price_by_color(SKY_BLUE)

    def get_price_by_color_titanium_white(self):
        return self.get_price_by_color(TITANIUM_WHITE)
