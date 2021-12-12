import pytest

from rl_data_utils.item.platform.constants import *
from rl_data_utils.item.platform.platform import Platforms


@pytest.mark.parametrize('color', [*PLATFORMS])
def test_has_color(color):
    assert Platforms(PLATFORMS).has(color)


@pytest.mark.parametrize('color', [*PLATFORMS])
def test_get_respective_color(color):
    result = Platforms(PLATFORMS).get_respective(color)
    print(result)


@pytest.mark.parametrize('platforms', [PLATFORMS])
def test_validate_platforms(platforms):
    Platforms(platforms).validate()


@pytest.mark.parametrize('platforms', [PLATFORMS])
def test_are_valid_platforms(platforms):
    assert Platforms(platforms).is_valid()


@pytest.mark.parametrize('platforms', [PLATFORMS])
def test_has_pc(platforms):
    assert Platforms(platforms).has_exactly(PC)


@pytest.mark.parametrize('platforms', [PLATFORMS])
def test_has_ps4(platforms):
    assert Platforms(platforms).has_exactly(PS4)


@pytest.mark.parametrize('platforms', [PLATFORMS])
def test_has_xbox(platforms):
    assert Platforms(platforms).has_exactly(XBOX)


@pytest.mark.parametrize('platforms', [PLATFORMS])
def test_has_switch(platforms):
    assert Platforms(platforms).has_exactly(SWITCH)
