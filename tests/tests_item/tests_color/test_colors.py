import pytest

from rl_data_utils.item.color.color import Colors
from rl_data_utils.item.color.constants import *
from tests.tests_item.tests_color.test_color import inventory_colors, insider_colors


@pytest.mark.parametrize('color', [*inventory_colors, *insider_colors, *COLORS])
def test_has_color(color):
    assert Colors(COLORS).has(color)


@pytest.mark.parametrize('color', [*inventory_colors, *insider_colors, *COLORS])
def test_get_respective_color(color):
    result = Colors(COLORS).get_respective(color)
    print(result)


@pytest.mark.parametrize('colors', [COLORS])
def test_validate_colors(colors):
    Colors(colors).validate()


@pytest.mark.parametrize('colors', [COLORS])
def test_are_valid_colors(colors):
    assert Colors(colors).is_valid()


@pytest.mark.parametrize('colors', [COLORS])
def test_has_black(colors):
    assert Colors(colors).has_exactly(BLACK)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_burnt_sienna(colors):
    assert Colors(colors).has_exactly(BURNT_SIENNA)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_cobalt(colors):
    assert Colors(colors).has_exactly(COBALT)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_crimson(colors):
    assert Colors(colors).has_exactly(CRIMSON)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_default(colors):
    assert Colors(colors).has_exactly(DEFAULT)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_forest_green(colors):
    assert Colors(colors).has_exactly(FOREST_GREEN)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_grey(colors):
    assert Colors(colors).has_exactly(GREY)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_lime(colors):
    assert Colors(colors).has_exactly(LIME)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_orange(colors):
    assert Colors(colors).has_exactly(ORANGE)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_pink(colors):
    assert Colors(colors).has_exactly(PINK)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_purple(colors):
    assert Colors(colors).has_exactly(PURPLE)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_saffron(colors):
    assert Colors(colors).has_exactly(SAFFRON)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_sky_blue(colors):
    assert Colors(colors).has_exactly(SKY_BLUE)


@pytest.mark.parametrize('colors', [COLORS])
def test_has_titanium_white(colors):
    assert Colors(colors).has_exactly(TITANIUM_WHITE)
