import pytest

from rl_data_utils.item.attribute.constants import BLACK_MARKET, COMMON, EXOTIC, IMPORT, LEGACY, LIMITED, PREMIUM, RARE, \
    UNCOMMON, VERY_RARE
from rl_data_utils.item.attribute_data.constants import RARITIES
from rl_data_utils.item.attribute.attribute import Rarity
from rl_data_utils.item.attribute_data.attribute_data import Rarities
from tests_item.tests_rarity.test_rarity import inventory_rarities, insider_rarities


@pytest.mark.parametrize("rarity", [*inventory_rarities, *insider_rarities, *RARITIES])
def test_has_rarity(rarity):
    assert Rarities(RARITIES).has(Rarity(rarity))


@pytest.mark.parametrize("rarity", [*inventory_rarities, *insider_rarities, *RARITIES])
def test_get_respective_rarity(rarity):
    result = Rarities(RARITIES).get_respective(Rarity(rarity))
    print(result)


@pytest.mark.parametrize("rarities", [RARITIES])
def test_has_black_market(rarities):
    assert Rarities(rarities).has(BLACK_MARKET)


@pytest.mark.parametrize("rarities", [RARITIES])
def test_has_common(rarities):
    assert Rarities(rarities).has(COMMON)


@pytest.mark.parametrize("rarities", [RARITIES])
def test_has_exotic(rarities):
    assert Rarities(rarities).has(EXOTIC)


@pytest.mark.parametrize("rarities", [RARITIES])
def test_has_import(rarities):
    assert Rarities(rarities).has(IMPORT)


@pytest.mark.parametrize("rarities", [RARITIES])
def test_has_legacy(rarities):
    assert Rarities(rarities).has(LEGACY)


@pytest.mark.parametrize("rarities", [RARITIES])
def test_has_limited(rarities):
    assert Rarities(rarities).has(LIMITED)


@pytest.mark.parametrize("rarities", [RARITIES])
def test_has_premium(rarities):
    assert Rarities(rarities).has(PREMIUM)


@pytest.mark.parametrize("rarities", [RARITIES])
def test_has_rare(rarities):
    assert Rarities(rarities).has(RARE)


@pytest.mark.parametrize("rarities", [RARITIES])
def test_has_uncommon(rarities):
    assert Rarities(rarities).has(UNCOMMON)


@pytest.mark.parametrize("rarities", [RARITIES])
def test_has_very_rare(rarities):
    assert Rarities(rarities).has(VERY_RARE)
