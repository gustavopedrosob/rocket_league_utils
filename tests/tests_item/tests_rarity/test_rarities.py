import pytest

from rl_data_utils.item import Rarities
from rl_data_utils.item.rarity.constants import *
from tests.tests_item.tests_rarity.test_rarity import inventory_rarities, insider_rarities


@pytest.mark.parametrize('color', [*inventory_rarities, *insider_rarities, *RARITIES])
def test_has_color(color):
    assert Rarities(RARITIES).has(color)


@pytest.mark.parametrize('color', [*inventory_rarities, *insider_rarities, *RARITIES])
def test_get_respective_color(color):
    result = Rarities(RARITIES).get_respective(color)
    print(result)


@pytest.mark.parametrize('rarities', [RARITIES])
def test_validate_rarities(rarities):
    Rarities(rarities).validate()


@pytest.mark.parametrize('rarities', [RARITIES])
def test_are_valid_rarities(rarities):
    assert Rarities(rarities).is_valid()


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_black_market(rarities):
    assert Rarities(rarities).has_exactly(BLACK_MARKET)


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_common(rarities):
    assert Rarities(rarities).has_exactly(COMMON)


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_exotic(rarities):
    assert Rarities(rarities).has_exactly(EXOTIC)


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_import(rarities):
    assert Rarities(rarities).has_exactly(IMPORT)


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_legacy(rarities):
    assert Rarities(rarities).has_exactly(LEGACY)


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_limited(rarities):
    assert Rarities(rarities).has_exactly(LIMITED)


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_premium(rarities):
    assert Rarities(rarities).has_exactly(PREMIUM)


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_rare(rarities):
    assert Rarities(rarities).has_exactly(RARE)


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_uncommon(rarities):
    assert Rarities(rarities).has_exactly(UNCOMMON)


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_very_rare(rarities):
    assert Rarities(rarities).has_exactly(VERY_RARE)
