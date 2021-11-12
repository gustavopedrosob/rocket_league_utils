from abc import ABC, abstractmethod
from re import IGNORECASE


class ABCBaseTypes(ABC):
    @abstractmethod
    def get_items_with_valid_type(self):
        pass

    @abstractmethod
    def get_items_by_type_regex(self, type_pattern: str, flags=IGNORECASE):
        pass

    @abstractmethod
    def get_items_by_type(self, type_: str):
        pass

    @abstractmethod
    def get_items_by_type_equal_to(self, type_: str):
        pass

    @abstractmethod
    def get_items_by_type_contains(self, type_: str):
        pass

    @abstractmethod
    def get_types(self):
        pass

    @abstractmethod
    def get_items_antenna(self) -> bool:
        pass

    @abstractmethod
    def get_items_avatar_border(self) -> bool:
        pass

    @abstractmethod
    def get_items_banner(self) -> bool:
        pass

    @abstractmethod
    def get_items_blueprint(self) -> bool:
        pass

    @abstractmethod
    def get_items_boost(self) -> bool:
        pass

    @abstractmethod
    def get_items_car(self) -> bool:
        pass

    @abstractmethod
    def get_items_decal(self) -> bool:
        pass

    @abstractmethod
    def get_items_engine_audio(self) -> bool:
        pass

    @abstractmethod
    def get_items_gift_pack(self) -> bool:
        pass

    @abstractmethod
    def get_items_goal_explosion(self) -> bool:
        pass

    @abstractmethod
    def get_items_paint_finish(self) -> bool:
        pass

    @abstractmethod
    def get_items_player_anthem(self) -> bool:
        pass

    @abstractmethod
    def get_items_player_title(self) -> bool:
        pass

    @abstractmethod
    def get_items_topper(self) -> bool:
        pass

    @abstractmethod
    def get_items_trail(self) -> bool:
        pass

    @abstractmethod
    def get_items_wheel(self) -> bool:
        pass
