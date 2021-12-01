import pytest

from rl_data_utils.item import Series
from rl_data_utils.item.serie.constants import *
from tests.tests_item.tests_serie.test_serie import inventory_series


@pytest.mark.parametrize('serie', [*inventory_series, *SERIES])
def test_has_serie(serie):
    assert Series(SERIES).has(serie)


@pytest.mark.parametrize('serie', [*inventory_series, *SERIES])
def test_get_respective_serie(serie):
    result = Series(SERIES).get_respective(serie)
    print(result)


@pytest.mark.parametrize('series', [SERIES])
def test_validate_series(series):
    Series(series).validate()


@pytest.mark.parametrize('series', [SERIES])
def test_are_valid_series(series):
    assert Series(series).is_valid()


@pytest.mark.parametrize('series', [SERIES])
def test_has_accelerator_series(series):
    assert Series(series).has_exactly(ACCELERATOR_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_accolade_1_series(series):
    assert Series(series).has_exactly(ACCOLADE_SERIES_1)


@pytest.mark.parametrize('series', [SERIES])
def test_has_accolade_2_series(series):
    assert Series(series).has_exactly(ACCOLADE_SERIES_2)


@pytest.mark.parametrize('series', [SERIES])
def test_has_auriga_series(series):
    assert Series(series).has_exactly(AURIGA_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_beach_blast_series(series):
    assert Series(series).has_exactly(BEACH_BLAST_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_bonus_gift(series):
    assert Series(series).has_exactly(BONUS_GIFT)


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_1_series(series):
    assert Series(series).has_exactly(CHAMPIONS_1_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_2_series(series):
    assert Series(series).has_exactly(CHAMPIONS_2_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_3_series(series):
    assert Series(series).has_exactly(CHAMPIONS_3_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_4_series(series):
    assert Series(series).has_exactly(CHAMPIONS_4_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_elevation_series(series):
    assert Series(series).has_exactly(ELEVATION_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_ferocity_series(series):
    assert Series(series).has_exactly(FEROCITY_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_egg_2018(series):
    assert Series(series).has_exactly(GOLDEN_EGG_2018)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_egg_2019(series):
    assert Series(series).has_exactly(GOLDEN_EGG_2019)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_egg_2020(series):
    assert Series(series).has_exactly(GOLDEN_EGG_2020)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_gift_2018(series):
    assert Series(series).has_exactly(GOLDEN_GIFT_2018)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_gift_2019(series):
    assert Series(series).has_exactly(GOLDEN_GIFT_2019)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_gift_2020(series):
    assert Series(series).has_exactly(GOLDEN_GIFT_2020)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_lantern_2019(series):
    assert Series(series).has_exactly(GOLDEN_LANTERN_2019)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_lantern_2020(series):
    assert Series(series).has_exactly(GOLDEN_LANTERN_2020)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_lantern_2021(series):
    assert Series(series).has_exactly(GOLDEN_LANTERN_2021)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_pumpkin_2018(series):
    assert Series(series).has_exactly(GOLDEN_PUMPKIN_2018)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_pumpkin_2019(series):
    assert Series(series).has_exactly(GOLDEN_PUMPKIN_2019)


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_pumpkin_2020(series):
    assert Series(series).has_exactly(GOLDEN_PUMPKIN_2020)


@pytest.mark.parametrize('series', [SERIES])
def test_has_haunted_hallows_series(series):
    assert Series(series).has_exactly(HAUNTED_HALLOWS_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_ignition_series(series):
    assert Series(series).has_exactly(IGNITION_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_impact_series(series):
    assert Series(series).has_exactly(IMPACT_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_momentum_series(series):
    assert Series(series).has_exactly(MOMENTUM_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_nitro_series(series):
    assert Series(series).has_exactly(NITRO_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_non_crate(series):
    assert Series(series).has_exactly(NON_CRATE)


@pytest.mark.parametrize('series', [SERIES])
def test_has_overdrive_series(series):
    assert Series(series).has_exactly(OVERDRIVE_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_players_choice_series(series):
    assert Series(series).has_exactly(PLAYERS_CHOICE_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_rlcs_reward(series):
    assert Series(series).has_exactly(RLCS_REWARD)


@pytest.mark.parametrize('series', [SERIES])
def test_has_season_1(series):
    assert Series(series).has_exactly(SEASON_1)


@pytest.mark.parametrize('series', [SERIES])
def test_has_secret_santa_series(series):
    assert Series(series).has_exactly(SECRET_SANTA_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_spring_fever_series(series):
    assert Series(series).has_exactly(SPRING_FEVER_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_totally_awesome_series(series):
    assert Series(series).has_exactly(TOTALLY_AWESOME_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_triumph_series(series):
    assert Series(series).has_exactly(TRIUMPH_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_turbo_series(series):
    assert Series(series).has_exactly(TURBO_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_velocity_series(series):
    assert Series(series).has_exactly(VELOCITY_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_victory_series(series):
    assert Series(series).has_exactly(VICTORY_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_vindicator_series(series):
    assert Series(series).has_exactly(VINDICATOR_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_zephyr_series(series):
    assert Series(series).has_exactly(ZEPHYR_SERIES)


@pytest.mark.parametrize('series', [SERIES])
def test_has_wwe_promo_code(series):
    assert Series(series).has_exactly(WWE_PROMO_CODE)
