from abc import abstractmethod
from rl_data_utils.item.item.item_data import ItemDataAttribute
from rl_data_utils.utils.item.color.color import has_color, get_respective_color, all_are_colors, validate_color_list
from rl_data_utils.utils.item.color.has_functions import has_black, has_burnt_sienna, has_cobalt, has_crimson, \
    has_default, has_forest_green, has_grey, has_lime, has_orange, has_pink, has_purple, has_saffron, has_sky_blue, \
    has_titanium_white
from rl_data_utils.exceptions import ItemHaveNotColor


class ABCListColor(ItemDataAttribute):
    @abstractmethod
    def get_list_color(self) -> list[str]:
        pass

    def contains_color(self, color: str):
        return has_color(color, self.get_list_color())

    def validate_contains_color(self, color: str):
        if not self.contains_color(color):
            raise ItemHaveNotColor(color)

    def is_valid_color_list(self):
        return all_are_colors(self.get_list_color())

    def validate_color_list(self):
        validate_color_list(self.get_list_color())

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
