import pytest

from rl_data_utils.item.attribute.constants import ANTENNA, BORDER, CAR, DECAL, ENGINE_AUDIO, GOAL_EXPLOSION, \
    PAINT_FINISH, ANTHEM, BANNER, BOOST, TOPPER, TRAIL, WHEEL, BODY, ANIMATED_DECAL, PLAYER_ANTHEM, AVATAR_BORDER
from rl_data_utils.item.attribute_data.constants import SLOTS
from rl_data_utils.item.attribute.attribute import Slot

inventory_slots = ["Engine Audio", "Player Banner", "Body", "Topper", "Goal Explosion", "Wheels",
                   "Player Anthem", "Animated Decal", "Paint Finish", "Decal", "Avatar Border",
                   "Antenna", "Rocket Boost", "Trail"]

insider_slots = ["Wheels", "Cars", "Boosts", "Toppers", "Decals", "Antennas", "Goal Explosions", "Trails",
                 "Paint Finishes", "Banners", "Engine Audios", "Avatar Borders"]

samples = [*insider_slots, *inventory_slots, *SLOTS]

pair_equals = [["antennas", "Antennas"], ["avatar borders", "Avatar Borders"], ["body", "Body"],
               ["decals", "Decals"], ["engine audio", "Engine Audio"], ["goal explosions", "Goal Explosions"],
               ["paint finishes", "Paint Finishes"], ["player anthems", "Player Anthems"],
               ["player banners", "Player Banners"], ["rocket boosts", "Rocket Boosts"], ["toppers", "Toppers"],
               ["trails", "Trails"], ["wheels", "Wheels"]]


def test_from_random():
    print(Slot.create_random())


@pytest.mark.parametrize("slot_1,slot_2", pair_equals)
def test_compare_slot(slot_1, slot_2):
    assert Slot(slot_1).compare(Slot(slot_2))


@pytest.mark.parametrize("slot", ["Anthem"])
def test_is_anthem(slot):
    assert Slot(slot).is_exactly(ANTHEM)


@pytest.mark.parametrize("slot", ["Antenna"])
def test_is_antenna(slot):
    assert Slot(slot).is_exactly(ANTENNA)


@pytest.mark.parametrize("slot", ["Border"])
def test_is_border(slot):
    assert Slot(slot).is_exactly(BORDER)


@pytest.mark.parametrize("slot", ["Avatar Border"])
def test_is_avatar_border(slot):
    assert Slot(slot).is_exactly(AVATAR_BORDER)


@pytest.mark.parametrize("slot", ["Banner"])
def test_is_banner(slot):
    assert Slot(slot).is_exactly(BANNER)


@pytest.mark.parametrize("slot", ["Boost"])
def test_is_boost(slot):
    assert Slot(slot).is_exactly(BOOST)


@pytest.mark.parametrize("slot", ["Car"])
def test_is_car(slot):
    assert Slot(slot).is_exactly(CAR)


def test_is_body():
    assert Slot("Body").is_exactly(BODY, False)


@pytest.mark.parametrize("slot", ["Decal"])
def test_is_decal(slot):
    assert Slot(slot).is_exactly(DECAL)


def test_is_animated_decal():
    assert Slot("Animated decal").is_exactly(ANIMATED_DECAL, False)


@pytest.mark.parametrize("slot", ["Engine Audio"])
def test_is_engine_audio(slot):
    assert Slot(slot).is_exactly(ENGINE_AUDIO)


@pytest.mark.parametrize("slot", ["Goal Explosion"])
def test_is_goal_explosion(slot):
    assert Slot(slot).is_exactly(GOAL_EXPLOSION)


@pytest.mark.parametrize("slot", ["Paint Finish"])
def test_is_paint_finish(slot):
    assert Slot(slot).is_exactly(PAINT_FINISH)


@pytest.mark.parametrize("slot", ["Anthem"])
def test_is_anthem(slot):
    assert Slot(slot).is_exactly(PLAYER_ANTHEM)


@pytest.mark.parametrize("slot", ["Topper"])
def test_is_topper(slot):
    assert Slot(slot).is_exactly(TOPPER)


@pytest.mark.parametrize("slot", ["Trail"])
def test_is_trail(slot):
    assert Slot(slot).is_exactly(TRAIL)


@pytest.mark.parametrize("slot", ["Wheels"])
def test_is_wheel(slot):
    assert Slot(slot).is_exactly(WHEEL)
