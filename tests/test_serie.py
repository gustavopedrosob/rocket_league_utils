from rl_data_utils.utils.item.serie.is_functions import *
from rl_data_utils.utils.item.serie.series import compare_series, is_serie

inventory_series = ['Accelerator', 'Accolade', 'Accolade II', 'Auriga', 'Champions 1', 'Champions 2', 'Champions 3',
                    'Champions 4', 'Crate', 'Elevation', 'Ferocity', "Golden Egg '18", "Golden Egg '19",
                    "Golden Lantern '19", "Golden Pumpkin '20", 'Ignition', 'Impact', 'Momentum', 'Nitro', 'Overdrive',
                    "Player's Choice", 'Postgame', 'Promo code', 'RLCS reward', 'Seasonal event', 'Season 1',
                    'Season reward', 'Secret Santa', 'Totally Awesome', 'Triumph', 'Turbo', 'Velocity', 'Victory',
                    'Vindicator', 'WWE promo code', 'Zephyr']


def test_is_accelerator_series():
    assert is_accelerator_series('Accelerator')


def test_is_beach_blast_series():
    assert is_beach_blast_series('Beach Blast')


def test_is_bonus_gift():
    assert is_bonus_gift('Bonus Gift')


def test_is_champions_1_series():
    assert is_champions_1_series('Champions 1')


def test_is_champions_2_series():
    assert is_champions_2_series('Champions 2')


def test_is_champions_3_series():
    assert is_champions_3_series('Champions 3')


def test_is_champions_4_series():
    assert is_champions_4_series('Champions 4')


def test_is_elevation_series():
    assert is_elevation_series('Elevation')


def test_is_ferocity_series():
    assert is_ferocity_series('Ferocity')


def test_is_golden_egg_2018():
    assert is_golden_egg_2018('Golden Egg \'18')


def test_is_golden_egg_2019():
    assert is_golden_egg_2019('Golden Egg \'19')


def test_is_golden_egg_2020():
    assert is_golden_egg_2020('Golden Egg \'20')


def test_is_golden_gift_2018():
    assert is_golden_gift_2018('Golden Gift \'18')


def test_is_golden_gift_2019():
    assert is_golden_gift_2019('Golden Gift \'19')


def test_is_golden_gift_2020():
    assert is_golden_gift_2020('Golden Gift \'20')


def test_is_golden_lantern_2020():
    assert is_golden_lantern_2020('Golden Lantern \'20')


def test_is_golden_lantern_2021():
    assert is_golden_lantern_2021('Golden Lantern \'21')


def test_is_golden_pumpkin_2018():
    assert is_golden_pumpkin_2018('Golden Pumpkin \'18')


def test_is_golden_pumpkin_2019():
    assert is_golden_pumpkin_2019('Golden Pumpkin \'19')


def test_is_golden_pumpkin_2020():
    assert is_golden_pumpkin_2020('Golden Pumpkin \'20')


def test_is_haunted_hallows_series():
    assert is_haunted_hallows_series('Haunted Hallows')


def test_is_impact_series():
    assert is_impact_series('Impact')


def test_is_nitro_series():
    assert is_nitro_series('Nitro')


def test_is_non_crate():
    assert is_non_crate('Non Crate')


def test_is_overdrive_series():
    assert is_overdrive_series('Overdrive')


def test_is_players_choice_series():
    assert is_players_choice_series('Player\'s Choice')


def test_is_secret_santa_series():
    assert is_secret_santa_series('Secret Santa')


def test_is_spring_fever_series():
    assert is_spring_fever_series('Spring Fever')


def test_is_totally_awesome_series():
    assert is_totally_awesome_series('Totally Awesome')


def test_is_triumph_series():
    assert is_triumph_series('Triumph')


def test_is_turbo_series():
    assert is_turbo_series('Turbo')


def test_is_velocity_series():
    assert is_velocity_series('Velocity')


def test_is_victory_series():
    assert is_victory_series('Victory')


def test_is_vindicator_series():
    assert is_vindicator_series('Vindicator')


def test_is_zephyr_series():
    assert is_zephyr_series('Zephyr')
