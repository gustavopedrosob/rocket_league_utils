from rl_data_utils.item.color import all_are_colors
from rl_data_utils.utils.item.color.constants import COLORS

rl_inventory_api_colors = ['Crimson', 'Sky Blue', 'Pink', 'Orange', 'Cobalt', 'Burnt Sienna', 'Titanium White', 'Grey',
                           'Saffron', 'Lime', 'Forest Green', 'Black', 'Purple']

rl_insider_api_colors = ['Default', 'Black', 'Titanium White', 'Grey', 'Crimson', 'Pink', 'Cobalt', 'Sky Blue',
                         'Burnt Sienna', 'Saffron', 'Lime', 'Forest Green', 'Orange', 'Purple']


def tests_is_color():
    assert all_are_colors(rl_inventory_api_colors)
    assert all_are_colors(COLORS)
    assert all_are_colors(rl_insider_api_colors)
