from tests.test_items import sample_items


sample_items = sample_items.get_items_with_valid_serie()


def test_get_items_by_serie_regex():
    print(sample_items.get_items_by_serie_regex("Reward").items)


def test_get_items_by_serie():
    print(sample_items.get_items_by_serie('Accelerator Series').items)


def test_get_items_by_serie_equal_to():
    print(sample_items.get_items_by_serie_equal_to("Season reward").items)


def test_get_items_by_serie_contains():
    print(sample_items.get_items_by_serie_contains("reward").items)


def test_get_series():
    print(sample_items.get_series())


def test_get_items_accelerator_series():
    print(sample_items.get_items_accelerator_series().items)


def test_get_items_beach_blast_series():
    print(sample_items.get_items_beach_blast_series().items)


def test_get_items_bonus_gift():
    print(sample_items.get_items_bonus_gift().items)


def test_get_items_champions_1_series():
    print(sample_items.get_items_champions_1_series().items)


def test_get_items_champions_2_series():
    print(sample_items.get_items_champions_2_series().items)


def test_get_items_champions_3_series():
    print(sample_items.get_items_champions_3_series().items)


def test_get_items_champions_4_series():
    print(sample_items.get_items_champions_4_series().items)


def test_get_items_elevation_series():
    print(sample_items.get_items_elevation_series().items)


def test_get_items_ferocity_series():
    print(sample_items.get_items_ferocity_series().items)


def test_get_items_golden_egg_2018():
    print(sample_items.get_items_golden_egg_2018().items)


def test_get_items_golden_egg_2019():
    print(sample_items.get_items_golden_egg_2019().items)


def test_get_items_golden_egg_2020():
    print(sample_items.get_items_golden_egg_2020().items)


def test_get_items_golden_gift_2018():
    print(sample_items.get_items_golden_gift_2018().items)


def test_get_items_golden_gift_2019():
    print(sample_items.get_items_golden_gift_2019().items)


def test_get_items_golden_gift_2020():
    print(sample_items.get_items_golden_gift_2020().items)


def test_get_items_golden_lantern_2020():
    print(sample_items.get_items_golden_lantern_2020().items)


def test_get_items_golden_lantern_2021():
    print(sample_items.get_items_golden_lantern_2021().items)


def test_get_items_golden_pumpkin_2018():
    print(sample_items.get_items_golden_pumpkin_2018().items)


def test_get_items_golden_pumpkin_2019():
    print(sample_items.get_items_golden_pumpkin_2019().items)


def test_get_items_golden_pumpkin_2020():
    print(sample_items.get_items_golden_pumpkin_2020().items)


def test_get_items_haunted_hallows_series():
    print(sample_items.get_items_haunted_hallows_series().items)


def test_get_items_impact_series():
    print(sample_items.get_items_impact_series().items)


def test_get_items_nitro_series():
    print(sample_items.get_items_nitro_series().items)


def test_get_items_non_crate():
    print(sample_items.get_items_non_crate().items)


def test_get_items_overdrive_series():
    print(sample_items.get_items_overdrive_series().items)


def test_get_items_players_choice_series():
    print(sample_items.get_items_players_choice_series().items)


def test_get_items_secret_santa_series():
    print(sample_items.get_items_secret_santa_series().items)


def test_get_items_spring_fever_series():
    print(sample_items.get_items_spring_fever_series().items)


def test_get_items_totally_awesome_series():
    print(sample_items.get_items_totally_awesome_series().items)


def test_get_items_triumph_series():
    print(sample_items.get_items_triumph_series().items)


def test_get_items_turbo_series():
    print(sample_items.get_items_turbo_series().items)


def test_get_items_velocity_series():
    print(sample_items.get_items_velocity_series().items)


def test_get_items_victory_series():
    print(sample_items.get_items_victory_series().items)


def test_get_items_vindicator_series():
    print(sample_items.get_items_vindicator_series().items)


def test_get_items_zephyr_series():
    print(sample_items.get_items_zephyr_series().items)
