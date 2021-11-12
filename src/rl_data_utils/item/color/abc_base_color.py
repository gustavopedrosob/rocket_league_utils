from abc import abstractmethod, ABC


class ABCBaseColor(ABC):
    @abstractmethod
    def is_valid_color(self):
        pass

    @abstractmethod
    def compare_colors(self, color) -> bool:
        pass

    @abstractmethod
    def get_hex_colors(self):
        pass

    @abstractmethod
    def get_respective_color(self):
        pass

    @abstractmethod
    def is_black(self) -> bool:
        pass

    @abstractmethod
    def is_burnt_sienna(self) -> bool:
        pass

    @abstractmethod
    def is_cobalt(self) -> bool:
        pass

    @abstractmethod
    def is_crimson(self) -> bool:
        pass

    @abstractmethod
    def is_default(self):
        pass

    @abstractmethod
    def is_forest_green(self) -> bool:
        pass

    @abstractmethod
    def is_grey(self) -> bool:
        pass

    @abstractmethod
    def is_lime(self) -> bool:
        pass

    @abstractmethod
    def is_orange(self) -> bool:
        pass

    @abstractmethod
    def is_pink(self) -> bool:
        pass

    @abstractmethod
    def is_purple(self) -> bool:
        pass

    @abstractmethod
    def is_saffron(self) -> bool:
        pass

    @abstractmethod
    def is_sky_blue(self) -> bool:
        pass

    @abstractmethod
    def is_titanium_white(self) -> bool:
        pass

    @abstractmethod
    def validate_color(self):
        pass

    @abstractmethod
    def get_color(self):
        pass
