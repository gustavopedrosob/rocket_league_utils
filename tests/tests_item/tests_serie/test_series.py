import pytest

from rl_data_utils.item.attribute.constants import ACCELERATOR, ACCOLADE_1, ACCOLADE_2, \
    AURIGA, BEACH_BLAST, BONUS_GIFT, CHAMPIONS_1, CHAMPIONS_2, CHAMPIONS_3, \
    CHAMPIONS_4, ELEVATION, FEROCITY, GOLDEN_EGG_2020, GOLDEN_EGG_2019, GOLDEN_EGG_2018, \
    GOLDEN_GIFT_2020, GOLDEN_GIFT_2019, GOLDEN_GIFT_2018, GOLDEN_LANTERN_2021, GOLDEN_LANTERN_2020, GOLDEN_LANTERN_2019, \
    GOLDEN_PUMPKIN_2020, GOLDEN_PUMPKIN_2019, GOLDEN_PUMPKIN_2018, HAUNTED_HALLOWS, IGNITION, \
    IMPACT, MOMENTUM, NITRO, NON_CRATE, OVERDRIVE, PLAYERS_CHOICE, RLCS_REWARD, \
    SEASON_1, SECRET_SANTA, SPRING_FEVER, TOTALLY_AWESOME, TRIUMPH, TURBO, \
    VELOCITY, VICTORY, VINDICATOR, ZEPHYR, WWE_PROMO_CODE
from rl_data_utils.item.attribute_data.constants import SERIES
from rl_data_utils.item.attribute_data.attribute_data import Series
from rl_data_utils.item.attribute.attribute import Serie
from tests_item.tests_serie.test_serie import inventory_series


@pytest.mark.parametrize('serie', [*inventory_series, *SERIES])
def test_has_serie(serie):
    assert Series.from_str_list(SERIES).has(Serie(serie))


@pytest.mark.parametrize('serie', [*inventory_series, *SERIES])
def test_get_respective_serie(serie):
    result = Series.from_str_list(SERIES).get_respective(Serie(serie))
    print(result)


@pytest.mark.parametrize('series', [SERIES])
def test_has_accelerator_series(series):
    assert Series.from_str_list(series).has(Serie(ACCELERATOR))


@pytest.mark.parametrize('series', [SERIES])
def test_has_accolade_1_series(series):
    assert Series.from_str_list(series).has(Serie(ACCOLADE_1))


@pytest.mark.parametrize('series', [SERIES])
def test_has_accolade_2_series(series):
    assert Series.from_str_list(series).has(Serie(ACCOLADE_2))


@pytest.mark.parametrize('series', [SERIES])
def test_has_auriga_series(series):
    assert Series.from_str_list(series).has(Serie(AURIGA))


@pytest.mark.parametrize('series', [SERIES])
def test_has_beach_blast_series(series):
    assert Series.from_str_list(series).has(Serie(BEACH_BLAST))


@pytest.mark.parametrize('series', [SERIES])
def test_has_bonus_gift(series):
    assert Series.from_str_list(series).has(Serie(BONUS_GIFT))


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_1_series(series):
    assert Series.from_str_list(series).has(Serie(CHAMPIONS_1))


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_2_series(series):
    assert Series.from_str_list(series).has(Serie(CHAMPIONS_2))


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_3_series(series):
    assert Series.from_str_list(series).has(Serie(CHAMPIONS_3))


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_4_series(series):
    assert Series.from_str_list(series).has(Serie(CHAMPIONS_4))


@pytest.mark.parametrize('series', [SERIES])
def test_has_elevation_series(series):
    assert Series.from_str_list(series).has(Serie(ELEVATION))


