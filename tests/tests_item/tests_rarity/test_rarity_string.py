import pytest

from rl_data_utils.item.rarity.constants import *
from rl_data_utils.item.rarity.rarity import RarityString


@pytest.mark.parametrize('rarity', ['bm', 'black market'])
def test_contains_black_market(rarity):
    assert RarityString(rarity).get_exactly(BLACK_MARKET)


@pytest.mark.parametrize('rarity', ['common', 'commons'])
def test_contains_common(rarity):
    assert RarityString(rarity).get_exactly(COMMON)


@pytest.mark.parametrize('rarity', ['exotic', 'exotics'])
def test_contains_exotic(rarity):
    assert RarityString(rarity).get_exactly(EXOTIC)


@pytest.mark.parametrize('rarity', ['import', 'imported', 'importeds', 'imports'])
def test_contains_import(rarity):
    assert RarityString(rarity).get_exactly(IMPORT)


@pytest.mark.parametrize('rarity', ['legacy', 'legacies'])
def test_contains_legacy(rarity):
    assert RarityString(rarity).get_exactly(LEGACY)


@pytest.mark.parametrize('rarity', ['limited', 'limiteds'])
def test_contains_limited(rarity):
    assert RarityString(rarity).get_exactly(LIMITED)


@pytest.mark.parametrize('rarity', ['premium', 'premiums'])
def test_contains_premium(rarity):
    assert RarityString(rarity).get_exactly(PREMIUM)


@pytest.mark.parametrize('rarity', ['rare', 'rares'])
def test_contains_rare(rarity):
    assert RarityString(rarity).get_exactly(RARE)


@pytest.mark.parametrize('rarity', ['uncommon', 'uncommons'])
def test_contains_uncommon(rarity):
    assert RarityString(rarity).get_exactly(UNCOMMON)


@pytest.mark.parametrize('rarity', ['very rare', 'vr', 'very rares'])
def test_contains_very_rare(rarity):
    assert RarityString(rarity).get_exactly(VERY_RARE)
