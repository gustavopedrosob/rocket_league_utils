import pytest

from rl_data_utils.item.certified.certified import Certified
from rl_data_utils.item.certified.constants import *
from tests.test_items import inventory_items
from tests.test_items_data import gameflip_data


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_aviator(items):
    print(items.filter_by_attribute(Certified(AVIATOR)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_acrobat(items):
    print(items.filter_by_attribute(Certified(ACROBAT)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_victor(items):
    print(items.filter_by_attribute(Certified(VICTOR)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_striker(items):
    print(items.filter_by_attribute(Certified(STRIKER)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_sniper(items):
    print(items.filter_by_attribute(Certified(SNIPER)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_scorer(items):
    print(items.filter_by_attribute(Certified(SCORER)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_playmaker(items):
    print(items.filter_by_attribute(Certified(PLAYMAKER)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_guardian(items):
    print(items.filter_by_attribute(Certified(GUARDIAN)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_paragon(items):
    print(items.filter_by_attribute(Certified(PARAGON)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_sweeper(items):
    print(items.filter_by_attribute(Certified(SWEEPER)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_turtle(items):
    print(items.filter_by_attribute(Certified(TURTLE)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_tactician(items):
    print(items.filter_by_attribute(Certified(TACTICIAN)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_showoff(items):
    print(items.filter_by_attribute(Certified(SHOW_OFF)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_juggler(items):
    print(items.filter_by_attribute(Certified(JUGGLER)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_goalkeeper(items):
    print(items.filter_by_attribute(Certified(GOALKEEPER)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_none(items):
    print(items.filter_by_attribute(Certified(NONE)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_undefined(items):
    print(items.filter_by_attribute(Certified.create_undefined()).items)
