from rl_data_utils.item.item_attribute import get_items_by_condition
from rl_data_utils.items.abc_items import ABCItems
from rl_data_utils.color.color import ABCColor
from re import IGNORECASE
from rl_data_utils.__others import _regex_found
from rl_data_utils.colors.abc_base_colors import ABCBaseColors


class ABCColors(ABCBaseColors, ABCItems):
    def get_items_by_color_regex(self, color_pattern: str, flags=IGNORECASE):
        return get_items_by_color_regex(color_pattern, self.get_items(), flags)

    def get_items_by_color(self, color: str, items=None):
        if items is None:
            items = self.get_items()
        return get_items_by_color(color, items)

    def get_items_by_color_equal_to(self, color: str):
        return get_items_by_color_equal_to(color, self.get_items())

    def get_items_by_color_contains(self, color: str):
        return get_items_by_color_contains(color, self.get_items())

    def get_colors(self):
        return get_colors(self.get_items())

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


def get_colors(items: list[ABCColor]):
    return {item.get_color() for item in items}


def get_items_by_color(color: str, items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.compare_colors(color), items)


def get_items_by_color_regex(color_pattern: str, items: list[ABCColor], flags=IGNORECASE):
    return get_items_by_condition(lambda item: _regex_found(color_pattern, item.get_color(), flags), items)


def get_items_by_color_equal_to(color: str, items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.get_color() == color, items)


def get_items_by_color_contains(color: str, items: list[ABCColor]):
    return get_items_by_condition(lambda item: color in item.get_color(), items)


def get_items_crimson(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_crimson(), items)


def get_items_sky_blue(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_sky_blue(), items)


def get_items_pink(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_pink(), items)


def get_items_orange(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_orange(), items)


def get_items_cobalt(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_cobalt(), items)


def get_items_burnt_sienna(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_burnt_sienna(), items)


def get_items_titanium_white(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_titanium_white(), items)


def get_items_grey(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_grey(), items)


def get_items_saffron(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_saffron(), items)


def get_items_lime(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_lime(), items)


def get_items_forest_green(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_forest_green(), items)


def get_items_black(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_black(), items)


def get_items_purple(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_purple(), items)
