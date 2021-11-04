from rl_data_utils.colors.colors import ABCColors
from rl_data_utils.color.list_color import get_items_by_color, get_items_by_color_regex, get_items_by_color_equal_to,\
    get_items_by_color_contains
from rl_data_utils.color.list_color import get_items_crimson, get_items_sky_blue, get_items_pink, get_items_orange,\
    get_items_cobalt, get_items_burnt_sienna, get_items_titanium_white, get_items_grey, get_items_saffron,\
    get_items_lime, get_items_forest_green, get_items_black, get_items_purple
from re import IGNORECASE


class ABCListColors(ABCColors):
    def get_items_by_color(self, color: str):
        return get_items_by_color(color, self.get_items())

    def get_items_by_color_regex(self, color_pattern: str, flags=IGNORECASE):
        return get_items_by_color_regex(color_pattern, self.get_items(), flags)

    def get_items_by_color_equal_to(self, color: str):
        return get_items_by_color_equal_to(color, self.get_items())

    def get_items_by_color_contains(self, color: str):
        return get_items_by_color_contains(color, self.get_items())

    def get_items_crimson(self):
        return get_items_crimson(self.get_items())

    def get_items_sky_blue(self):
        return get_items_sky_blue(self.get_items())

    def get_items_pink(self):
        return get_items_pink(self.get_items())

    def get_items_orange(self):
        return get_items_orange(self.get_items())

    def get_items_cobalt(self):
        return get_items_cobalt(self.get_items())

    def get_items_burnt_sienna(self):
        return get_items_burnt_sienna(self.get_items())

    def get_items_titanium_white(self):
        return get_items_titanium_white(self.get_items())

    def get_items_grey(self):
        return get_items_grey(self.get_items())

    def get_items_saffron(self):
        return get_items_saffron(self.get_items())

    def get_items_lime(self):
        return get_items_lime(self.get_items())

    def get_items_forest_green(self):
        return get_items_forest_green(self.get_items())

    def get_items_black(self):
        return get_items_black(self.get_items())

    def get_items_purple(self):
        return get_items_purple(self.get_items())
