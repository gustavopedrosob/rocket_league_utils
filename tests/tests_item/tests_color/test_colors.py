import pytest

from rl_data_utils.item.attribute.attribute import Color
from rl_data_utils.item.attribute_data.attribute_data import Colors
from rl_data_utils.item.attribute.constants import BLACK, BURNT_SIENNA, COBALT, CRIMSON, DEFAULT, FOREST_GREEN, GREY, \
    LIME, ORANGE, PINK, PURPLE, SAFFRON, SKY_BLUE, TITANIUM_WHITE
from rl_data_utils.item.attribute_data.constants import COLORS
from tests_item.tests_color.test_color import insider_colors, inventory_colors

colors_data = Colors(COLORS)


@pytest.mark.parametrize("color", [*inventory_colors, *insider_colors, *COLORS])
def test_has_color(color):
    assert colors_data.has(Color(color))


@pytest.mark.parametrize("color", [*inventory_colors, *insider_colors, *COLORS])
def test_get_respective_color(color):
    result = colors_data.get_respective(Color(color))
    print(result)


def test_has_black():
    assert colors_data.has(BLACK)


def test_has_burnt_sienna():
    assert colors_data.has(BURNT_SIENNA)


def test_has_cobalt():
    assert colors_data.has(COBALT)


def test_has_crimson():
    assert colors_data.has(CRIMSON)


def test_has_default():
    assert colors_data.has(DEFAULT)


def test_has_forest_green():
    assert colors_data.has(FOREST_GREEN)


def test_has_grey():
    assert colors_data.has(GREY)


def test_has_lime():
    assert colors_data.has(LIME)


def test_has_orange():
    assert colors_data.has(ORANGE)


def test_has_pink():
    assert colors_data.has(PINK)


def test_has_purple():
    assert colors_data.has(PURPLE)


def test_has_saffron():
    assert colors_data.has(SAFFRON)


def test_has_sky_blue():
    assert colors_data.has(SKY_BLUE)


def test_has_titanium_white():
    assert colors_data.has(TITANIUM_WHITE)
