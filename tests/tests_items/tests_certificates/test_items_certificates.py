import pytest

from rl_data_utils.item.certified.certified import Certified
from rl_data_utils.item.certified.constants import *
from test_items_rl_insider import rl_insider_items
from tests.test_items import inventory_items
from tests.test_items_data import gameflip_data


samples_items = [inventory_items, gameflip_data, rl_insider_items]


@pytest.mark.parametrize('items', samples_items)
def test_get_items_aviator(items):
    print(items.filter_by_attribute(Certified(AVIATOR)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_acrobat(items):
    print(items.filter_by_attribute(Certified(ACROBAT)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_victor(items):
    print(items.filter_by_attribute(Certified(VICTOR)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_striker(items):
    print(items.filter_by_attribute(Certified(STRIKER)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_sniper(items):
    print(items.filter_by_attribute(Certified(SNIPER)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_scorer(items):
    print(items.filter_by_attribute(Certified(SCORER)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_playmaker(items):
    print(items.filter_by_attribute(Certified(PLAYMAKER)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_guardian(items):
    print(items.filter_by_attribute(Certified(GUARDIAN)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_paragon(items):
    print(items.filter_by_attribute(Certified(PARAGON)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_sweeper(items):
    print(items.filter_by_attribute(Certified(SWEEPER)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_turtle(items):
    print(items.filter_by_attribute(Certified(TURTLE)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_tactician(items):
    print(items.filter_by_attribute(Certified(TACTICIAN)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_showoff(items):
    print(items.filter_by_attribute(Certified(SHOW_OFF)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_juggler(items):
    print(items.filter_by_attribute(Certified(JUGGLER)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_goalkeeper(items):
    print(items.filter_by_attribute(Certified(GOALKEEPER)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_none(items):
    print(items.filter_by_attribute(Certified(NONE)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_undefined(items):
    items.filter_by_attribute(Certified.create_undefined())
