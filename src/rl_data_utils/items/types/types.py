from rl_data_utils.items.items.items import ABCItems
from re import IGNORECASE
from rl_data_utils.items.types.abc_base_types import ABCBaseTypes
from rl_data_utils.utils.items.types.types import get_items_by_type_regex, get_types, get_items_by_type, \
    get_items_by_type_equal_to, get_items_by_type_contains, get_items_antenna, get_items_avatar_border, \
    get_items_banner, get_items_boost, get_items_car, get_items_decal, get_items_engine_audio, get_items_gift_pack, \
    get_items_goal_explosion, get_items_paint_finish, get_items_player_anthem, get_items_topper, get_items_trail, \
    get_items_wheel


class ABCTypes(ABCBaseTypes, ABCItems):
    def get_items_by_type_regex(self, type_pattern: str, flags=IGNORECASE):
        return get_items_by_type_regex(type_pattern, self.get_items(), flags)

    def get_items_by_type(self, type_: str, items=None):
        if items is None:
            items = self.get_items()
        return get_items_by_type(type_, items)

    def get_items_by_type_equal_to(self, type_: str):
        return get_items_by_type_equal_to(type_, self.get_items())

    def get_items_by_type_contains(self, type_: str):
        return get_items_by_type_contains(type_, self.get_items())

    def get_types(self):
        return get_types(self.get_items())

    def get_items_antenna(self) -> bool:
        return get_items_antenna(self.get_items())

    def get_items_avatar_border(self) -> bool:
        return get_items_avatar_border(self.get_items())

    def get_items_banner(self) -> bool:
        return get_items_banner(self.get_items())

    def get_items_boost(self) -> bool:
        return get_items_boost(self.get_items())

    def get_items_car(self) -> bool:
        return get_items_car(self.get_items())

    def get_items_decal(self) -> bool:
        return get_items_decal(self.get_items())

    def get_items_engine_audio(self) -> bool:
        return get_items_engine_audio(self.get_items())

    def get_items_gift_pack(self) -> bool:
        return get_items_gift_pack(self.get_items())

    def get_items_goal_explosion(self) -> bool:
        return get_items_goal_explosion(self.get_items())

    def get_items_paint_finish(self) -> bool:
        return get_items_paint_finish(self.get_items())

    def get_items_player_anthem(self):
        return get_items_player_anthem(self.get_items())

    def get_items_topper(self) -> bool:
        return get_items_topper(self.get_items())

    def get_items_trail(self) -> bool:
        return get_items_trail(self.get_items())

    def get_items_wheel(self) -> bool:
        return get_items_wheel(self.get_items())
