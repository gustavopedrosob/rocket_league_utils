import pytest
from rl_data_utils.exceptions import CertifiedNotExists
from test_items import sample_items


sample_items = sample_items.get_items_with_valid_certified()


def test_get_items_by_certified_certified_not_exists():
    with pytest.raises(CertifiedNotExists):
        sample_items.get_items_by_certified("")


def test_get_items_by_certified():
    print(sample_items.get_items_by_certified("striker").items)


def test_get_items_by_certified_regex():
    print(sample_items.get_items_by_certified_regex('s').items)


def test_get_items_by_certified_equal_to():
    print(sample_items.get_items_by_certified_equal_to("Striker").items)


def test_get_items_by_certified_contains():
    print(sample_items.get_items_by_certified_contains("S").items)


def test_get_certificates():
    print(sample_items.get_certificates())


def test_get_items_aviator():
    print(sample_items.get_items_aviator().items)


def test_get_items_acrobat():
    print(sample_items.get_items_acrobat().items)


def test_get_items_victor():
    print(sample_items.get_items_victor().items)


def test_get_items_striker():
    print(sample_items.get_items_striker().items)


def test_get_items_sniper():
    print(sample_items.get_items_sniper().items)


def test_get_items_scorer():
    print(sample_items.get_items_scorer().items)


def test_get_items_playmaker():
    print(sample_items.get_items_playmaker().items)


def test_get_items_guardian():
    print(sample_items.get_items_guardian().items)


def test_get_items_paragon():
    print(sample_items.get_items_paragon().items)


def test_get_items_sweeper():
    print(sample_items.get_items_sweeper().items)


def test_get_items_turtle():
    print(sample_items.get_items_turtle().items)


def test_get_items_tactician():
    print(sample_items.get_items_tactician().items)


def test_get_items_showoff():
    print(sample_items.get_items_showoff().items)


def test_get_items_juggler():
    print(sample_items.get_items_juggler().items)


def test_get_items_goalkeeper():
    print(sample_items.get_items_goalkeeper().items)
