import pytest

from rl_data_utils.item.attribute.preset import AVIATOR, ACROBAT, VICTOR, PLAYMAKER, PARAGON, GUARDIAN, SWEEPER, TURTLE, \
    TACTICIAN, SHOW_OFF, JUGGLER, GOALKEEPER, NONE, STRIKER, SNIPER, SCORER
from test_items import inventory_items
from test_items_data import gameflip_data
from test_items_rl_insider import rl_insider_items


samples_items = [inventory_items, gameflip_data, rl_insider_items]


@pytest.mark.parametrize('items', samples_items)
def test_get_items_aviator(items):
    print(items.filter_by_attribute(AVIATOR))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_acrobat(items):
    print(items.filter_by_attribute(ACROBAT))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_victor(items):
    print(items.filter_by_attribute(VICTOR))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_striker(items):
    print(items.filter_by_attribute(STRIKER))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_sniper(items):
    print(items.filter_by_attribute(SNIPER))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_scorer(items):
    print(items.filter_by_attribute(SCORER))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_playmaker(items):
    print(items.filter_by_attribute(PLAYMAKER))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_guardian(items):
    print(items.filter_by_attribute(GUARDIAN))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_paragon(items):
    print(items.filter_by_attribute(PARAGON))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_sweeper(items):
    print(items.filter_by_attribute(SWEEPER))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_turtle(items):
    print(items.filter_by_attribute(TURTLE))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_tactician(items):
    print(items.filter_by_attribute(TACTICIAN))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_showoff(items):
    print(items.filter_by_attribute(SHOW_OFF))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_juggler(items):
    print(items.filter_by_attribute(JUGGLER))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_goalkeeper(items):
    print(items.filter_by_attribute(GOALKEEPER))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_none(items):
    print(items.filter_by_attribute(NONE))

