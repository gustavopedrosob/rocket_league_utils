from abc import ABC, abstractmethod


class ABCBaseType(ABC):
    @abstractmethod
    def is_valid_type(self):
        pass

    @abstractmethod
    def compare_types(self, type_: str) -> bool:
        pass

    @abstractmethod
    def get_respective_type(self) -> str:
        pass

    @abstractmethod
    def is_antenna(self) -> bool:
        pass

    @abstractmethod
    def is_avatar_border(self) -> bool:
        pass

    @abstractmethod
    def is_banner(self) -> bool:
        pass

    @abstractmethod
    def is_boost(self) -> bool:
        pass

    @abstractmethod
    def is_car(self) -> bool:
        pass

    @abstractmethod
    def is_decal(self) -> bool:
        pass

    @abstractmethod
    def is_engine_audio(self) -> bool:
        pass

    @abstractmethod
    def is_gift_pack(self) -> bool:
        pass

    @abstractmethod
    def is_goal_explosion(self) -> bool:
        pass

    @abstractmethod
    def is_paint_finish(self) -> bool:
        pass

    @abstractmethod
    def is_player_anthem(self):
        pass

    @abstractmethod
    def is_topper(self) -> bool:
        pass

    @abstractmethod
    def is_trail(self) -> bool:
        pass

    @abstractmethod
    def is_wheel(self) -> bool:
        pass

    @abstractmethod
    def validate_type(self):
        pass

    @abstractmethod
    def get_type(self):
        pass
