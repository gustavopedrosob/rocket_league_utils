from rl_data_utils.exceptions import TypeNotExists, InvalidTypesList, TypeIsNotInString
from rl_data_utils.utils.item.type.contains import contains_antenna, contains_avatar_border, contains_banner, \
    contains_boost, contains_car, contains_decal, contains_engine_audio, contains_gift_pack, contains_goal_explosion, \
    contains_player_anthem, contains_topper, contains_trail, contains_wheel, contains_paint_finish
from rl_data_utils.utils.item.type.is_functions import is_antenna, is_avatar_border, is_banner, is_boost, is_car, \
    is_decal, is_engine_audio, is_gift_pack, is_goal_explosion, is_paint_finish, is_player_anthem, is_topper, is_trail, \
    is_wheel
from rl_data_utils.utils.item.type.type import all_are_types, compare_type, contains_types, has_type, \
    get_type_in_string, get_respective_type, is_type, validate_types_list, validate_type
from rl_data_utils.utils.item.type.constants import TYPES
from tests.utils.utils_attribute import all_are, compare, contains, has, get_in_string, get_respective, is_, \
    validate_list, validate

inventory_types = ['Engine Audio', 'Player Banner', 'Body', 'Topper', 'Goal Explosion', 'Wheels',
                   'Player Anthem', 'Animated Decal', 'Paint Finish', 'Blueprint', 'Decal', 'Avatar Border',
                   'Antenna', 'Rocket Boost', 'Player Title', 'Trail']

insider_types = ['Wheels', 'Cars', 'Boosts', 'Toppers', 'Decals', 'Antennas', 'Goal Explosions', 'Trails',
                 'Gift Packs', 'Paint Finishes', 'Banners', 'Engine Audios', 'Avatar Borders']

samples = [insider_types, inventory_types, TYPES]

pair_equals = [['antennas', 'Antennas'], ['avatar borders', 'Avatar Borders'], ['bodies', 'Bodies'],
               ['decals', 'Decals'], ['engine audio', 'Engine Audio'], ['goal explosions', 'Goal Explosions'],
               ['paint finishes', 'Paint Finishes'], ['player anthems', 'Player Anthems'],
               ['player banners', 'Player Banners'], ['rocket boosts', 'Rocket Boosts'], ['toppers', 'Toppers'],
               ['trails', 'Trails'], ['wheels', 'Wheels']]


def test_all_are_types():
    all_are(all_are_types, samples)


def test_compare_types():
    compare(compare_type, pair_equals, TypeNotExists)


def test_contains_types():
    contains(contains_types, samples)


def test_has_type():
    has(has_type, inventory_types, TypeNotExists, InvalidTypesList)


def test_get_type_in_string():
    get_in_string(get_type_in_string, 'Dingo Titanium White Striker Body', 'Body', TypeIsNotInString)


def test_get_respective_type():
    get_respective(get_respective_type, pair_equals, TypeNotExists)


def test_is_type():
    is_(is_type, samples)


def test_validate_types_list():
    validate_list(validate_types_list, samples, InvalidTypesList)


def test_validate_type():
    validate(validate_type, samples, TypeNotExists)


def test_is_antenna():
    assert is_antenna('antenna')
    assert is_antenna('antennas')


def test_is_avatar_border():
    assert is_avatar_border('avatar border')


def test_is_banner():
    assert is_banner('banner')


def test_is_boost():
    assert is_boost('boost')
    assert is_boost('boosts')


def test_is_car():
    assert is_car('car')
    assert is_car('cars')
    assert is_car('bodies')
    assert is_car('body')


def test_is_decal():
    assert is_decal('decal')


def test_is_engine_audio():
    assert is_engine_audio('engine audio')


def test_is_gift_pack():
    assert is_gift_pack('gift pack')


def test_is_goal_explosion():
    assert is_goal_explosion('goal explosion')


def test_is_paint_finish():
    assert is_paint_finish('paint finish')
    assert is_paint_finish('paint finishes')


def test_is_player_anthem():
    assert is_player_anthem('player anthem')


def test_is_topper():
    assert is_topper('topper')
    assert is_topper('toppers')
    assert is_topper('hat')
    assert is_topper('hats')


def test_is_trail():
    assert is_trail('trail')


def test_is_wheel():
    assert is_wheel('wheel')


def test_contains_antenna():
    assert contains_antenna('antenna')
    assert contains_antenna('antennas')


def test_contains_avatar_border():
    assert contains_avatar_border('avatar border')


def test_contains_banner():
    assert contains_banner('banner')


def test_contains_boost():
    assert contains_boost('boost')
    assert contains_boost('boosts')


def test_contains_car():
    assert contains_car('car')
    assert contains_car('cars')
    assert contains_car('bodies')
    assert contains_car('body')


def test_contains_decal():
    assert contains_decal('decal')


def test_contains_engine_audio():
    assert contains_engine_audio('engine audio')


def test_contains_gift_pack():
    assert contains_gift_pack('gift pack')


def test_contains_goal_explosion():
    assert contains_goal_explosion('goal explosion')


def test_contains_paint_finish():
    assert contains_paint_finish('paint finish')
    assert contains_paint_finish('paint finishes')


def test_contains_player_anthem():
    assert contains_player_anthem('player anthem')


def test_contains_topper():
    assert contains_topper('topper')
    assert contains_topper('toppers')
    assert contains_topper('hat')
    assert contains_topper('hats')


def test_contains_trail():
    assert contains_trail('trail')


def test_contains_wheel():
    assert contains_wheel('wheel')
