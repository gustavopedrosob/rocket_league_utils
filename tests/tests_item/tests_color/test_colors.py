import pytest

from rl_data_utils.item.attribute.attribute import Color
from rl_data_utils.item.attribute_data.attribute_data import Colors
from rl_data_utils.item.attribute.constants import BLACK, BURNT_SIENNA, COBALT, CRIMSON, DEFAULT, FOREST_GREEN, GREY, \
    LIME, ORANGE, PINK, PURPLE, SAFFRON, SKY_BLUE, TITANIUM_WHITE
from rl_data_utils.item.attribute_data.constants import COLORS
from tests_item.tests_color.test_color import insider_colors, inventory_colors

colors_data = Colors.from_str_list(COLORS)


@pytest.mark.parametrize("color", [*inventory_colors, *insider_colors, *COLORS])
def test_has_color(color):
    assert colors_data.has(Color(color))


@pytest.mark.parametrize("color", [*inventory_colors, *insider_colors, *COLORS])
def test_get_respective_color(color):
    result = colors_data.get_respective(Color(color))
    print(result)


@pytest.mark.parametrize("colors", [COLORS])
def test_has_black(colors):
    assert colors_data.has(Color(BLACK))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_burnt_sienna(colors):
    assert colors_data.has(Color(BURNT_SIENNA))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_cobalt(colors):
    assert colors_data.has(Color(COBALT))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_crimson(colors):
    assert colors_data.has(Color(CRIMSON))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_default(colors):
    assert colors_data.has(Color(DEFAULT))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_forest_green(colors):
    assert colors_data.has(Color(FOREST_GREEN))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_grey(colors):
    assert colors_data.has(Color(GREY))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_lime(colors):
    assert colors_data.has(Color(LIME))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_orange(colors):
    assert colors_data.has(Color(ORANGE))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_pink(colors):
    assert colors_data.has(Color(PINK))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_purple(colors):
    assert colors_data.has(Color(PURPLE))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_saffron(colors):
    assert colors_data.has(Color(SAFFRON))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_sky_blue(colors):
    assert colors_data.has(Color(SKY_BLUE))


@pytest.mark.parametrize("colors", [COLORS])
def test_has_titanium_white(colors):
    assert colors_data.has(Color(TITANIUM_WHITE))
