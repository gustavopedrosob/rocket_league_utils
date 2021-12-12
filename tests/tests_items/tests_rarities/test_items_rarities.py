import pytest

from rl_data_utils.item.rarity.constants import *
from rl_data_utils.item.rarity.rarity import Rarity
from tests.test_items_data import gameflip_data
from tests.test_items import inventory_items


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_common(items):
    print(items.filter_by_attribute(Rarity(COMMON)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_legacy(items):
    print(items.filter_by_attribute(Rarity(LEGACY)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_uncommon(items):
    print(items.filter_by_attribute(Rarity(UNCOMMON)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_rare(items):
    print(items.filter_by_attribute(Rarity(RARE)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_very_rare(items):
    print(items.filter_by_attribute(Rarity(VERY_RARE)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_import(items):
    print(items.filter_by_attribute(Rarity(IMPORT)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_exotic(items):
    print(items.filter_by_attribute(Rarity(EXOTIC)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_black_market(items):
    print(items.filter_by_attribute(Rarity(BLACK_MARKET)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_limited(items):
    print(items.filter_by_attribute(Rarity(LIMITED)).items)
