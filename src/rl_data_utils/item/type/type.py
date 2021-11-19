from abc import abstractmethod, ABC
from rl_data_utils.item.item.item_attribute import ItemAttribute
from rl_data_utils.utils.item.type.is_functions import is_antenna, is_avatar_border, is_banner, is_boost, is_car, \
    is_decal, is_engine_audio, is_gift_pack, is_goal_explosion, is_paint_finish, is_player_anthem, is_topper, is_trail, \
    is_wheel, is_blueprint, is_player_title
from rl_data_utils.utils.item.type.type import compare_type, get_respective_type, validate_type, is_type


class ABCType(ABC, ItemAttribute):
    @abstractmethod
    def get_type(self):
        pass

    def is_valid_type(self):
        return is_type(self.get_type())

    def compare_type(self, type_: str) -> bool:
        return compare_type(self.get_type(), type_)

    def get_respective_type(self) -> str:
        return get_respective_type(self.get_type())

    def is_antenna(self) -> bool:
        return is_antenna(self.get_type())

    def is_avatar_border(self) -> bool:
        return is_avatar_border(self.get_type())

    def is_banner(self) -> bool:
        return is_banner(self.get_type())

    def is_blueprint(self) -> bool:
        return is_blueprint(self.get_type())

    def is_boost(self) -> bool:
        return is_boost(self.get_type())

    def is_car(self) -> bool:
        return is_car(self.get_type())

    def is_decal(self) -> bool:
        return is_decal(self.get_type())

    def is_engine_audio(self) -> bool:
        return is_engine_audio(self.get_type())

    def is_gift_pack(self) -> bool:
        return is_gift_pack(self.get_type())

    def is_goal_explosion(self) -> bool:
        return is_goal_explosion(self.get_type())

    def is_paint_finish(self) -> bool:
        return is_paint_finish(self.get_type())

    def is_player_anthem(self):
        return is_player_anthem(self.get_type())

    def is_player_title(self):
        return is_player_title(self.get_type())

    def is_topper(self) -> bool:
        return is_topper(self.get_type())

    def is_trail(self) -> bool:
        return is_trail(self.get_type())

    def is_wheel(self) -> bool:
        return is_wheel(self.get_type())

    def validate_type(self):
        validate_type(self.get_type())


class Type(ABCType):
    def __init__(self, type_: str):
        self.type = type_

    def get_type(self):
        return self.type

    def set_type(self, type_: str):
        self.type = type_
