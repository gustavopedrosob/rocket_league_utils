import pytest

from rl_data_utils.item.attribute.constants import ACCELERATOR, ACCOLADE_1, ACCOLADE_2, \
    AURIGA, BEACH_BLAST, BONUS_GIFT, CHAMPIONS_1, CHAMPIONS_2, CHAMPIONS_3, \
    CHAMPIONS_4, ELEVATION, FEROCITY, GOLDEN_EGG_2020, GOLDEN_EGG_2019, GOLDEN_EGG_2018, \
    GOLDEN_GIFT_2020, GOLDEN_GIFT_2019, GOLDEN_GIFT_2018, GOLDEN_LANTERN_2021, GOLDEN_LANTERN_2020, GOLDEN_LANTERN_2019, \
    GOLDEN_PUMPKIN_2020, GOLDEN_PUMPKIN_2019, GOLDEN_PUMPKIN_2018, HAUNTED_HALLOWS, IGNITION, \
    IMPACT, MOMENTUM, NITRO, NON_CRATE, OVERDRIVE, PLAYERS_CHOICE, RLCS_REWARD, \
    SEASON_1, SECRET_SANTA, SPRING_FEVER, TOTALLY_AWESOME, TRIUMPH, TURBO, \
    VELOCITY, VICTORY, VINDICATOR, ZEPHYR, WWE_PROMO_CODE
from rl_data_utils.item.attribute.attribute import Serie

inventory_series = ['Accelerator', 'Accolade 1', 'Accolade II', 'Auriga', 'Champions 1', 'Champions 2', 'Champions 3',
                    'Champions 4', 'Elevation', 'Ferocity', "Golden Egg '18", "Golden Egg '19",
                    "Golden Lantern '19", "Golden Pumpkin '20", 'Ignition', 'Impact', 'Momentum', 'Nitro', 'Overdrive',
                    "Player's Choice", 'Postgame', 'RLCS reward', 'Season 1', 'Secret Santa', 'Totally Awesome',
                    'Triumph', 'Turbo', 'Velocity', 'Victory', 'Vindicator', 'WWE promo code', 'Zephyr']


def test_from_random():
    print(Serie.create_random())


# @pytest.mark.parametrize('serie_1,serie_2', [pair_equals])
# def test_compare_serie(serie_1, serie_2):
#     assert Serie(serie_1).compare(Serie(serie_2))


@pytest.mark.parametrize('serie', ['Accelerator'])
def test_is_accelerator_series(serie):
    assert Serie(serie).is_exactly(ACCELERATOR)


@pytest.mark.parametrize('serie', ['Accolade 1'])
def test_is_accolade_1_series(serie):
    assert Serie(serie).is_exactly(ACCOLADE_1)


@pytest.mark.parametrize('serie', ['Accolade 2'])
def test_is_accolade_2_series(serie):
    assert Serie(serie).is_exactly(ACCOLADE_2)


@pytest.mark.parametrize('serie', ['Auriga'])
def test_is_auriga_series(serie):
    assert Serie(serie).is_exactly(AURIGA)


@pytest.mark.parametrize('serie', ['Beach Blast'])
def test_is_beach_blast_series(serie):
    assert Serie(serie).is_exactly(BEACH_BLAST)


@pytest.mark.parametrize('serie', ['Bonus Gift'])
def test_is_bonus_gift(serie):
    assert Serie(serie).is_exactly(BONUS_GIFT)


@pytest.mark.parametrize('serie', ['Champions 1'])
def test_is_champions_1_series(serie):
    assert Serie(serie).is_exactly(CHAMPIONS_1)


@pytest.mark.parametrize('serie', ['Champions 2'])
def test_is_champions_2_series(serie):
    assert Serie(serie).is_exactly(CHAMPIONS_2)


@pytest.mark.parametrize('serie', ['Champions 3'])
def test_is_champions_3_series(serie):
    assert Serie(serie).is_exactly(CHAMPIONS_3)


@pytest.mark.parametrize('serie', ['Champions 4'])
def test_is_champions_4_series(serie):
    assert Serie(serie).is_exactly(CHAMPIONS_4)


@pytest.mark.parametrize('serie', ['Elevation'])
def test_is_elevation_series(serie):
    assert Serie(serie).is_exactly(ELEVATION)


@pytest.mark.parametrize('serie', ['Ferocity'])
def test_is_ferocity_series(serie):
    assert Serie(serie).is_exactly(FEROCITY)


@pytest.mark.parametrize('serie', ['Golden Egg \'18'])
def test_is_golden_egg_2018(serie):
    assert Serie(serie).is_exactly(GOLDEN_EGG_2018)


@pytest.mark.parametrize('serie', ['Golden Egg \'19'])
def test_is_golden_egg_2019(serie):
    assert Serie(serie).is_exactly(GOLDEN_EGG_2019)


@pytest.mark.parametrize('serie', ['Golden Egg \'20'])
def test_is_golden_egg_2020(serie):
    assert Serie(serie).is_exactly(GOLDEN_EGG_2020)


@pytest.mark.parametrize('serie', ['Golden Gift 18'])
def test_is_golden_gift_2018(serie):
    assert Serie(serie).is_exactly(GOLDEN_GIFT_2018)