@pytest.mark.parametrize('series', [SERIES])
def test_has_ferocity_series(series):
    assert Series.from_str_list(series).has(Serie(FEROCITY))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_egg_2018(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_EGG_2018))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_egg_2019(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_EGG_2019))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_egg_2020(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_EGG_2020))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_gift_2018(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_GIFT_2018))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_gift_2019(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_GIFT_2019))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_gift_2020(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_GIFT_2020))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_lantern_2019(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_LANTERN_2019))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_lantern_2020(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_LANTERN_2020))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_lantern_2021(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_LANTERN_2021))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_pumpkin_2018(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_PUMPKIN_2018))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_pumpkin_2019(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_PUMPKIN_2019))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_pumpkin_2020(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_PUMPKIN_2020))


@pytest.mark.parametrize('series', [SERIES])
def test_has_haunted_hallows_series(series):
    assert Series.from_str_list(series).has(Serie(HAUNTED_HALLOWS))


@pytest.mark.parametrize('series', [SERIES])
def test_has_ignition_series(series):
    assert Series.from_str_list(series).has(Serie(IGNITION))


@pytest.mark.parametrize('series', [SERIES])
def test_has_impact_series(series):
    assert Series.from_str_list(series).has(Serie(IMPACT))


@pytest.mark.parametrize('series', [SERIES])
def test_has_momentum_series(series):
    assert Series.from_str_list(series).has(Serie(MOMENTUM))


@pytest.mark.parametrize('series', [SERIES])
def test_has_nitro_series(series):
    assert Series.from_str_list(series).has(Serie(NITRO))


@pytest.mark.parametrize('series', [SERIES])
def test_has_non_crate(series):
    assert Series.from_str_list(series).has(Serie(NON_CRATE))


@pytest.mark.parametrize('series', [SERIES])
def test_has_overdrive_series(series):
    assert Series.from_str_list(series).has(Serie(OVERDRIVE))


@pytest.mark.parametrize('series', [SERIES])
def test_has_players_choice_series(series):
    assert Series.from_str_list(series).has(Serie(PLAYERS_CHOICE))


@pytest.mark.parametrize('series', [SERIES])
def test_has_rlcs_reward(series):
    assert Series.from_str_list(series).has(Serie(RLCS_REWARD))


@pytest.mark.parametrize('series', [SERIES])
def test_has_season_1(series):
    assert Series.from_str_list(series).has(Serie(SEASON_1))


@pytest.mark.parametrize('series', [SERIES])
def test_has_secret_santa_series(series):
    assert Series.from_str_list(series).has(Serie(SECRET_SANTA))


@pytest.mark.parametrize('series', [SERIES])
def test_has_spring_fever_series(series):
    assert Series.from_str_list(series).has(Serie(SPRING_FEVER))


@pytest.mark.parametrize('series', [SERIES])
def test_has_totally_awesome_series(series):
    assert Series.from_str_list(series).has(Serie(TOTALLY_AWESOME))


@pytest.mark.parametrize('series', [SERIES])
def test_has_triumph_series(series):
    assert Series.from_str_list(series).has(Serie(TRIUMPH))


@pytest.mark.parametrize('series', [SERIES])
def test_has_turbo_series(series):
    assert Series.from_str_list(series).has(Serie(TURBO))


@pytest.mark.parametrize('series', [SERIES])
def test_has_velocity_series(series):
    assert Series.from_str_list(series).has(Serie(VELOCITY))


@pytest.mark.parametrize('series', [SERIES])
def test_has_victory_series(series):
    assert Series.from_str_list(series).has(Serie(VICTORY))


@pytest.mark.parametrize('series', [SERIES])
def test_has_vindicator_series(series):
    assert Series.from_str_list(series).has(Serie(VINDICATOR))


@pytest.mark.parametrize('series', [SERIES])
def test_has_zephyr_series(series):
    assert Series.from_str_list(series).has(Serie(ZEPHYR))


@pytest.mark.parametrize('series', [SERIES])
def test_has_wwe_promo_code(series):
    assert Series.from_str_list(series).has(Serie(WWE_PROMO_CODE))
