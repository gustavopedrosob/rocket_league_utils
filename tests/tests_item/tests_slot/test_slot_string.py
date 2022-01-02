import pytest

from rl_data_utils.item.attribute_string.attribute_string import AttributeString
from rl_data_utils.item.slot.constants import *
from rl_data_utils.item.slot.slot import Slot


@pytest.mark.parametrize('slot', ['Antenna'])
def test_contains_antenna(slot):
    assert AttributeString(Slot, slot).get_exactly(ANTENNA)


@pytest.mark.parametrize('slot', ['Avatar Border'])
def test_contains_border(slot):
    assert AttributeString(Slot, slot).get_exactly(BORDER)


@pytest.mark.parametrize('slot', ['Banner'])
def test_contains_banner(slot):
    assert AttributeString(Slot, slot).get_exactly(BANNER)


@pytest.mark.parametrize('slot', ['Boost'])
def test_contains_boost(slot):
    assert AttributeString(Slot, slot).get_exactly(BOOST)


@pytest.mark.parametrize('slot', ['Car'])
def test_contains_car(slot):
    assert AttributeString(Slot, slot).get_exactly(CAR)


@pytest.mark.parametrize('slot', ['Decal'])
def test_contains_decal(slot):
    assert AttributeString(Slot, slot).get_exactly(DECAL)


@pytest.mark.parametrize('slot', ['Engine Audio'])
def test_contains_engine_audio(slot):
    assert AttributeString(Slot, slot).get_exactly(ENGINE_AUDIO)


@pytest.mark.parametrize('slot', ['Gift Pack'])
def test_contains_gift_pack(slot):
    assert AttributeString(Slot, slot).get_exactly(GIFT_PACK)


@pytest.mark.parametrize('slot', ['Goal Explosion'])
def test_contains_goal_explosion(slot):
    assert AttributeString(Slot, slot).get_exactly(GOAL_EXPLOSION)


@pytest.mark.parametrize('slot', ['Paint Finish'])
def test_contains_paint_finish(slot):
    assert AttributeString(Slot, slot).get_exactly(PAINT_FINISH)


@pytest.mark.parametrize('slot', ['Anthem'])
def test_contains_anthem(slot):
    assert AttributeString(Slot, slot).get_exactly(ANTHEM)


@pytest.mark.parametrize('slot', ['Topper'])
def test_contains_topper(slot):
    assert AttributeString(Slot, slot).get_exactly(TOPPER)


@pytest.mark.parametrize('slot', ['Trail'])
def test_contains_trail(slot):
    assert AttributeString(Slot, slot).get_exactly(TRAIL)


@pytest.mark.parametrize('slot', ['Wheels'])
def test_contains_wheel(slot):
    assert AttributeString(Slot, slot).get_exactly(WHEEL)
