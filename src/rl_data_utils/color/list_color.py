from abc import abstractmethod
from rl_data_utils.color.color import contains_color_in_list, get_respective_color
from rl_data_utils.item.abc_item import get_items_by_condition
from rl_data_utils.__others import _regex_found_any_in_list
from re import IGNORECASE
from rl_data_utils.color.has_functions import *
from rl_data_utils.exceptions import ItemHaveNotColor


class ABCListColor:
    @abstractmethod
    def get_list_color(self) -> list[str]:
        pass

    def contains_color(self, color: str):
        return contains_color_in_list(color, self.get_list_color())

    def validate_contains_color(self, color: str):
        if not self.contains_color(color):
            raise ItemHaveNotColor(color)

    def get_respective_color(self, color: str):
        return get_respective_color(color, self.get_list_color())

    def has_black(self) -> bool:
        return has_black(self.get_list_color())

    def has_burnt_sienna(self) -> bool:
        return has_burnt_sienna(self.get_list_color())

    def has_cobalt(self) -> bool:
        return has_cobalt(self.get_list_color())

    def has_crimson(self) -> bool:
        return has_crimson(self.get_list_color())

    def has_default(self) -> bool:
        return has_default(self.get_list_color())

    def has_forest_green(self) -> bool:
        return has_forest_green(self.get_list_color())

    def has_grey(self) -> bool:
        return has_grey(self.get_list_color())

    def has_lime(self) -> bool:
        return has_lime(self.get_list_color())

    def has_orange(self) -> bool:
        return has_orange(self.get_list_color())

    def has_pink(self) -> bool:
        return has_pink(self.get_list_color())

    def has_purple(self) -> bool:
        return has_purple(self.get_list_color())

    def has_saffron(self) -> bool:
        return has_saffron(self.get_list_color())

    def has_sky_blue(self) -> bool:
        return has_sky_blue(self.get_list_color())

    def has_titanium_white(self) -> bool:
        return has_titanium_white(self.get_list_color())


def get_items_by_color(color: str, items: list[ABCListColor]):
    return get_items_by_condition(lambda item: contains_color_in_list(color, item.get_list_color()),
                                  items)


def get_items_by_color_regex(color_pattern: str, items: list[ABCListColor], flags=IGNORECASE):
    return get_items_by_condition(
        lambda list_color: _regex_found_any_in_list(color_pattern, list_color.get_list_color(), flags), items)


def get_items_by_color_equal_to(color: str, items: list[ABCListColor]):
    return get_items_by_condition(lambda item: color in item.get_list_color(), items)


def get_items_by_color_contains(color: str, items: list[ABCListColor]):
    return get_items_by_condition(lambda item: any([color in ci for ci in item.get_list_color()]), items)


def get_items_crimson(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_crimson(), items)


def get_items_sky_blue(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_sky_blue(), items)


def get_items_pink(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_pink(), items)


def get_items_orange(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_orange(), items)


def get_items_cobalt(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_cobalt(), items)


def get_items_burnt_sienna(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_burnt_sienna(), items)


def get_items_titanium_white(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_titanium_white(), items)


def get_items_grey(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_grey(), items)


def get_items_saffron(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_saffron(), items)


def get_items_lime(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_lime(), items)


def get_items_forest_green(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_forest_green(), items)


def get_items_black(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_black(), items)


def get_items_purple(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_purple(), items)
