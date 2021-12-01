import pytest

from rl_data_utils.item.item.credits import Credits
from rl_data_utils.item.item.item import Item


def test_credit():
    assert Credits()


@pytest.mark.parametrize('quantity', [10, 100, 110, 120, 20])
def test_credits_is_valid(quantity):
    assert Credits.initialize(quantity).is_valid()


@pytest.mark.parametrize('quantity', [1, 5, 6, 19, 15])
def test_credits_is_not_valid(quantity):
    assert not Credits.initialize(quantity).is_valid()


@pytest.mark.parametrize('item_1,item_2', [['dingo tw imported', 'dingo titanium white import']])
def test_comparing_items(item_1, item_2):
    assert Item.initialize(item_1) == Item.initialize(item_2)
