import pytest

from rl_data_utils.item.attribute.constants import BLACK_MARKET, COMMON, EXOTIC, IMPORT, LEGACY, LIMITED, PREMIUM, RARE, \
    UNCOMMON, VERY_RARE
from rl_data_utils.item.attribute_data.constants import RARITIES
from rl_data_utils.item.attribute.attribute import Rarity
from rl_data_utils.item.attribute_data.attribute_data import Rarities
from tests_item.tests_rarity.test_rarity import inventory_rarities, insider_rarities


@pytest.mark.parametrize('rarity', [*inventory_rarities, *insider_rarities, *RARITIES])
def test_has_rarity(rarity):
    assert Rarities.from_str_list(RARITIES).has(Rarity(rarity))


@pytest.mark.parametrize('rarity', [*inventory_rarities, *insider_rarities, *RARITIES])
def test_get_respective_rarity(rarity):
    result = Rarities.from_str_list(RARITIES).get_respective(Rarity(rarity))
    print(result)


@pytest.mark.parametrize('rarities', [RARITIES])
def test_validate_rarities(rarities):
    Rarities.from_str_list(rarities).validate()


@pytest.mark.parametrize('rarities', [RARITIES])
def test_are_valid_rarities(rarities):
    assert Rarities.from_str_list(rarities).is_valid()


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_black_market(rarities):
    assert Rarities.from_str_list(rarities).has(Rarity(BLACK_MARKET))


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_common(rarities):
    assert Rarities.from_str_list(rarities).has(Rarity(COMMON))


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_exotic(rarities):
    assert Rarities.from_str_list(rarities).has(Rarity(EXOTIC))


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_import(rarities):
    assert Rarities.from_str_list(rarities).has(Rarity(IMPORT))


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_legacy(rarities):
    assert Rarities.from_str_list(rarities).has(Rarity(LEGACY))


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_limited(rarities):
    assert Rarities.from_str_list(rarities).has(Rarity(LIMITED))


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_premium(rarities):
    assert Rarities.from_str_list(rarities).has(Rarity(PREMIUM))


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_rare(rarities):
    assert Rarities.from_str_list(rarities).has(Rarity(RARE))


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_uncommon(rarities):
    assert Rarities.from_str_list(rarities).has(Rarity(UNCOMMON))


@pytest.mark.parametrize('rarities', [RARITIES])
def test_has_very_rare(rarities):
    assert Rarities.from_str_list(rarities).has(Rarity(VERY_RARE))
