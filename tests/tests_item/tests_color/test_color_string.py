import pytest

from rl_data_utils.item.attribute.constants import BLACK, BURNT_SIENNA, COBALT, CRIMSON, DEFAULT, FOREST_GREEN, GREY, \
    LIME, ORANGE, PINK, PURPLE, SAFFRON, SKY_BLUE, TITANIUM_WHITE
from rl_data_utils.item.attribute.attribute import Color


@pytest.mark.parametrize("color", ["black"])
def test_contains_black(color):
    assert Color.from_text(color, BLACK)


@pytest.mark.parametrize("color", ["burnt sienna", "bs", "sienna"])
def test_contains_burnt_sienna(color):
    assert Color.from_text(color, BURNT_SIENNA)


@pytest.mark.parametrize("color", ["cobalt", "blue"])
def test_contains_cobalt(color):
    assert Color.from_text(color, COBALT)


@pytest.mark.parametrize("color", ["crimson", "red", "carmesim"])
def test_contains_crimson(color):
    assert Color.from_text(color, CRIMSON)


@pytest.mark.parametrize("color", ["default", "regular"])
def test_contains_default(color):
    assert Color.from_text(color, DEFAULT)


@pytest.mark.parametrize("color", ["forest green", "green", "fg"])
def test_contains_forest_green(color):
    assert Color.from_text(color, FOREST_GREEN)


@pytest.mark.parametrize("color", ["grey"])
def test_contains_grey(color):
    assert Color.from_text(color, GREY)


@pytest.mark.parametrize("color", ["lime"])
def test_contains_lime(color):
    assert Color.from_text(color, LIME)


@pytest.mark.parametrize("color", ["orange"])
def test_contains_orange(color):
    assert Color.from_text(color, ORANGE)


@pytest.mark.parametrize("color", ["pink"])
def test_contains_pink(color):
    assert Color.from_text(color, PINK)


@pytest.mark.parametrize("color", ["purple"])
def test_contains_purple(color):
    assert Color.from_text(color, PURPLE)


@pytest.mark.parametrize("color", ["saffron", "yellow"])
def test_contains_saffron(color):
    assert Color.from_text(color, SAFFRON)


@pytest.mark.parametrize("color", ["sky blue", "sb"])
def test_contains_sky_blue(color):
    assert Color.from_text(color, SKY_BLUE)


@pytest.mark.parametrize("color", ["titanium white", "tw"])
def test_contains_titanium_white(color):
    assert Color.from_text(color, TITANIUM_WHITE)
