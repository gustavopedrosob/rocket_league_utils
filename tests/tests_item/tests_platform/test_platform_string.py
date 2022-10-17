import pytest

from rl_data_utils.item.attribute.constants import PC, PS4, SWITCH, XBOX
from rl_data_utils.item.attribute.attribute import Platform


@pytest.mark.parametrize("platform", ["pc"])
def test_contains_pc(platform):
    assert Platform.from_text(platform, PC)


@pytest.mark.parametrize("platform", ["ps4", "ps 4", "play 4", "playstation 4"])
def test_contains_ps4(platform):
    assert Platform.from_text(platform, PS4)


@pytest.mark.parametrize("platform", ["xbox"])
def test_contains_xbox(platform):
    assert Platform.from_text(platform, XBOX)


@pytest.mark.parametrize("platform", ["switch"])
def test_contains_switch(platform):
    assert Platform.from_text(platform, SWITCH)
