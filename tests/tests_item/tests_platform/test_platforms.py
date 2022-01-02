import pytest

from rl_data_utils.item.platform.constants import *
from rl_data_utils.item.platform.platform import Platforms, Platform


platforms_data = Platforms.from_str_list(PLATFORMS)


@pytest.mark.parametrize('platform', [*PLATFORMS])
def test_has_platform(platform):
    assert platforms_data.has(Platform(platform))


@pytest.mark.parametrize('platform', [*PLATFORMS])
def test_get_respective_platform(platform):
    result = platforms_data.get_respective(Platform(platform))
    print(result)


@pytest.mark.parametrize('platforms', [PLATFORMS])
def test_are_valid_platforms_data(platforms):
    assert Platforms.from_str_list(platforms).is_valid()


@pytest.mark.parametrize('platforms', [PLATFORMS])
def test_has_pc(platforms):
    assert platforms_data.has(Platform(PC))


@pytest.mark.parametrize('platforms', [PLATFORMS])
def test_has_ps4(platforms):
    assert platforms_data.has(Platform(PS4))


@pytest.mark.parametrize('platforms', [PLATFORMS])
def test_has_xbox(platforms):
    assert platforms_data.has(Platform(XBOX))


@pytest.mark.parametrize('platforms', [PLATFORMS])
def test_has_switch(platforms):
    assert platforms_data.has(Platform(SWITCH))
