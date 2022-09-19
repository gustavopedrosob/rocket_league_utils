import pytest

from rl_data_utils.item.attribute.attribute import Color
from rl_data_utils.item.attribute.constants import BLACK, BURNT_SIENNA, COBALT, CRIMSON, DEFAULT, FOREST_GREEN, GREY, \
    LIME, ORANGE, PINK, PURPLE, SAFFRON, SKY_BLUE, TITANIUM_WHITE
from tests_items.tests_certificates.test_items_certificates import samples_items


@pytest.mark.parametrize('items', samples_items)
def test_get_items_crimson(items):
    print(items.filter_by_attribute(Color(CRIMSON)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_sky_blue(items):
    print(items.filter_by_attribute(Color(SKY_BLUE)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_pink(items):
    print(items.filter_by_attribute(Color(PINK)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_orange(items):
    print(items.filter_by_attribute(Color(ORANGE)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_cobalt(items):
    print(items.filter_by_attribute(Color(COBALT)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_burnt_sienna(items):
    print(items.filter_by_attribute(Color(BURNT_SIENNA)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_titanium_white(items):
    print(items.filter_by_attribute(Color(TITANIUM_WHITE)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_grey(items):
    print(items.filter_by_attribute(Color(GREY)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_saffron(items):
    print(items.filter_by_attribute(Color(SAFFRON)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_lime(items):
    print(items.filter_by_attribute(Color(LIME)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_forest_green(items):
    print(items.filter_by_attribute(Color(FOREST_GREEN)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_black(items):
    print(items.filter_by_attribute(Color(BLACK)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_purple(items):
    print(items.filter_by_attribute(Color(PURPLE)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_default(items):
    print(items.filter_by_attribute(Color(DEFAULT)))
