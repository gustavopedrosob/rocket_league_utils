import pytest

from rl_data_utils.item.attribute.constants import ACCELERATOR, ACCOLADE_1, ACCOLADE_2, \
    AURIGA, BEACH_BLAST, BONUS_GIFT, CHAMPIONS_1, CHAMPIONS_2, CHAMPIONS_3, \
    CHAMPIONS_4, ELEVATION, FEROCITY, GOLDEN_EGG_2020, GOLDEN_EGG_2019, GOLDEN_EGG_2018, \
    GOLDEN_GIFT_2020, GOLDEN_GIFT_2019, GOLDEN_GIFT_2018, GOLDEN_LANTERN_2021, GOLDEN_LANTERN_2020,\
    GOLDEN_LANTERN_2019, GOLDEN_PUMPKIN_2020, GOLDEN_PUMPKIN_2019, GOLDEN_PUMPKIN_2018, HAUNTED_HALLOWS, IGNITION, \
    IMPACT, MOMENTUM, NITRO, NON_CRATE, OVERDRIVE, PLAYERS_CHOICE, RLCS_REWARD, \
    SEASON_1, SECRET_SANTA, SPRING_FEVER, TOTALLY_AWESOME, TRIUMPH, TURBO, \
    VELOCITY, VICTORY, VINDICATOR, ZEPHYR, WWE_PROMO_CODE
from rl_data_utils.item.attribute_data.constants import SERIES
from rl_data_utils.item.attribute_data.attribute_data import Series
from rl_data_utils.item.attribute.attribute import Serie
from tests_item.tests_serie.test_serie import inventory_series


@pytest.mark.parametrize("serie", [*inventory_series, *SERIES])
def test_has_serie(serie):
    assert Series(SERIES).has(Serie(serie))


@pytest.mark.parametrize("serie", [*inventory_series, *SERIES])
def test_get_respective_serie(serie):
    result = Series(SERIES).get_respective(Serie(serie))
    print(result)


@pytest.mark.parametrize("series", [SERIES])
def test_has_accelerator_series(series):
    assert Series(series).has(ACCELERATOR)


@pytest.mark.parametrize("series", [SERIES])
def test_has_accolade_1_series(series):
    assert Series(series).has(ACCOLADE_1)


@pytest.mark.parametrize("series", [SERIES])
def test_has_accolade_2_series(series):
    assert Series(series).has(ACCOLADE_2)


@pytest.mark.parametrize("series", [SERIES])
def test_has_auriga_series(series):
    assert Series(series).has(AURIGA)


@pytest.mark.parametrize("series", [SERIES])
def test_has_beach_blast_series(series):
    assert Series(series).has(BEACH_BLAST)


@pytest.mark.parametrize("series", [SERIES])
def test_has_bonus_gift(series):
    assert Series(series).has(BONUS_GIFT)


@pytest.mark.parametrize("series", [SERIES])
def test_has_champions_1_series(series):
    assert Series(series).has(CHAMPIONS_1)


@pytest.mark.parametrize("series", [SERIES])
def test_has_champions_2_series(series):
    assert Series(series).has(CHAMPIONS_2)


@pytest.mark.parametrize("series", [SERIES])
def test_has_champions_3_series(series):
    assert Series(series).has(CHAMPIONS_3)


@pytest.mark.parametrize("series", [SERIES])
def test_has_champions_4_series(series):
    assert Series(series).has(CHAMPIONS_4)


@pytest.mark.parametrize("series", [SERIES])
def test_has_elevation_series(series):
    assert Series(series).has(ELEVATION)


