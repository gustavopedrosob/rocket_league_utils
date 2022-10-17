import pytest

from rl_data_utils.item.attribute.constants import BLACK_MARKET, COMMON, EXOTIC, IMPORT, LEGACY, LIMITED, PREMIUM, RARE, \
    UNCOMMON, VERY_RARE
from rl_data_utils.item.attribute.attribute import Rarity


@pytest.mark.parametrize("rarity", ["bm", "black market"])
def test_contains_black_market(rarity):
    assert Rarity.from_text(rarity, BLACK_MARKET)


@pytest.mark.parametrize("rarity", ["common"])
def test_contains_common(rarity):
    assert Rarity.from_text(rarity, COMMON)


@pytest.mark.parametrize("rarity", ["exotic"])
def test_contains_exotic(rarity):
    assert Rarity.from_text(rarity, EXOTIC)


@pytest.mark.parametrize("rarity", ["import", "imported"])
def test_contains_import(rarity):
    assert Rarity.from_text(rarity, IMPORT)


@pytest.mark.parametrize("rarity", ["legacy"])
def test_contains_legacy(rarity):
    assert Rarity.from_text(rarity, LEGACY)


@pytest.mark.parametrize("rarity", ["limited"])
def test_contains_limited(rarity):
    assert Rarity.from_text(rarity, LIMITED)


@pytest.mark.parametrize("rarity", ["premium"])
def test_contains_premium(rarity):
    assert Rarity.from_text(rarity, PREMIUM)


@pytest.mark.parametrize("rarity", ["rare"])
def test_contains_rare(rarity):
    assert Rarity.from_text(rarity, RARE)


@pytest.mark.parametrize("rarity", ["uncommon"])
def test_contains_uncommon(rarity):
    assert Rarity.from_text(rarity, UNCOMMON)


@pytest.mark.parametrize("rarity", ["very rare", "vr"])
def test_contains_very_rare(rarity):
    assert Rarity.from_text(rarity, VERY_RARE)