@pytest.mark.parametrize('serie', ['Golden Gift 19'])
def test_is_golden_gift_2019(serie):
    assert Serie(serie).is_exactly(GOLDEN_GIFT_2019)


@pytest.mark.parametrize('serie', ['Golden Gift 20'])
def test_is_golden_gift_2020(serie):
    assert Serie(serie).is_exactly(GOLDEN_GIFT_2020)


@pytest.mark.parametrize('serie', ['Golden Lantern \'19'])
def test_is_golden_lantern_2019(serie):
    assert Serie(serie).is_exactly(GOLDEN_LANTERN_2019)


@pytest.mark.parametrize('serie', ['Golden Lantern \'20'])
def test_is_golden_lantern_2020(serie):
    assert Serie(serie).is_exactly(GOLDEN_LANTERN_2020)


@pytest.mark.parametrize('serie', ['Golden Lantern \'21'])
def test_is_golden_lantern_2021(serie):
    assert Serie(serie).is_exactly(GOLDEN_LANTERN_2021)


@pytest.mark.parametrize('serie', ['Golden Pumpkin \'18'])
def test_is_golden_pumpkin_2018(serie):
    assert Serie(serie).is_exactly(GOLDEN_PUMPKIN_2018)


@pytest.mark.parametrize('serie', ['Golden Pumpkin \'19'])
def test_is_golden_pumpkin_2019(serie):
    assert Serie(serie).is_exactly(GOLDEN_PUMPKIN_2019)


@pytest.mark.parametrize('serie', ['Golden Pumpkin \'20'])
def test_is_golden_pumpkin_2020(serie):
    assert Serie(serie).is_exactly(GOLDEN_PUMPKIN_2020)


@pytest.mark.parametrize('serie', ['Haunted Hallows'])
def test_is_haunted_hallows_series(serie):
    assert Serie(serie).is_exactly(HAUNTED_HALLOWS)


@pytest.mark.parametrize('serie', ['Ignition'])
def test_is_ignition_series(serie):
    assert Serie(serie).is_exactly(IGNITION)


@pytest.mark.parametrize('serie', ['Impact'])
def test_is_impact_series(serie):
    assert Serie(serie).is_exactly(IMPACT)


@pytest.mark.parametrize('serie', ['Momentum'])
def test_is_momentum_series(serie):
    assert Serie(serie).is_exactly(MOMENTUM)


@pytest.mark.parametrize('serie', ['Nitro'])
def test_is_nitro_series(serie):
    assert Serie(serie).is_exactly(NITRO)


@pytest.mark.parametrize('serie', ['Non Crate'])
def test_is_non_crate(serie):
    assert Serie(serie).is_exactly(NON_CRATE)


@pytest.mark.parametrize('serie', ['Overdrive'])
def test_is_overdrive_series(serie):
    assert Serie(serie).is_exactly(OVERDRIVE)


@pytest.mark.parametrize('serie', ['Player\'s Choice'])
def test_is_players_choice_series(serie):
    assert Serie(serie).is_exactly(PLAYERS_CHOICE)


@pytest.mark.parametrize('serie', ['RLCS Reward'])
def test_is_rlcs_reward_series(serie):
    assert Serie(serie).is_exactly(RLCS_REWARD)


@pytest.mark.parametrize('serie', ['Season 1'])
def test_is_season_1(serie):
    assert Serie(serie).is_exactly(SEASON_1)


@pytest.mark.parametrize('serie', ['Secret Santa'])
def test_is_secret_santa_series(serie):
    assert Serie(serie).is_exactly(SECRET_SANTA)


@pytest.mark.parametrize('serie', ['Spring Fever'])
def test_is_spring_fever_series(serie):
    assert Serie(serie).is_exactly(SPRING_FEVER)


@pytest.mark.parametrize('serie', ['Totally Awesome'])
def test_is_totally_awesome_series(serie):
    assert Serie(serie).is_exactly(TOTALLY_AWESOME)


@pytest.mark.parametrize('serie', ['Triumph'])
def test_is_triumph_series(serie):
    assert Serie(serie).is_exactly(TRIUMPH)


@pytest.mark.parametrize('serie', ['Turbo'])
def test_is_turbo_series(serie):
    assert Serie(serie).is_exactly(TURBO)


@pytest.mark.parametrize('serie', ['Velocity'])
def test_is_velocity_series(serie):
    assert Serie(serie).is_exactly(VELOCITY)


@pytest.mark.parametrize('serie', ['Victory'])
def test_is_victory_series(serie):
    assert Serie(serie).is_exactly(VICTORY)


@pytest.mark.parametrize('serie', ['Vindicator'])
def test_is_vindicator_series(serie):
    assert Serie(serie).is_exactly(VINDICATOR)


@pytest.mark.parametrize('serie', ['Zephyr'])
def test_is_zephyr_series(serie):
    assert Serie(serie).is_exactly(ZEPHYR)


@pytest.mark.parametrize('serie', ['WWE Promo Code'])
def test_is_wwe_promo_code(serie):
    assert Serie(serie).is_exactly(WWE_PROMO_CODE)
