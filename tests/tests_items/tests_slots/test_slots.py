import pytest

from rl_data_utils.item.attribute.preset import ANTENNA, BORDER, CAR, DECAL, ENGINE_AUDIO, GOAL_EXPLOSION, GIFT_PACK, \
    PAINT_FINISH, ANTHEM, BANNER, BOOST, TOPPER, TRAIL, WHEEL
from tests_items.tests_certificates.test_items_certificates import samples_items


@pytest.mark.parametrize('items', samples_items)
def test_get_items_antenna(items):
    print(items.filter_by_attribute(ANTENNA))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_avatar_border(items):
    print(items.filter_by_attribute(BORDER))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_banner(items):
    print(items.filter_by_attribute(BANNER))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_boost(items):
    print(items.filter_by_attribute(BOOST))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_car(items):
    print(items.filter_by_attribute(CAR))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_decal(items):
    print(items.filter_by_attribute(DECAL))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_engine_audio(items):
    print(items.filter_by_attribute(ENGINE_AUDIO))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_gift_pack(items):
    print(items.filter_by_attribute(GIFT_PACK))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_goal_explosion(items):
    print(items.filter_by_attribute(GOAL_EXPLOSION))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_paint_finish(items):
    print(items.filter_by_attribute(PAINT_FINISH))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_player_anthem(items):
    print(items.filter_by_attribute(ANTHEM))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_topper(items):
    print(items.filter_by_attribute(TOPPER))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_trail(items):
    print(items.filter_by_attribute(TRAIL))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_wheel(items):
    print(items.filter_by_attribute(WHEEL))
