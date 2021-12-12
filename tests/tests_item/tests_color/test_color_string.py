import pytest

from rl_data_utils.item.color.color import ColorString
from rl_data_utils.item.color.constants import *


@pytest.mark.parametrize('color', ['black'])
def test_contains_black(color):
    assert ColorString(color).get_exactly(BLACK)


@pytest.mark.parametrize('color', ['burnt sienna', 'bs', 'sienna'])
def test_contains_burnt_sienna(color):
    assert ColorString(color).get_exactly(BURNT_SIENNA)


@pytest.mark.parametrize('color', ['cobalt', 'blue'])
def test_contains_cobalt(color):
    assert ColorString(color).get_exactly(COBALT)


@pytest.mark.parametrize('color', ['crimson', 'red', 'carmesim'])
def test_contains_crimson(color):
    assert ColorString(color).get_exactly(CRIMSON)


@pytest.mark.parametrize('color', ['default', 'regular'])
def test_contains_default(color):
    assert ColorString(color).get_exactly(DEFAULT)


@pytest.mark.parametrize('color', ['forest green', 'green', 'fg'])
def test_contains_forest_green(color):
    assert ColorString(color).get_exactly(FOREST_GREEN)


@pytest.mark.parametrize('color', ['grey'])
def test_contains_grey(color):
    assert ColorString(color).get_exactly(GREY)


@pytest.mark.parametrize('color', ['lime'])
def test_contains_lime(color):
    assert ColorString(color).get_exactly(LIME)


@pytest.mark.parametrize('color', ['orange'])
def test_contains_orange(color):
    assert ColorString(color).get_exactly(ORANGE)


@pytest.mark.parametrize('color', ['pink'])
def test_contains_pink(color):
    assert ColorString(color).get_exactly(PINK)


@pytest.mark.parametrize('color', ['purple'])
def test_contains_purple(color):
    assert ColorString(color).get_exactly(PURPLE)


@pytest.mark.parametrize('color', ['saffron', 'yellow'])
def test_contains_saffron(color):
    assert ColorString(color).get_exactly(SAFFRON)


@pytest.mark.parametrize('color', ['sky blue', 'sb'])
def test_contains_sky_blue(color):
    assert ColorString(color).get_exactly(SKY_BLUE)


@pytest.mark.parametrize('color', ['titanium white', 'tw'])
def test_contains_titanium_white(color):
    assert ColorString(color).get_exactly(TITANIUM_WHITE)
