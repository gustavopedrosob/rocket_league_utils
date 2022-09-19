import pytest

from rl_data_utils.item.attribute.preset import BLACK_MARKET, COMMON, EXOTIC, IMPORT, LEGACY, LIMITED, RARE, \
    UNCOMMON, VERY_RARE
from tests_items.tests_certificates.test_items_certificates import samples_items


@pytest.mark.parametrize('items', samples_items)
def test_get_items_common(items):
    print(items.filter_by_attribute(COMMON))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_legacy(items):
    print(items.filter_by_attribute(LEGACY))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_uncommon(items):
    print(items.filter_by_attribute(UNCOMMON))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_rare(items):
    print(items.filter_by_attribute(RARE))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_very_rare(items):
    print(items.filter_by_attribute(VERY_RARE))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_import(items):
    print(items.filter_by_attribute(IMPORT))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_exotic(items):
    print(items.filter_by_attribute(EXOTIC))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_black_market(items):
    print(items.filter_by_attribute(BLACK_MARKET))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_limited(items):
    print(items.filter_by_attribute(LIMITED))
