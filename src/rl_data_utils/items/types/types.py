from rl_data_utils.items.items.items import Items
from re import IGNORECASE
from rl_data_utils.items.types.abc_base_types import ABCBaseTypes
from rl_data_utils.utils.items.types.types import get_items_by_type_regex, get_types, get_items_by_type, \
    get_items_by_type_equal_to, get_items_by_type_contains, get_items_antenna, get_items_avatar_border, \
    get_items_banner, get_items_boost, get_items_car, get_items_decal, get_items_engine_audio, get_items_gift_pack, \
    get_items_goal_explosion, get_items_paint_finish, get_items_player_anthem, get_items_topper, get_items_trail, \
    get_items_wheel, get_items_player_title, get_items_blueprint


class Types(ABCBaseTypes, Items):
    def get_items_by_type_regex(self, type_pattern: str, flags=IGNORECASE):
        return self.__class__(get_items_by_type_regex(type_pattern, self.items, flags))

    def get_items_by_type(self, type_: str):
        return self.__class__(get_items_by_type(type_, self.items))

    def get_items_by_type_equal_to(self, type_: str):
        return self.__class__(get_items_by_type_equal_to(type_, self.items))

    def get_items_by_type_contains(self, type_: str):
        return self.__class__(get_items_by_type_contains(type_, self.items))

    def get_types(self):
        return get_types(self.items)

    def get_items_antenna(self) -> bool:
        return self.__class__(get_items_antenna(self.items))

    def get_items_avatar_border(self) -> bool:
        return self.__class__(get_items_avatar_border(self.items))

    def get_items_banner(self) -> bool:
        return self.__class__(get_items_banner(self.items))

    def get_items_blueprint(self) -> bool:
        return self.__class__(get_items_blueprint(self.items))

    def get_items_boost(self) -> bool:
        return self.__class__(get_items_boost(self.items))

    def get_items_car(self) -> bool:
        return self.__class__(get_items_car(self.items))

    def get_items_decal(self) -> bool:
        return self.__class__(get_items_decal(self.items))

    def get_items_engine_audio(self) -> bool:
        return self.__class__(get_items_engine_audio(self.items))

    def get_items_gift_pack(self) -> bool:
        return self.__class__(get_items_gift_pack(self.items))

    def get_items_goal_explosion(self) -> bool:
        return self.__class__(get_items_goal_explosion(self.items))

    def get_items_paint_finish(self) -> bool:
        return self.__class__(get_items_paint_finish(self.items))

    def get_items_player_anthem(self) -> bool:
        return self.__class__(get_items_player_anthem(self.items))

    def get_items_player_title(self) -> bool:
        return self.__class__(get_items_player_title(self.items))

    def get_items_topper(self) -> bool:
        return self.__class__(get_items_topper(self.items))

    def get_items_trail(self) -> bool:
        return self.__class__(get_items_trail(self.items))

    def get_items_wheel(self) -> bool:
        return self.__class__(get_items_wheel(self.items))
