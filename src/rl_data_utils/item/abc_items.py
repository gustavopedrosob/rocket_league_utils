from abc import ABC, abstractmethod

from rl_data_utils.item.abc_item import get_items_by_condition, get_items_by, get_item_by, get_items_by_string, \
    get_item_by_string, get_names, get_types, get_rarities, get_colors, get_certificates, get_items_by_name, \
    get_items_by_certified, get_items_by_color, get_items_by_rarity, get_items_by_type, get_items_by_name_equal_to, \
    get_items_by_certified_equal_to, get_items_by_color_equal_to, get_items_by_rarity_equal_to, \
    get_items_by_type_equal_to, get_items_by_name_contains, get_items_by_certified_contains, \
    get_items_by_color_contains, get_items_by_rarity_contains, get_items_by_type_contains, get_items_crimson, \
    get_items_sky_blue, get_items_pink, get_items_orange, get_items_cobalt, get_items_burnt_sienna, \
    get_items_titanium_white, get_items_grey, get_items_saffron, get_items_lime, get_items_forest_green, \
    get_items_black, get_items_purple, get_items_aviator, get_items_acrobat, get_items_victor, get_items_striker, \
    get_items_sniper, get_items_scorer, get_items_playmaker, get_items_guardian, get_items_paragon, get_items_sweeper, \
    get_items_turtle, get_items_tactician, get_items_showoff, get_items_juggler, get_items_goalkeeper, \
    get_items_uncommon, get_items_rare, get_items_very_rare, get_items_import, get_items_exotic, get_items_limited, \
    get_items_antenna, get_items_avatar_border, get_items_banner, get_items_boost, get_items_car, get_items_decal, \
    get_items_engine_audio, get_items_gift_pack, get_items_goal_explosion, get_items_paint_finish, \
    get_items_player_anthem, get_items_topper, get_items_trail, get_items_wheel, ABCItem


class ABCItems(ABC):
    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def set_items(self, items: list[ABCItem]):
        pass

    def get_item_by(self, name: str, color: str = None, rarity: str = None, type_: str = None, certified: str = None):
        return get_item_by(self.get_items(), name, color, rarity, type_, certified)

    def get_items_by(self, name: str, color: str = None, rarity: str = None, type_: str = None, certified: str = None):
        return get_items_by(self.get_items(), name, color, rarity, type_, certified)

    def get_items_by_string(self, string: str):
        return get_items_by_string(self.get_items(), string)

    def get_item_by_string(self, string: str):
        return get_item_by_string(self.get_items(), string)

    def get_items_by_condition(self, lamb):
        return get_items_by_condition(lamb, self.get_items())

    def get_items_by_name(self, name: str):
        return get_items_by_name(name, self.get_items())

    def get_items_by_certified(self, certified: str):
        return get_items_by_certified(certified, self.get_items())

    def get_items_by_color(self, color: str):
        return get_items_by_color(color, self.get_items())

    def get_items_by_rarity(self, rarity: str):
        return get_items_by_rarity(rarity, self.get_items())

    def get_items_by_type(self, type_: str):
        return get_items_by_type(type_, self.get_items())

    def get_items_by_name_equal_to(self, name: str):
        return get_items_by_name_equal_to(name, self.get_items())

    def get_items_by_certified_equal_to(self, certified: str):
        return get_items_by_certified_equal_to(certified, self.get_items())

    def get_items_by_color_equal_to(self, color: str):
        return get_items_by_color_equal_to(color, self.get_items())

    def get_items_by_rarity_equal_to(self, rarity: str):
        return get_items_by_rarity_equal_to(rarity, self.get_items())

    def get_items_by_type_equal_to(self, type_: str):
        return get_items_by_type_equal_to(type_, self.get_items())

    def get_items_by_name_contains(self, name: str):
        return get_items_by_name_contains(name, self.get_items())

    def get_items_by_certified_contains(self, certified: str):
        return get_items_by_certified_contains(certified, self.get_items())

    def get_items_by_color_contains(self, color: str):
        return get_items_by_color_contains(color, self.get_items())

    def get_items_by_rarity_contains(self, rarity: str):
        return get_items_by_rarity_contains(rarity, self.get_items())

    def get_items_by_type_contains(self, type_: str):
        return get_items_by_type_contains(type_, self.get_items())

    def get_names(self):
        return get_names(self.get_items())

    def get_types(self):
        return get_types(self.get_items())

    def get_rarities(self):
        return get_rarities(self.get_items())

    def get_colors(self):
        return get_colors(self.get_items())

    def get_certificates(self):
        return get_certificates(self.get_items())

    def get_items_crimson(self):
        return get_items_crimson(self.get_items())

    def get_items_sky_blue(self):
        return get_items_sky_blue(self.get_items())

    def get_items_pink(self):
        return get_items_pink(self.get_items())

    def get_items_orange(self):
        return get_items_orange(self.get_items())

    def get_items_cobalt(self):
        return get_items_cobalt(self.get_items())

    def get_items_burnt_sienna(self):
        return get_items_burnt_sienna(self.get_items())

    def get_items_titanium_white(self):
        return get_items_titanium_white(self.get_items())

    def get_items_grey(self):
        return get_items_grey(self.get_items())

    def get_items_saffron(self):
        return get_items_saffron(self.get_items())

    def get_items_lime(self):
        return get_items_lime(self.get_items())

    def get_items_forest_green(self):
        return get_items_forest_green(self.get_items())

    def get_items_black(self):
        return get_items_black(self.get_items())

    def get_items_purple(self):
        return get_items_purple(self.get_items())

    def get_items_aviator(self):
        return get_items_aviator(self.get_items())

    def get_items_acrobat(self):
        return get_items_acrobat(self.get_items())

    def get_items_victor(self):
        return get_items_victor(self.get_items())

    def get_items_striker(self):
        return get_items_striker(self.get_items())

    def get_items_sniper(self):
        return get_items_sniper(self.get_items())

    def get_items_scorer(self):
        return get_items_scorer(self.get_items())

    def get_items_playmaker(self):
        return get_items_playmaker(self.get_items())

    def get_items_guardian(self):
        return get_items_guardian(self.get_items())

    def get_items_paragon(self):
        return get_items_paragon(self.get_items())

    def get_items_sweeper(self):
        return get_items_sweeper(self.get_items())

    def get_items_turtle(self):
        return get_items_turtle(self.get_items())

    def get_items_tactician(self):
        return get_items_tactician(self.get_items())

    def get_items_showoff(self):
        return get_items_showoff(self.get_items())

    def get_items_juggler(self):
        return get_items_juggler(self.get_items())

    def get_items_goalkeeper(self):
        return get_items_goalkeeper(self.get_items())

    def get_items_uncommon(self):
        return get_items_uncommon(self.get_items())

    def get_items_rare(self):
        return get_items_rare(self.get_items())

    def get_items_very_rare(self):
        return get_items_very_rare(self.get_items())

    def get_items_import(self):
        return get_items_import(self.get_items())

    def get_items_exotic(self):
        return get_items_exotic(self.get_items())

    def get_items_black_market(self):
        return get_items_black(self.get_items())

    def get_items_limited(self):
        return get_items_limited(self.get_items())

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
