from abc import abstractmethod
from rl_data_utils.item.item.item_data import ItemDataAttribute
from rl_data_utils.utils.item.color.constants import BLACK, BURNT_SIENNA, COBALT, CRIMSON, DEFAULT, FOREST_GREEN, GREY,\
    LIME, ORANGE, PINK, PURPLE, SAFFRON, SKY_BLUE, TITANIUM_WHITE
from rl_data_utils.utils.item.platform.constants import PC, XBOX, PS4, SWITCH


class ABCPricePlatformColor(ItemDataAttribute):
    @abstractmethod
    def get_price_by_color_and_platform(self, color: str, platform: str):
        pass

    def get_price_pc_black(self):
        return self.get_price_by_color_and_platform(BLACK, PC)

    def get_price_pc_burnt_sienna(self):
        return self.get_price_by_color_and_platform(BURNT_SIENNA, PC)

    def get_price_pc_cobalt(self):
        return self.get_price_by_color_and_platform(COBALT, PC)

    def get_price_pc_crimson(self):
        return self.get_price_by_color_and_platform(CRIMSON, PC)

    def get_price_pc_default(self):
        return self.get_price_by_color_and_platform(DEFAULT, PC)

    def get_price_pc_forest_green(self):
        return self.get_price_by_color_and_platform(FOREST_GREEN, PC)

    def get_price_pc_grey(self):
        return self.get_price_by_color_and_platform(GREY, PC)

    def get_price_pc_lime(self):
        return self.get_price_by_color_and_platform(LIME, PC)

    def get_price_pc_orange(self):
        return self.get_price_by_color_and_platform(ORANGE, PC)

    def get_price_pc_pink(self):
        return self.get_price_by_color_and_platform(PINK, PC)

    def get_price_pc_purple(self):
        return self.get_price_by_color_and_platform(PURPLE, PC)

    def get_price_pc_saffron(self):
        return self.get_price_by_color_and_platform(SAFFRON, PC)

    def get_price_pc_sky_blue(self):
        return self.get_price_by_color_and_platform(SKY_BLUE, PC)

    def get_price_pc_titanium_white(self):
        return self.get_price_by_color_and_platform(TITANIUM_WHITE, PC)
    
    def get_price_xbox_black(self):
        return self.get_price_by_color_and_platform(BLACK, XBOX)

    def get_price_xbox_burnt_sienna(self):
        return self.get_price_by_color_and_platform(BURNT_SIENNA, XBOX)

    def get_price_xbox_cobalt(self):
        return self.get_price_by_color_and_platform(COBALT, XBOX)

    def get_price_xbox_crimson(self):
        return self.get_price_by_color_and_platform(CRIMSON, XBOX)

    def get_price_xbox_default(self):
        return self.get_price_by_color_and_platform(DEFAULT, XBOX)

    def get_price_xbox_forest_green(self):
        return self.get_price_by_color_and_platform(FOREST_GREEN, XBOX)

    def get_price_xbox_grey(self):
        return self.get_price_by_color_and_platform(GREY, XBOX)

    def get_price_xbox_lime(self):
        return self.get_price_by_color_and_platform(LIME, XBOX)

    def get_price_xbox_orange(self):
        return self.get_price_by_color_and_platform(ORANGE, XBOX)

    def get_price_xbox_pink(self):
        return self.get_price_by_color_and_platform(PINK, XBOX)

    def get_price_xbox_purple(self):
        return self.get_price_by_color_and_platform(PURPLE, XBOX)

    def get_price_xbox_saffron(self):
        return self.get_price_by_color_and_platform(SAFFRON, XBOX)

    def get_price_xbox_sky_blue(self):
        return self.get_price_by_color_and_platform(SKY_BLUE, XBOX)

    def get_price_xbox_titanium_white(self):
        return self.get_price_by_color_and_platform(TITANIUM_WHITE, XBOX)
    
    def get_price_ps4_black(self):
        return self.get_price_by_color_and_platform(BLACK, PS4)

    def get_price_ps4_burnt_sienna(self):
        return self.get_price_by_color_and_platform(BURNT_SIENNA, PS4)

    def get_price_ps4_cobalt(self):
        return self.get_price_by_color_and_platform(COBALT, PS4)

    def get_price_ps4_crimson(self):
        return self.get_price_by_color_and_platform(CRIMSON, PS4)

    def get_price_ps4_default(self):
        return self.get_price_by_color_and_platform(DEFAULT, PS4)

    def get_price_ps4_forest_green(self):
        return self.get_price_by_color_and_platform(FOREST_GREEN, PS4)

    def get_price_ps4_grey(self):
        return self.get_price_by_color_and_platform(GREY, PS4)

    def get_price_ps4_lime(self):
        return self.get_price_by_color_and_platform(LIME, PS4)

    def get_price_ps4_orange(self):
        return self.get_price_by_color_and_platform(ORANGE, PS4)

    def get_price_ps4_pink(self):
        return self.get_price_by_color_and_platform(PINK, PS4)

    def get_price_ps4_purple(self):
        return self.get_price_by_color_and_platform(PURPLE, PS4)

    def get_price_ps4_saffron(self):
        return self.get_price_by_color_and_platform(SAFFRON, PS4)

    def get_price_ps4_sky_blue(self):
        return self.get_price_by_color_and_platform(SKY_BLUE, PS4)

    def get_price_ps4_titanium_white(self):
        return self.get_price_by_color_and_platform(TITANIUM_WHITE, PS4)
    
    def get_price_switch_black(self):
        return self.get_price_by_color_and_platform(BLACK, SWITCH)

    def get_price_switch_burnt_sienna(self):
        return self.get_price_by_color_and_platform(BURNT_SIENNA, SWITCH)

    def get_price_switch_cobalt(self):
        return self.get_price_by_color_and_platform(COBALT, SWITCH)

    def get_price_switch_crimson(self):
        return self.get_price_by_color_and_platform(CRIMSON, SWITCH)

    def get_price_switch_default(self):
        return self.get_price_by_color_and_platform(DEFAULT, SWITCH)

    def get_price_switch_forest_green(self):
        return self.get_price_by_color_and_platform(FOREST_GREEN, SWITCH)

    def get_price_switch_grey(self):
        return self.get_price_by_color_and_platform(GREY, SWITCH)

    def get_price_switch_lime(self):
        return self.get_price_by_color_and_platform(LIME, SWITCH)

    def get_price_switch_orange(self):
        return self.get_price_by_color_and_platform(ORANGE, SWITCH)

    def get_price_switch_pink(self):
        return self.get_price_by_color_and_platform(PINK, SWITCH)

    def get_price_switch_purple(self):
        return self.get_price_by_color_and_platform(PURPLE, SWITCH)

    def get_price_switch_saffron(self):
        return self.get_price_by_color_and_platform(SAFFRON, SWITCH)

    def get_price_switch_sky_blue(self):
        return self.get_price_by_color_and_platform(SKY_BLUE, SWITCH)

    def get_price_switch_titanium_white(self):
        return self.get_price_by_color_and_platform(TITANIUM_WHITE, SWITCH)
