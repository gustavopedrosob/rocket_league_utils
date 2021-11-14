import pytest
from rl_data_utils.exceptions import ColorNotExists, InvalidColorsList, ColorIsNotInString
from rl_data_utils.utils.item.color.color import all_are_colors, compare_colors, contains_colors, get_color_in_string, \
    get_respective_color, is_color, validate_colors_list, validate_color, has_color
from rl_data_utils.utils.item.color.constants import COLORS
from rl_data_utils.utils.item.color.contains import contains_black, contains_burnt_sienna, contains_cobalt, \
    contains_crimson, contains_default, contains_forest_green, contains_grey, contains_lime, contains_orange, \
    contains_pink, contains_purple, contains_saffron, contains_sky_blue, contains_titanium_white
from rl_data_utils.utils.item.color.is_functions import is_black, is_burnt_sienna, is_cobalt, is_crimson, is_default, \
    is_forest_green, is_grey, is_lime, is_orange, is_pink, is_purple, is_saffron, is_sky_blue, is_titanium_white

inventory_colors = ['Crimson', 'Sky Blue', 'Pink', 'Orange', 'Cobalt', 'Burnt Sienna', 'Titanium White', 'Grey',
                    'Saffron', 'Lime', 'Forest Green', 'Black', 'Purple']

insider_colors = ['Default', 'Black', 'Titanium White', 'Grey', 'Crimson', 'Pink', 'Cobalt', 'Sky Blue',
                  'Burnt Sienna', 'Saffron', 'Lime', 'Forest Green', 'Orange', 'Purple']

pair_equals = [['default', 'Default'], ['black', 'Black'], ['titanium white', 'Titanium White'], ['grey', 'Grey'],
               ['crimson', 'Crimson'], ['pink', 'Pink'], ['cobalt', 'Cobalt'], ['sky blue', 'Sky Blue'],
               ['burnt sienna', 'Burnt Sienna'], ['saffron', 'Saffron'], ['lime', 'Lime'],
               ['forest green', 'Forest Green'], ['orange', 'Orange'], ['purple', 'Purple']]


def test_all_are_colors():
    for container in [inventory_colors, insider_colors, COLORS]:
        assert all_are_colors(container)


def test_compare_colors():
    for pair in pair_equals:
        assert compare_colors(*pair)
    with pytest.raises(ColorNotExists):
        compare_colors('', 'red')
        compare_colors('red', '')


def test_contains_colors():
    for container in [inventory_colors, insider_colors, COLORS]:
        for color in container:
            assert contains_colors(color)


def test_has_color():
    assert has_color('red', inventory_colors)
    with pytest.raises(ColorNotExists):
        has_color('', inventory_colors)
    with pytest.raises(InvalidColorsList):
        has_color('red', [''])


def test_get_color_in_string():
    assert get_color_in_string('Dingo Titanium White Striker') == 'Titanium White'
    with pytest.raises(ColorIsNotInString):
        get_color_in_string('Dingo Striker')


def test_get_respective_color():
    for c1, c2 in pair_equals:
        assert get_respective_color(c1) == c2
    with pytest.raises(ColorNotExists):
        get_respective_color('')


def test_is_color():
    for container in [inventory_colors, insider_colors, COLORS]:
        for color in container:
            assert is_color(color)


def test_validate_colors_list():
    for container in [inventory_colors, insider_colors, COLORS]:
        validate_colors_list(container)
    with pytest.raises(InvalidColorsList):
        validate_colors_list(['', 'red'])


def test_validate_color():
    for container in [inventory_colors, insider_colors, COLORS]:
        for color in container:
            validate_color(color)
    with pytest.raises(ColorNotExists):
        validate_color('')


def test_is_black():
    assert is_black('black')


def test_is_burnt_sienna():
    assert is_burnt_sienna('bs')
    assert is_burnt_sienna('burnt sienna')
    assert is_burnt_sienna('sienna')


def test_is_cobalt():
    assert is_cobalt('cobalt')
    assert is_cobalt('blue')


def test_is_crimson():
    assert is_crimson('crimson')
    assert is_crimson('carmesim')
    assert is_crimson('red')


def test_is_default():
    assert is_default('none')
    assert is_default('default')
    assert is_default('regular')


def test_is_forest_green():
    assert is_forest_green('fg')
    assert is_forest_green('forest green')
    assert is_forest_green('green')
    assert is_forest_green('forestgreen')


def test_is_grey():
    assert is_grey('grey')


def test_is_lime():
    assert is_lime('lime')


def test_is_orange():
    assert is_orange('orange')


def test_is_pink():
    assert is_pink('pink')


def test_is_purple():
    assert is_purple('purple')


def test_is_saffron():
    assert is_saffron('saffron')
    assert is_saffron('yellow')


def test_is_sky_blue():
    assert is_sky_blue('sky blue')
    assert is_sky_blue('skyblue')
    assert is_sky_blue('sb')


def test_is_titanium_white():
    assert is_titanium_white('titanium white')
    assert is_titanium_white('white')


def test_contains_black():
    assert contains_black('black')


def test_contains_burnt_sienna():
    assert contains_burnt_sienna('bs')
    assert contains_burnt_sienna('burnt sienna')
    assert contains_burnt_sienna('sienna')


def test_contains_cobalt():
    assert contains_cobalt('cobalt')
    assert contains_cobalt('blue')


def test_contains_crimson():
    assert contains_crimson('crimson')
    assert contains_crimson('red')


def test_contains_default():
    assert contains_default('none')
    assert contains_default('default')
    assert contains_default('regular')


def test_contains_forest_green():
    assert contains_forest_green('fg')
    assert contains_forest_green('forest green')
    assert contains_forest_green('green')
    assert contains_forest_green('forestgreen')


def test_contains_grey():
    assert contains_grey('grey')


def test_contains_lime():
    assert contains_lime('lime')


def test_contains_orange():
    assert contains_orange('orange')


def test_contains_pink():
    assert contains_pink('pink')


def test_contains_purple():
    assert contains_purple('purple')


def test_contains_saffron():
    assert contains_saffron('saffron')
    assert contains_saffron('yellow')


def test_contains_sky_blue():
    assert contains_sky_blue('sky blue')
    assert contains_sky_blue('skyblue')
    assert contains_sky_blue('sb')


def test_contains_titanium_white():
    assert contains_titanium_white('titanium white')
    assert contains_titanium_white('white')
