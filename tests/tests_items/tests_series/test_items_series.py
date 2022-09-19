import pytest

from rl_data_utils.item.attribute.preset import ACCELERATOR_SERIES, BEACH_BLAST_SERIES, BONUS_GIFT, \
    CHAMPIONS_1_SERIES, CHAMPIONS_2_SERIES, CHAMPIONS_3_SERIES, CHAMPIONS_4_SERIES, ELEVATION_SERIES, FEROCITY_SERIES, \
    GOLDEN_EGG_2020, GOLDEN_EGG_2019, GOLDEN_EGG_2018, GOLDEN_GIFT_2020, GOLDEN_GIFT_2019, GOLDEN_GIFT_2018, \
    GOLDEN_LANTERN_2021, GOLDEN_LANTERN_2020, GOLDEN_PUMPKIN_2020, GOLDEN_PUMPKIN_2019, GOLDEN_PUMPKIN_2018, \
    HAUNTED_HALLOWS_SERIES, IMPACT_SERIES, NITRO_SERIES, NON_CRATE, OVERDRIVE_SERIES, PLAYERS_CHOICE_SERIES, \
    SECRET_SANTA_SERIES, SPRING_FEVER_SERIES, TOTALLY_AWESOME_SERIES, TRIUMPH_SERIES, TURBO_SERIES, VELOCITY_SERIES, \
    VICTORY_SERIES, VINDICATOR_SERIES, ZEPHYR_SERIES
from tests_items.tests_certificates.test_items_certificates import samples_items


@pytest.mark.parametrize('items', samples_items)
def test_get_items_accelerator_series(items):
    print(items.filter_by_attribute(ACCELERATOR_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_beach_blast_series(items):
    print(items.filter_by_attribute(BEACH_BLAST_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_bonus_gift(items):
    print(items.filter_by_attribute(BONUS_GIFT))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_champions_1_series(items):
    print(items.filter_by_attribute(CHAMPIONS_1_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_champions_2_series(items):
    print(items.filter_by_attribute(CHAMPIONS_2_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_champions_3_series(items):
    print(items.filter_by_attribute(CHAMPIONS_3_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_champions_4_series(items):
    print(items.filter_by_attribute(CHAMPIONS_4_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_elevation_series(items):
    print(items.filter_by_attribute(ELEVATION_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_ferocity_series(items):
    print(items.filter_by_attribute(FEROCITY_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_egg_2018(items):
    print(items.filter_by_attribute(GOLDEN_EGG_2018))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_egg_2019(items):
    print(items.filter_by_attribute(GOLDEN_EGG_2019))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_egg_2020(items):
    print(items.filter_by_attribute(GOLDEN_EGG_2020))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_gift_2018(items):
    print(items.filter_by_attribute(GOLDEN_GIFT_2018))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_gift_2019(items):
    print(items.filter_by_attribute(GOLDEN_GIFT_2019))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_gift_2020(items):
    print(items.filter_by_attribute(GOLDEN_GIFT_2020))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_lantern_2020(items):
    print(items.filter_by_attribute(GOLDEN_LANTERN_2020))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_lantern_2021(items):
    print(items.filter_by_attribute(GOLDEN_LANTERN_2021))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_pumpkin_2018(items):
    print(items.filter_by_attribute(GOLDEN_PUMPKIN_2018))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_pumpkin_2019(items):
    print(items.filter_by_attribute(GOLDEN_PUMPKIN_2019))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_pumpkin_2020(items):
    print(items.filter_by_attribute(GOLDEN_PUMPKIN_2020))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_haunted_hallows_series(items):
    print(items.filter_by_attribute(HAUNTED_HALLOWS_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_impact_series(items):
    print(items.filter_by_attribute(IMPACT_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_nitro_series(items):
    print(items.filter_by_attribute(NITRO_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_non_crate(items):
    print(items.filter_by_attribute(NON_CRATE))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_overdrive_series(items):
    print(items.filter_by_attribute(OVERDRIVE_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_players_choice_series(items):
    print(items.filter_by_attribute(PLAYERS_CHOICE_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_secret_santa_series(items):
    print(items.filter_by_attribute(SECRET_SANTA_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_spring_fever_series(items):
    print(items.filter_by_attribute(SPRING_FEVER_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_totally_awesome_series(items):
    print(items.filter_by_attribute(TOTALLY_AWESOME_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_triumph_series(items):
    print(items.filter_by_attribute(TRIUMPH_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_turbo_series(items):
    print(items.filter_by_attribute(TURBO_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_velocity_series(items):
    print(items.filter_by_attribute(VELOCITY_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_victory_series(items):
    print(items.filter_by_attribute(VICTORY_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_vindicator_series(items):
    print(items.filter_by_attribute(VINDICATOR_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_zephyr_series(items):
    print(items.filter_by_attribute(ZEPHYR_SERIES))
