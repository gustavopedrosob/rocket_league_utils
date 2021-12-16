from logging import info, basicConfig, INFO

import pytest

from rl_data_utils.item.color.constants import DEFAULT
from rl_data_utils.item.item.constants import INDENTIFIER
from rl_data_utils.item.item.credit import Credit
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.rarity.constants import *


basicConfig(level=INFO)


def test_indentifier_compare():
    item_1 = Item(True, 'Dingo', 'Car', 'Titanium White', 'Imported', 'Striker', 1, False, True, 'pc')
    item_2 = Item(False, 'Dingo', 'Car', 'Grey', 'Imported', 'Goalkeeper', 5, False, True, 'pc')
    assert item_1.compare(item_2, INDENTIFIER)


def test_is_ncr():
    ncvr_item = Item(rarity=RARE)
    assert ncvr_item.is_ncr()


def test_is_ncvr():
    ncvr_item = Item(rarity=VERY_RARE)
    assert ncvr_item.is_ncvr()


def test_is_nci():
    ncvr_item = Item(rarity=IMPORT)
    assert ncvr_item.is_nci()


def test_is_nce():
    ncvr_item = Item(rarity=EXOTIC)
    assert ncvr_item.is_nce()


def test_is_undefined():
    assert Item().is_undefined()
    assert not Item(color=DEFAULT).is_undefined()


def test_from_random():
    info(Item.create_random())


def test_credit():
    assert Credit()


@pytest.mark.parametrize('quantity', [10, 100, 110, 120, 20])
def test_credits_is_valid(quantity):
    assert Credit.initialize(quantity).is_valid()


@pytest.mark.parametrize('quantity', [1, 5, 6, 19, 15])
def test_credits_is_not_valid(quantity):
    assert not Credit.initialize(quantity).is_valid()


@pytest.mark.parametrize('item_1,item_2', [['dingo tw imported', 'dingo titanium white import']])
def test_comparing_items(item_1, item_2):
    assert Item.initialize(item_1).compare(Item.initialize(item_2))
