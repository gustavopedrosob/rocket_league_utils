from abc import ABC, abstractmethod
from re import IGNORECASE


class ABCBaseColors(ABC):
    @abstractmethod
    def get_items_by_color_regex(self, color_pattern: str, flags=IGNORECASE):
        pass

    @abstractmethod
    def get_items_by_color(self, color: str, items=None):
        pass

    @abstractmethod
    def get_items_by_color_equal_to(self, color: str):
        pass

    @abstractmethod
    def get_items_by_color_contains(self, color: str):
        pass

    @abstractmethod
    def get_colors(self):
        pass

    @abstractmethod
    def get_items_crimson(self):
        pass

    @abstractmethod
    def get_items_sky_blue(self):
        pass

    @abstractmethod
    def get_items_pink(self):
        pass

    @abstractmethod
    def get_items_orange(self):
        pass

    @abstractmethod
    def get_items_cobalt(self):
        pass

    @abstractmethod
    def get_items_burnt_sienna(self):
        pass

    @abstractmethod
    def get_items_titanium_white(self):
        pass

    @abstractmethod
    def get_items_grey(self):
        pass

    @abstractmethod
    def get_items_saffron(self):
        pass

    @abstractmethod
    def get_items_lime(self):
        pass

    @abstractmethod
    def get_items_forest_green(self):
        pass

    @abstractmethod
    def get_items_black(self):
        pass

    @abstractmethod
    def get_items_purple(self):
        pass
