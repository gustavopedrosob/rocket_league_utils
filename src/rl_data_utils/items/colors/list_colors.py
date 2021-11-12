from re import IGNORECASE
from rl_data_utils.utils.items.colors.list_colors import get_items_by_color, get_items_by_color_regex, \
    get_items_by_color_equal_to, get_items_by_color_contains, get_items_crimson, get_items_sky_blue, get_items_pink, \
    get_items_orange, get_items_cobalt, get_items_burnt_sienna, get_items_titanium_white, get_items_grey, \
    get_items_saffron, get_items_lime, get_items_forest_green, get_items_black, get_items_purple, \
    get_items_with_valid_color
from rl_data_utils.items.colors.abc_base_colors import ABCBaseColors
from rl_data_utils.items.items.items import Items


class ListColors(ABCBaseColors, Items):
    def get_items_with_valid_color(self):
        return self.__class__(get_items_with_valid_color(self.items))

    def get_items_by_color(self, color: str):
        return self.__class__(get_items_by_color(color, self.items))

    def get_items_by_color_regex(self, color_pattern: str, flags=IGNORECASE):
        return self.__class__(get_items_by_color_regex(color_pattern, self.items, flags))

    def get_items_by_color_equal_to(self, color: str):
        return self.__class__(get_items_by_color_equal_to(color, self.items))

    def get_items_by_color_contains(self, color: str):
        return self.__class__(get_items_by_color_contains(color, self.items))

    def get_colors(self):
        result = set()
        for item in self.items:
            result.update(item.get_list_color())
        return result

    def get_items_crimson(self):
        return self.__class__(get_items_crimson(self.items))

    def get_items_sky_blue(self):
        return self.__class__(get_items_sky_blue(self.items))

    def get_items_pink(self):
        return self.__class__(get_items_pink(self.items))

    def get_items_orange(self):
        return self.__class__(get_items_orange(self.items))

    def get_items_cobalt(self):
        return self.__class__(get_items_cobalt(self.items))

    def get_items_burnt_sienna(self):
        return self.__class__(get_items_burnt_sienna(self.items))

    def get_items_titanium_white(self):
        return self.__class__(get_items_titanium_white(self.items))

    def get_items_grey(self):
        return self.__class__(get_items_grey(self.items))

    def get_items_saffron(self):
        return self.__class__(get_items_saffron(self.items))

    def get_items_lime(self):
        return self.__class__(get_items_lime(self.items))

    def get_items_forest_green(self):
        return self.__class__(get_items_forest_green(self.items))

    def get_items_black(self):
        return self.__class__(get_items_black(self.items))

    def get_items_purple(self):
        return self.__class__(get_items_purple(self.items))
