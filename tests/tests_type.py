from rl_data_utils.type import all_are_types
from rl_data_utils.type.constants import TYPES

rl_inventory_api_types = ['Engine Audio', 'Player Banner', 'Body', 'Topper', 'Goal Explosion', 'Wheels',
                          'Player Anthem', 'Animated Decal', 'Paint Finish', 'Blueprint', 'Decal', 'Avatar Border',
                          'Antenna', 'Rocket Boost', 'Player Title', 'Trail']

rl_insider_api_types = ['Wheels', 'Cars', 'Boosts', 'Toppers', 'Decals', 'Antennas', 'Goal Explosions', 'Trails',
                        'Gift Packs', 'Paint Finishes', 'Banners', 'Engine Audios', 'Avatar Borders']


def test_is_type():
    assert all_are_types(rl_inventory_api_types)
    assert all_are_types(TYPES)
    assert all_are_types(rl_insider_api_types)
