from rl_data_utils.colors.colors import ABCColor
from rl_data_utils.item.utils import get_attributes_in_string
from rl_data_utils.types.types import ABCType
from rl_data_utils.rarities.rarities import ABCRarity
from rl_data_utils.certificates.certificates import ABCCertified
from rl_data_utils.names.names import ABCName
from rl_data_utils.item.utils import validate_attributes


class ABCItem(ABCName, ABCColor, ABCType, ABCRarity, ABCCertified):
    def validate(self):
        validate_attributes(self.get_color(), self.get_type(), self.get_rarity(), self.get_certified())

    def __eq__(self, other):
        if isinstance(other, ABCItem):
            return compare_items(self, other)
        else:
            return False


def get_items_by_condition(lamb, items: list[ABCItem]):
    return list(filter(lamb, items))


def compare_items(item_1, item_2):
    from rl_data_utils.certificates.certificates import compare_certificates
    from rl_data_utils.colors.colors import compare_colors
    from rl_data_utils.names.names import compare_names
    from rl_data_utils.rarities.rarities import compare_rarities
    from rl_data_utils.types.types import compare_types
    for get_function, function in [(ABCItem.get_certified, compare_certificates), (ABCItem.get_color, compare_colors),
                                   (ABCItem.get_name, compare_names), (ABCItem.get_rarity, compare_rarities),
                                   (ABCItem.get_type, compare_types)]:
        item_1_value = get_function(item_1)
        item_2_value = get_function(item_2)
        if item_1_value and item_2_value:
            if not function(item_1_value, item_2_value):
                return False
    return True


def get_items_by(items: list[ABCItem], name: str, color: str = None, rarity: str = None, type_: str = None,
                 certified: str = None):
    if rarity:
        items = get_items_by_rarity(rarity, items)
    if type_:
        items = get_items_by_type(type_, items)
    if certified:
        items = get_items_by_certified(certified, items)
    if color:
        items = get_items_by_color(color, items)
    return get_items_by_name(name, items)


def get_item_by(items: list[ABCItem], name: str, color: str = None, rarity: str = None, type_: str = None,
                certified: str = None):
    return get_items_by(items, name, color, rarity, type_, certified)[0]


def get_items_by_string(items: list[ABCItem], string: str):
    kwargs = get_attributes_in_string(string)
    return get_items_by(items, **kwargs)


def get_item_by_string(items: list[ABCItem], string: str):
    return get_items_by_string(items, string)[0]


def get_names(items: list[ABCItem]):
    return {item.get_name() for item in items}


def get_types(items: list[ABCItem]):
    return {item.get_type() for item in items}


def get_rarities(items: list[ABCItem]):
    return {item.get_rarity() for item in items}


def get_colors(items: list[ABCItem]):
    return {item.get_color() for item in items}


def get_certificates(items: list[ABCItem]):
    return {item.get_certified() for item in items}


def get_items_by_name(name: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.compare_name(name), items)


def get_items_by_certified(certified: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.compare_certificates(certified), items)


def get_items_by_color(color: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.compare_colors(color), items)


def get_items_by_rarity(rarity: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.compare_rarities(rarity), items)


def get_items_by_type(type_: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.compare_types(type_), items)


def get_items_by_name_equal_to(name: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.get_name() == name, items)


def get_items_by_certified_equal_to(certified: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.get_certified() == certified, items)


def get_items_by_color_equal_to(color: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.get_color() == color, items)


def get_items_by_rarity_equal_to(rarity: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.get_rarity() == rarity, items)


def get_items_by_type_equal_to(type_: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.get_type() == type_, items)


def get_items_by_name_contains(name: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: name in item.get_name(), items)


def get_items_by_certified_contains(certified: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: certified in item.get_certified(), items)


def get_items_by_color_contains(color: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: color in item.get_color(), items)


def get_items_by_rarity_contains(rarity: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: rarity in item.get_rarity(), items)


def get_items_by_type_contains(type_: str, items: list[ABCItem]):
    return get_items_by_condition(lambda item: type_ in item.get_type(), items)


def get_items_crimson(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_crimson(), items)


def get_items_sky_blue(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_sky_blue(), items)


def get_items_pink(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_pink(), items)


def get_items_orange(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_orange(), items)


def get_items_cobalt(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_cobalt(), items)


def get_items_burnt_sienna(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_burnt_sienna(), items)


def get_items_titanium_white(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_titanium_white(), items)


def get_items_grey(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_grey(), items)


def get_items_saffron(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_saffron(), items)


def get_items_lime(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_lime(), items)


def get_items_forest_green(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_forest_green(), items)


def get_items_black(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_black(), items)


def get_items_purple(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_purple(), items)


def get_items_aviator(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_aviator(), items)


def get_items_acrobat(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_acrobat(), items)


def get_items_victor(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_victor(), items)


def get_items_striker(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_striker(), items)


def get_items_sniper(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_sniper(), items)


def get_items_scorer(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_scorer(), items)


def get_items_playmaker(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_playmaker(), items)


def get_items_guardian(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_guardian(), items)


def get_items_paragon(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_paragon(), items)


def get_items_sweeper(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_sweeper(), items)


def get_items_turtle(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_turtle(), items)


def get_items_tactician(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_tactician(), items)


def get_items_showoff(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_show_off(), items)


def get_items_juggler(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_juggler(), items)


def get_items_goalkeeper(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_goalkeeper(), items)


def get_items_uncommon(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_uncommon(), items)


def get_items_rare(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_rare(), items)


def get_items_very_rare(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_very_rare(), items)


def get_items_import(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_import(), items)


def get_items_exotic(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_exotic(), items)


def get_items_black_market(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_black_market(), items)


def get_items_limited(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_limited(), items)


def get_items_antenna(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_antenna(), items)


def get_items_avatar_border(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_avatar_border(), items)


def get_items_banner(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_banner(), items)


def get_items_boost(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_boost(), items)


def get_items_car(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_car(), items)


def get_items_decal(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_decal(), items)


def get_items_engine_audio(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_engine_audio(), items)


def get_items_gift_pack(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_gift_pack(), items)


def get_items_goal_explosion(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_goal_explosion(), items)


def get_items_paint_finish(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_paint_finish(), items)


def get_items_player_anthem(items: list[ABCItem]):
    return get_items_by_condition(lambda item: item.is_player_anthem(), items)


def get_items_topper(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_topper(), items)


def get_items_trail(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_trail(), items)


def get_items_wheel(items: list[ABCItem]) -> bool:
    return get_items_by_condition(lambda item: item.is_wheel(), items)