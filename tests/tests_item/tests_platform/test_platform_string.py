import pytest

from rl_data_utils.item.platform.constants import *
from rl_data_utils.item.platform.platform import PlatformString


@pytest.mark.parametrize('platform', ['pc'])
def test_contains_pc(platform):
    assert PlatformString(platform).get_exactly(PC)


@pytest.mark.parametrize('platform', ['ps4', 'ps 4', 'play 4', 'playstation 4'])
def test_contains_ps4(platform):
    assert PlatformString(platform).get_exactly(PS4)


@pytest.mark.parametrize('platform', ['xbox'])
def test_contains_xbox(platform):
    assert PlatformString(platform).get_exactly(XBOX)


@pytest.mark.parametrize('platform', ['switch'])
def test_contains_switch(platform):
    assert PlatformString(platform).get_exactly(SWITCH)
