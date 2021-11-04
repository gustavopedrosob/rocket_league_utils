from rl_data_utils.rarity import all_are_rarities
from rl_data_utils.rarity.constants import RARITIES

rl_insider_api_rarities = ['Limited', 'Uncommon', 'Rare', 'Very Rare', 'Import', 'Exotic', 'Black Market']

rl_inventory_api_rarities = ['Import', 'Limited', 'Uncommon', 'Black market', 'Rare', 'Very rare', 'Exotic']


def tests_is_rarity():
    assert all_are_rarities(rl_insider_api_rarities)
    assert all_are_rarities(RARITIES)
    assert all_are_rarities(rl_inventory_api_rarities)
