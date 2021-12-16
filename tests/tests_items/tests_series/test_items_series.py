import pytest

from rl_data_utils.item.serie.constants import *
from rl_data_utils.item.serie.serie import Serie
from tests_items.tests_certificates.test_items_certificates import samples_items


@pytest.mark.parametrize('items', samples_items)
def test_get_items_accelerator_series(items):
    print(items.filter_by_attribute(Serie(ACCELERATOR_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_beach_blast_series(items):
    print(items.filter_by_attribute(Serie(BEACH_BLAST_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_bonus_gift(items):
    print(items.filter_by_attribute(Serie(BONUS_GIFT)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_champions_1_series(items):
    items.filter_by_attribute(Serie(CHAMPIONS_1_SERIES))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_champions_2_series(items):
    print(items.filter_by_attribute(Serie(CHAMPIONS_2_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_champions_3_series(items):
    print(items.filter_by_attribute(Serie(CHAMPIONS_3_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_champions_4_series(items):
    print(items.filter_by_attribute(Serie(CHAMPIONS_4_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_elevation_series(items):
    print(items.filter_by_attribute(Serie(ELEVATION_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_ferocity_series(items):
    print(items.filter_by_attribute(Serie(FEROCITY_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_egg_2018(items):
    print(items.filter_by_attribute(Serie(GOLDEN_EGG_2018)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_egg_2019(items):
    print(items.filter_by_attribute(Serie(GOLDEN_EGG_2019)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_egg_2020(items):
    print(items.filter_by_attribute(Serie(GOLDEN_EGG_2020)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_gift_2018(items):
    print(items.filter_by_attribute(Serie(GOLDEN_GIFT_2018)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_gift_2019(items):
    print(items.filter_by_attribute(Serie(GOLDEN_GIFT_2019)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_gift_2020(items):
    print(items.filter_by_attribute(Serie(GOLDEN_GIFT_2020)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_lantern_2020(items):
    print(items.filter_by_attribute(Serie(GOLDEN_LANTERN_2020)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_lantern_2021(items):
    print(items.filter_by_attribute(Serie(GOLDEN_LANTERN_2021)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_pumpkin_2018(items):
    print(items.filter_by_attribute(Serie(GOLDEN_PUMPKIN_2018)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_pumpkin_2019(items):
    print(items.filter_by_attribute(Serie(GOLDEN_PUMPKIN_2019)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_golden_pumpkin_2020(items):
    print(items.filter_by_attribute(Serie(GOLDEN_PUMPKIN_2020)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_haunted_hallows_series(items):
    print(items.filter_by_attribute(Serie(HAUNTED_HALLOWS_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_impact_series(items):
    print(items.filter_by_attribute(Serie(IMPACT_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_nitro_series(items):
    print(items.filter_by_attribute(Serie(NITRO_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_non_crate(items):
    print(items.filter_by_attribute(Serie(NON_CRATE)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_overdrive_series(items):
    print(items.filter_by_attribute(Serie(OVERDRIVE_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_players_choice_series(items):
    print(items.filter_by_attribute(Serie(PLAYERS_CHOICE_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_secret_santa_series(items):
    print(items.filter_by_attribute(Serie(SECRET_SANTA_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_spring_fever_series(items):
    print(items.filter_by_attribute(Serie(SPRING_FEVER_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_totally_awesome_series(items):
    print(items.filter_by_attribute(Serie(TOTALLY_AWESOME_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_triumph_series(items):
    print(items.filter_by_attribute(Serie(TRIUMPH_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_turbo_series(items):
    print(items.filter_by_attribute(Serie(TURBO_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_velocity_series(items):
    print(items.filter_by_attribute(Serie(VELOCITY_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_victory_series(items):
    print(items.filter_by_attribute(Serie(VICTORY_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_vindicator_series(items):
    print(items.filter_by_attribute(Serie(VINDICATOR_SERIES)))


@pytest.mark.parametrize('items', samples_items)
def test_get_items_zephyr_series(items):
    print(items.filter_by_attribute(Serie(ZEPHYR_SERIES)))
