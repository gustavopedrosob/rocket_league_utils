import pytest

from rl_data_utils.item.attribute.constants import PC, PS4, SWITCH, XBOX
from rl_data_utils.item.attribute_data.constants import PLATFORMS
from rl_data_utils.item.attribute.attribute import Platform
from rl_data_utils.item.attribute_data.attribute_data import Platforms

platforms_data = Platforms(PLATFORMS)


@pytest.mark.parametrize("platform", [*PLATFORMS])
def test_has_platform(platform):
    assert platforms_data.has(platform)


@pytest.mark.parametrize("platform", [*PLATFORMS])
def test_get_respective_platform(platform):
    result = platforms_data.get_respective(platform)
    print(result)


@pytest.mark.parametrize("platforms", [PLATFORMS])
def test_has_pc(platforms):
    assert platforms_data.has(PC)


@pytest.mark.parametrize("platforms", [PLATFORMS])
def test_has_ps4(platforms):
    assert platforms_data.has(PS4)


@pytest.mark.parametrize("platforms", [PLATFORMS])
def test_has_xbox(platforms):
    assert platforms_data.has(XBOX)


@pytest.mark.parametrize("platforms", [PLATFORMS])
def test_has_switch(platforms):
    assert platforms_data.has(SWITCH)