@pytest.mark.parametrize("series", [SERIES])
def test_has_ferocity_series(series):
    assert Series(series).has(FEROCITY)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_egg_2018(series):
    assert Series(series).has(GOLDEN_EGG_2018)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_egg_2019(series):
    assert Series(series).has(GOLDEN_EGG_2019)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_egg_2020(series):
    assert Series(series).has(GOLDEN_EGG_2020)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_gift_2018(series):
    assert Series(series).has(GOLDEN_GIFT_2018)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_gift_2019(series):
    assert Series(series).has(GOLDEN_GIFT_2019)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_gift_2020(series):
    assert Series(series).has(GOLDEN_GIFT_2020)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_lantern_2019(series):
    assert Series(series).has(GOLDEN_LANTERN_2019)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_lantern_2020(series):
    assert Series(series).has(GOLDEN_LANTERN_2020)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_lantern_2021(series):
    assert Series(series).has(GOLDEN_LANTERN_2021)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_pumpkin_2018(series):
    assert Series(series).has(GOLDEN_PUMPKIN_2018)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_pumpkin_2019(series):
    assert Series(series).has(GOLDEN_PUMPKIN_2019)


@pytest.mark.parametrize("series", [SERIES])
def test_has_golden_pumpkin_2020(series):
    assert Series(series).has(GOLDEN_PUMPKIN_2020)


@pytest.mark.parametrize("series", [SERIES])
def test_has_haunted_hallows_series(series):
    assert Series(series).has(HAUNTED_HALLOWS)


@pytest.mark.parametrize("series", [SERIES])
def test_has_ignition_series(series):
    assert Series(series).has(IGNITION)


@pytest.mark.parametrize("series", [SERIES])
def test_has_impact_series(series):
    assert Series(series).has(IMPACT)


@pytest.mark.parametrize("series", [SERIES])
def test_has_momentum_series(series):
    assert Series(series).has(MOMENTUM)


@pytest.mark.parametrize("series", [SERIES])
def test_has_nitro_series(series):
    assert Series(series).has(NITRO)


@pytest.mark.parametrize("series", [SERIES])
def test_has_non_crate(series):
    assert Series(series).has(NON_CRATE)


@pytest.mark.parametrize("series", [SERIES])
def test_has_overdrive_series(series):
    assert Series(series).has(OVERDRIVE)


@pytest.mark.parametrize("series", [SERIES])
def test_has_players_choice_series(series):
    assert Series(series).has(PLAYERS_CHOICE)


@pytest.mark.parametrize("series", [SERIES])
def test_has_rlcs_reward(series):
    assert Series(series).has(RLCS_REWARD)


@pytest.mark.parametrize("series", [SERIES])
def test_has_season_1(series):
    assert Series(series).has(SEASON_1)


@pytest.mark.parametrize("series", [SERIES])
def test_has_secret_santa_series(series):
    assert Series(series).has(SECRET_SANTA)


@pytest.mark.parametrize("series", [SERIES])
def test_has_spring_fever_series(series):
    assert Series(series).has(SPRING_FEVER)


@pytest.mark.parametrize("series", [SERIES])
def test_has_totally_awesome_series(series):
    assert Series(series).has(TOTALLY_AWESOME)


@pytest.mark.parametrize("series", [SERIES])
def test_has_triumph_series(series):
    assert Series(series).has(TRIUMPH)


@pytest.mark.parametrize("series", [SERIES])
def test_has_turbo_series(series):
    assert Series(series).has(TURBO)


@pytest.mark.parametrize("series", [SERIES])
def test_has_velocity_series(series):
    assert Series(series).has(VELOCITY)


@pytest.mark.parametrize("series", [SERIES])
def test_has_victory_series(series):
    assert Series(series).has(VICTORY)


@pytest.mark.parametrize("series", [SERIES])
def test_has_vindicator_series(series):
    assert Series(series).has(VINDICATOR)


@pytest.mark.parametrize("series", [SERIES])
def test_has_zephyr_series(series):
    assert Series(series).has(ZEPHYR)


@pytest.mark.parametrize("series", [SERIES])
def test_has_wwe_promo_code(series):
    assert Series(series).has(WWE_PROMO_CODE)
