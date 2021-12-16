import pytest

from rl_data_utils.item.slot.constants import *
from rl_data_utils.item.slot.slot import Slot
from tests_items.tests_certificates.test_items_certificates import samples_items


@pytest.mark.parametrize('items', samples_items)
def test_get_items_antenna(items):
    print(items.filter_by_attribute(Slot(ANTENNA)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_avatar_border(items):
    print(items.filter_by_attribute(Slot(BORDER)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_banner(items):
    print(items.filter_by_attribute(Slot(BANNER)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_boost(items):
    print(items.filter_by_attribute(Slot(BOOST)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_car(items):
    print(items.filter_by_attribute(Slot(CAR)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_decal(items):
    print(items.filter_by_attribute(Slot(DECAL)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_engine_audio(items):
    print(items.filter_by_attribute(Slot(ENGINE_AUDIO)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_gift_pack(items):
    print(items.filter_by_attribute(Slot(GIFT_PACK)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_goal_explosion(items):
    print(items.filter_by_attribute(Slot(GOAL_EXPLOSION)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_paint_finish(items):
    print(items.filter_by_attribute(Slot(PAINT_FINISH)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_player_anthem(items):
    print(items.filter_by_attribute(Slot(ANTHEM)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_topper(items):
    print(items.filter_by_attribute(Slot(TOPPER)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_trail(items):
    print(items.filter_by_attribute(Slot(TRAIL)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_wheel(items):
    print(items.filter_by_attribute(Slot(WHEEL)))
