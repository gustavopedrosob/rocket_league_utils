from rl_data_utils.exceptions import SlotNotExists
from test_items import sample_items
import pytest


def test_get_items_by_slot_slot_not_exists():
    with pytest.raises(SlotNotExists):
        sample_items.get_items_by_slot('')


def test_get_items_by_slot():
    print(sample_items.get_items_by_slot("goal explosion").items)


def test_get_items_by_slot_regex():
    print(sample_items.get_items_by_slot_regex('g').items)


def test_get_items_by_slot_equal_to():
    print(sample_items.get_items_by_slot_equal_to("Goal Explosion").items)


def test_get_items_by_slot_contains():
    print(sample_items.get_items_by_slot_contains("G").items)


def test_get_slots():
    print(sample_items.get_slots())


def test_get_items_antenna():
    print(sample_items.get_items_antenna().items)


def test_get_items_avatar_border():
    print(sample_items.get_items_avatar_border().items)


def test_get_items_banner():
    print(sample_items.get_items_banner().items)


def test_get_items_boost():
    print(sample_items.get_items_boost().items)


def test_get_items_car():
    print(sample_items.get_items_car().items)


def test_get_items_decal():
    print(sample_items.get_items_decal().items)


def test_get_items_engine_audio():
    print(sample_items.get_items_engine_audio().items)


def test_get_items_gift_pack():
    print(sample_items.get_items_gift_pack().items)


def test_get_items_goal_explosion():
    print(sample_items.get_items_goal_explosion().items)


def test_get_items_paint_finish():
    print(sample_items.get_items_paint_finish().items)


def test_get_items_player_anthem():
    print(sample_items.get_items_player_anthem().items)


def test_get_items_topper():
    print(sample_items.get_items_topper().items)


def test_get_items_trail():
    print(sample_items.get_items_trail().items)


def test_get_items_wheel():
    print(sample_items.get_items_wheel().items)
