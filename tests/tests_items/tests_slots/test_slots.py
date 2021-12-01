import pytest

from rl_data_utils.item import Slot
from rl_data_utils.item.slot.constants import *
from test_items_data import gameflip_data
from tests.test_items import inventory_items


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_antenna(items):
    print(items.filter_by_attribute(Slot(ANTENNA)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_avatar_border(items):
    print(items.filter_by_attribute(Slot(BORDER)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_banner(items):
    print(items.filter_by_attribute(Slot(BANNER)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_boost(items):
    print(items.filter_by_attribute(Slot(BOOST)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_car(items):
    print(items.filter_by_attribute(Slot(CAR)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_decal(items):
    print(items.filter_by_attribute(Slot(DECAL)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_engine_audio(items):
    print(items.filter_by_attribute(Slot(ENGINE_AUDIO)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_gift_pack(items):
    print(items.filter_by_attribute(Slot(GIFT_PACK)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_goal_explosion(items):
    print(items.filter_by_attribute(Slot(GOAL_EXPLOSION)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_paint_finish(items):
    print(items.filter_by_attribute(Slot(PAINT_FINISH)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_player_anthem(items):
    print(items.filter_by_attribute(Slot(ANTHEM)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_topper(items):
    print(items.filter_by_attribute(Slot(TOPPER)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_trail(items):
    print(items.filter_by_attribute(Slot(TRAIL)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_wheel(items):
    print(items.filter_by_attribute(Slot(WHEEL)).items)
