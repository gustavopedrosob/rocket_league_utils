from abc import abstractmethod, ABC
from rl_data_utils.item.item.item_attribute import ItemAttribute
from rl_data_utils.utils.item.slot.is_functions import is_antenna, is_avatar_border, is_banner, is_boost, is_car, \
    is_decal, is_engine_audio, is_gift_pack, is_goal_explosion, is_paint_finish, is_player_anthem, is_topper, is_trail, \
    is_wheel, is_blueprint, is_player_title
from rl_data_utils.utils.item.slot.slot import compare_slot, get_respective_slot, validate_slot, is_slot


class ABCSlot(ABC, ItemAttribute):
    @abstractmethod
    def get_slot(self):
        pass

    def is_valid_slot(self):
        return is_slot(self.get_slot())

    def compare_slot(self, slot: str) -> bool:
        return compare_slot(self.get_slot(), slot)

    def get_respective_slot(self) -> str:
        return get_respective_slot(self.get_slot())

    def is_antenna(self) -> bool:
        return is_antenna(self.get_slot())

    def is_avatar_border(self) -> bool:
        return is_avatar_border(self.get_slot())

    def is_banner(self) -> bool:
        return is_banner(self.get_slot())

    def is_blueprint(self) -> bool:
        return is_blueprint(self.get_slot())

    def is_boost(self) -> bool:
        return is_boost(self.get_slot())

    def is_car(self) -> bool:
        return is_car(self.get_slot())

    def is_decal(self) -> bool:
        return is_decal(self.get_slot())

    def is_engine_audio(self) -> bool:
        return is_engine_audio(self.get_slot())

    def is_gift_pack(self) -> bool:
        return is_gift_pack(self.get_slot())

    def is_goal_explosion(self) -> bool:
        return is_goal_explosion(self.get_slot())

    def is_paint_finish(self) -> bool:
        return is_paint_finish(self.get_slot())

    def is_player_anthem(self):
        return is_player_anthem(self.get_slot())

    def is_player_title(self):
        return is_player_title(self.get_slot())

    def is_topper(self) -> bool:
        return is_topper(self.get_slot())

    def is_trail(self) -> bool:
        return is_trail(self.get_slot())

    def is_wheel(self) -> bool:
        return is_wheel(self.get_slot())

    def validate_slot(self):
        validate_slot(self.get_slot())


class Slot(ABCSlot):
    def __init__(self, slot: str):
        self.slot = slot

    def get_slot(self):
        return self.slot

    def set_type(self, slot: str):
        self.slot = slot
