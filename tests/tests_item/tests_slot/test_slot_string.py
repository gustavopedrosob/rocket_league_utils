import pytest

from rl_data_utils.item.attribute.constants import ANTENNA, BORDER, CAR, DECAL, ENGINE_AUDIO, GOAL_EXPLOSION,\
    GIFT_PACK, PAINT_FINISH, ANTHEM, BANNER, BOOST, TOPPER, TRAIL, WHEEL
from rl_data_utils.item.attribute.attribute import Slot


@pytest.mark.parametrize("slot", ["Antenna"])
def test_contains_antenna(slot):
    assert Slot.from_text(slot, ANTENNA)


@pytest.mark.parametrize("slot", ["Avatar Border"])
def test_contains_border(slot):
    assert Slot.from_text(slot, BORDER)


@pytest.mark.parametrize("slot", ["Banner"])
def test_contains_banner(slot):
    assert Slot.from_text(slot, BANNER)


@pytest.mark.parametrize("slot", ["Boost"])
def test_contains_boost(slot):
    assert Slot.from_text(slot, BOOST)


@pytest.mark.parametrize("slot", ["Car"])
def test_contains_car(slot):
    assert Slot.from_text(slot, CAR)


@pytest.mark.parametrize("slot", ["Decal"])
def test_contains_decal(slot):
    assert Slot.from_text(slot, DECAL)


@pytest.mark.parametrize("slot", ["Engine Audio"])
def test_contains_engine_audio(slot):
    assert Slot.from_text(slot, ENGINE_AUDIO)


@pytest.mark.parametrize("slot", ["Gift Pack"])
def test_contains_gift_pack(slot):
    assert Slot.from_text(slot, GIFT_PACK)


@pytest.mark.parametrize("slot", ["Goal Explosion"])
def test_contains_goal_explosion(slot):
    assert Slot.from_text(slot, GOAL_EXPLOSION)


@pytest.mark.parametrize("slot", ["Paint Finish"])
def test_contains_paint_finish(slot):
    assert Slot.from_text(slot, PAINT_FINISH)


@pytest.mark.parametrize("slot", ["Anthem"])
def test_contains_anthem(slot):
    assert Slot.from_text(slot, ANTHEM)


@pytest.mark.parametrize("slot", ["Topper"])
def test_contains_topper(slot):
    assert Slot.from_text(slot, TOPPER)


@pytest.mark.parametrize("slot", ["Trail"])
def test_contains_trail(slot):
    assert Slot.from_text(slot, TRAIL)


@pytest.mark.parametrize("slot", ["Wheels"])
def test_contains_wheel(slot):
    assert Slot.from_text(slot, WHEEL)
