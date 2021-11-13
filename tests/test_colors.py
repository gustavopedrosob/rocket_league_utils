import pytest
from rl_data_utils.exceptions import ColorNotExists
from test_items import sample_items

sample_items = sample_items.get_items_with_valid_color()


def test_get_items_by_color_color_not_exists():
    with pytest.raises(ColorNotExists):
        sample_items.get_items_by_color("")


def test_get_items_by_color():
    print(sample_items.get_items_by_color("crimson").items)


def test_get_items_by_color_regex():
    print(sample_items.get_items_by_color_regex('c').items)


def test_get_items_by_color_equal_to():
    print(sample_items.get_items_by_color_equal_to("Crimson").items)


def test_get_items_by_color_contains():
    print(sample_items.get_items_by_color_contains("c").items)


def test_get_colors():
    print(sample_items.get_colors())


def test_get_items_crimson():
    print(sample_items.get_items_crimson().items)


def test_get_items_sky_blue():
    print(sample_items.get_items_sky_blue().items)


def test_get_items_pink():
    print(sample_items.get_items_pink().items)


def test_get_items_orange():
    print(sample_items.get_items_orange().items)


def test_get_items_cobalt():
    print(sample_items.get_items_cobalt().items)


def test_get_items_burnt_sienna():
    print(sample_items.get_items_burnt_sienna().items)


def test_get_items_titanium_white():
    print(sample_items.get_items_titanium_white().items)


def test_get_items_grey():
    print(sample_items.get_items_grey().items)


def test_get_items_saffron():
    print(sample_items.get_items_saffron().items)


def test_get_items_lime():
    print(sample_items.get_items_lime().items)


def test_get_items_forest_green():
    print(sample_items.get_items_forest_green().items)


def test_get_items_black():
    print(sample_items.get_items_black().items)


def test_get_items_purple():
    print(sample_items.get_items_purple().items)
