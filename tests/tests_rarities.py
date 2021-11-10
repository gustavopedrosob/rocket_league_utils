import pytest
from tests_items import sample_items
from rl_data_utils.exceptions import RarityNotExists


def test_get_items_by_rarity_rarity_not_exists():
    with pytest.raises(RarityNotExists):
        sample_items.get_items_by_rarity('')


def test_get_items_by_rarity():
    print(sample_items.get_items_by_rarity("Very rare"))


def test_get_items_by_rarity_regex():
    print(sample_items.get_items_by_rarity_regex('v'))


def test_get_items_by_rarity_equal_to():
    print(sample_items.get_items_by_rarity_equal_to("Very rare"))


def test_get_items_by_rarity_contains():
    print(sample_items.get_items_by_rarity_contains("V"))


def test_get_rarities():
    print(sample_items.get_rarities())


def test_get_items_common():
    print(sample_items.get_items_common())


def test_get_items_legacy():
    print(sample_items.get_items_legacy())


def test_get_items_uncommon():
    print(sample_items.get_items_uncommon())


def test_get_items_rare():
    print(sample_items.get_items_rare())


def test_get_items_very_rare():
    print(sample_items.get_items_very_rare())


def test_get_items_import():
    print(sample_items.get_items_import())


def test_get_items_exotic():
    print(sample_items.get_items_exotic())


def test_get_items_black_market():
    print(sample_items.get_items_black_market())


def test_get_items_limited():
    print(sample_items.get_items_limited())
