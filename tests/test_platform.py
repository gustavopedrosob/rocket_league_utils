from rl_data_utils.exceptions import PlatformNotExists, PlatformIsNotInString, InvalidPlatformsList
from rl_data_utils.utils.item.platform.constants import PLATFORMS
from rl_data_utils.utils.item.platform.is_functions import is_pc, is_ps4, is_xbox, is_switch
from rl_data_utils.utils.item.platform.platform import compare_platforms, get_respective_platform, \
    get_platform_in_string, has_platform, validate_platforms_list, is_platform, validate_platform, all_are_platforms, \
    contains_platforms
from tests.utils.utils_attribute import validate, validate_list, is_, get_respective, get_in_string, has, contains, \
    compare, all_are

pair_equals = [['pc', 'Pc'], ['ps4', 'Ps4'], ['xbox', 'Xbox'], ['switch', 'Switch']]

samples = [PLATFORMS]


def test_all_are_platforms():
    all_are(all_are_platforms, samples)


def test_compare_platforms():
    compare(compare_platforms, pair_equals, PlatformNotExists)


def test_contains_platforms():
    contains(contains_platforms, samples)


def test_has_platform():
    has(has_platform, PLATFORMS, PlatformNotExists, InvalidPlatformsList)


def test_get_platform_in_string():
    get_in_string(get_platform_in_string, 'Pc Dingo Titanium White Striker', 'Pc', PlatformIsNotInString)


def test_get_respective_platform():
    get_respective(get_respective_platform, pair_equals, PlatformNotExists)


def test_is_platform():
    is_(is_platform, samples)


def test_validate_platforms_list():
    validate_list(validate_platforms_list, samples, InvalidPlatformsList)


def test_validate_platform():
    validate(validate_platform, samples, PlatformNotExists)


def test_is_pc():
    assert is_pc('pc')


def test_is_ps4():
    for ps4 in ['ps4', 'ps 4', 'play 4', 'playstation 4']:
        assert is_ps4(ps4)


def test_is_xbox():
    assert is_xbox('xbox')


def test_is_switch():
    assert is_switch('switch')
