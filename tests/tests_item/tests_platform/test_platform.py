import pytest

from rl_data_utils.item.attribute.constants import PC, PS4, SWITCH, XBOX, PLAY_4, PLAYSTATION_4, COMPUTER, STEAM, \
    EPIC_GAMES, EPIC
from rl_data_utils.item.attribute.attribute import Platform

pair_equals = [["pc", "Pc"], ["ps4", "Ps4"], ["xbox", "Xbox"], ["switch", "Switch"]]


def test_from_random():
    print(Platform.create_random())


@pytest.mark.parametrize("platform_1,platform_2", pair_equals)
def test_compare_platform(platform_1, platform_2):
    assert Platform(platform_1).compare(Platform(platform_2))


@pytest.mark.parametrize("platform", ["pc", "computer", "steam", "epic games", "epic"])
def test_is_pc(platform):
    assert Platform(platform).is_exactly(PC)


def test_is_computer():
    assert Platform("computer").is_exactly(COMPUTER, False)


def test_is_steam():
    assert Platform("steam").is_exactly(STEAM, False)


def test_is_epic_games():
    assert Platform("epic games").is_exactly(EPIC_GAMES, False)


def test_is_epic():
    assert Platform("epic").is_exactly(EPIC, False)


@pytest.mark.parametrize("platform", ["ps4", "ps 4", "play 4", "playstation 4"])
def test_is_ps4(platform):
    assert Platform(platform).is_exactly(PS4)


def test_is_play_4():
    assert Platform("Play4").is_exactly(PLAY_4, False)


def test_is_playstation_4():
    assert Platform("Playstation_4").is_exactly(PLAYSTATION_4, False)


@pytest.mark.parametrize("platform", ["xbox"])
def test_is_xbox(platform):
    assert Platform(platform).is_exactly(XBOX)


@pytest.mark.parametrize("platform", ["switch"])
def test_is_switch(platform):
    assert Platform(platform).is_exactly(SWITCH)
