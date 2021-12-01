import pytest

from rl_data_utils.item import Color
from rl_data_utils.item.color.constants import *
from test_items_data import gameflip_data
from tests.test_items import inventory_items


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_crimson(items):
    print(items.filter_by_attribute(Color(CRIMSON)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_sky_blue(items):
    print(items.filter_by_attribute(Color(SKY_BLUE)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_pink(items):
    print(items.filter_by_attribute(Color(PINK)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_orange(items):
    print(items.filter_by_attribute(Color(ORANGE)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_cobalt(items):
    print(items.filter_by_attribute(Color(COBALT)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_burnt_sienna(items):
    print(items.filter_by_attribute(Color(BURNT_SIENNA)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_titanium_white(items):
    print(items.filter_by_attribute(Color(TITANIUM_WHITE)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_grey(items):
    print(items.filter_by_attribute(Color(GREY)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_saffron(items):
    print(items.filter_by_attribute(Color(SAFFRON)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_lime(items):
    print(items.filter_by_attribute(Color(LIME)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_forest_green(items):
    print(items.filter_by_attribute(Color(FOREST_GREEN)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_black(items):
    print(items.filter_by_attribute(Color(BLACK)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_purple(items):
    print(items.filter_by_attribute(Color(PURPLE)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_default(items):
    print(items.filter_by_attribute(Color(DEFAULT)).items)


@pytest.mark.parametrize('items', [inventory_items, gameflip_data])
def test_get_items_undefined(items):
    print(items.filter_by_attribute(Color.create_undefined()).items)

