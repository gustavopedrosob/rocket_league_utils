import pytest
from rl_data_utils.item.attribute.attribute import Color
from rl_data_utils.item.attribute.constants import BLACK, BURNT_SIENNA, COBALT, CRIMSON, DEFAULT, FOREST_GREEN, GREY, \
    LIME, ORANGE, PINK, PURPLE, SAFFRON, SKY_BLUE, TITANIUM_WHITE
from rl_data_utils.item.attribute_data.constants import COLORS

inventory_colors = ['Crimson', 'Sky Blue', 'Pink', 'Orange', 'Cobalt', 'Burnt Sienna', 'Titanium White', 'Grey',
                    'Saffron', 'Lime', 'Forest Green', 'Black', 'Purple']

insider_colors = ['Default', 'Black', 'Titanium White', 'Grey', 'Crimson', 'Pink', 'Cobalt', 'Sky Blue',
                  'Burnt Sienna', 'Saffron', 'Lime', 'Forest Green', 'Orange', 'Purple']

pair_equals = [['default', 'Default'], ['black', 'Black'], ['titanium white', 'Titanium White'], ['grey', 'Grey'],
               ['crimson', 'Crimson'], ['pink', 'Pink'], ['cobalt', 'Cobalt'], ['sky blue', 'Sky Blue'],
               ['burnt sienna', 'Burnt Sienna'], ['saffron', 'Saffron'], ['lime', 'Lime'],
               ['forest green', 'Forest Green'], ['orange', 'Orange'], ['purple', 'Purple']]

samples = [inventory_colors, insider_colors, COLORS]


pair_hex = [
    (['crimson', 'red'], "#ff4d4d"), (['sky_blue', 'sb'], "#69ffff"), (['pink'], "#ff8dce"),
    (['orange'], "#da9a00"), (['blue', 'cobalt'], "#8c9eff"), (['sienna'], "#995e4d"), (['tw'], "#fff"),
    (['grey'], "#c4c4c4"), (['saffron'], "#ff8"), (['lime'], "#ccff4d"), (['fg', 'green', 'forest_green'], "#329536"),
    (['black'], "#000"), (['purple'], "#e974fd")]


@pytest.mark.parametrize('color,pair', pair_hex)
def test_get_hex_color(color, pair):
    for e in color:
        assert Color(e).get_hex() == pair


def test_get_hex_color_key_error():
    with pytest.raises(KeyError):
        Color('iansianisnan').get_hex()


def test_from_random():
    print(Color.create_random())


@pytest.mark.parametrize('color', [*inventory_colors, *insider_colors, *COLORS])
def test_is_color(color):
    assert Color(color).is_valid()


@pytest.mark.parametrize('color_1,color_2', pair_equals)
def test_compare_color(color_1, color_2):
    assert Color(color_1).compare(Color(color_2))


@pytest.mark.parametrize('color', ['black'])
def test_is_black(color):
    assert Color(color).is_exactly(BLACK)


@pytest.mark.parametrize('color', ['burnt sienna', 'bs', 'sienna'])
def test_is_burnt_sienna(color):
    assert Color(color).is_exactly(BURNT_SIENNA)


@pytest.mark.parametrize('color', ['cobalt', 'blue'])
def test_is_cobalt(color):
    assert Color(color).is_exactly(COBALT)


@pytest.mark.parametrize('color', ['crimson', 'red', 'carmesim'])
def test_is_crimson(color):
    assert Color(color).is_exactly(CRIMSON)


@pytest.mark.parametrize('color', ['default', 'regular'])
def test_is_default(color):
    assert Color(color).is_exactly(DEFAULT)


@pytest.mark.parametrize('color', ['forest green', 'green', 'fg'])
def test_is_forest_green(color):
    assert Color(color).is_exactly(FOREST_GREEN)


@pytest.mark.parametrize('color', ['grey'])
def test_is_grey(color):
    assert Color(color).is_exactly(GREY)


@pytest.mark.parametrize('color', ['lime'])
def test_is_lime(color):
    assert Color(color).is_exactly(LIME)


@pytest.mark.parametrize('color', ['orange'])
def test_is_orange(color):
    assert Color(color).is_exactly(ORANGE)


@pytest.mark.parametrize('color', ['pink'])
def test_is_pink(color):
    assert Color(color).is_exactly(PINK)


@pytest.mark.parametrize('color', ['purple'])
def test_is_purple(color):
    assert Color(color).is_exactly(PURPLE)


@pytest.mark.parametrize('color', ['saffron', 'yellow'])
def test_is_saffron(color):
    assert Color(color).is_exactly(SAFFRON)


@pytest.mark.parametrize('color', ['sky blue', 'sb'])
def test_is_sky_blue(color):
    assert Color(color).is_exactly(SKY_BLUE)


@pytest.mark.parametrize('color', ['titanium white', 'tw'])
def test_is_titanium_white(color):
    assert Color(color).is_exactly(TITANIUM_WHITE)
