import pytest
from rl_data_utils.item.rarity.constants import *
from rl_data_utils.item.rarity.rarity import Rarity

insider_rarities = ['Limited', 'Uncommon', 'Rare', 'Very Rare', 'Import', 'Exotic', 'Black Market']

inventory_rarities = ['Import', 'Limited', 'Uncommon', 'Black market', 'Rare', 'Very rare', 'Exotic']

pair_equals = [['black market', 'Black market'], ['common', 'Common'], ['exotic', 'Exotic'], ['import', 'Import'],
               ['limited', 'Limited'], ['premium', 'Premium'], ['rare', 'Rare'], ['uncommon', 'Uncommon'],
               ['very rare', 'Very rare'], ['legacy', 'Legacy']]

samples = [*RARITIES, *inventory_rarities, *insider_rarities]


def test_from_random():
    print(Rarity.create_random())


@pytest.mark.parametrize('rarity', samples)
def test_is_rarity(rarity):
    assert Rarity(rarity).is_valid()


@pytest.mark.parametrize('rarity_1,rarity_2', pair_equals)
def test_compare_rarity(rarity_1, rarity_2):
    assert Rarity(rarity_1).compare(Rarity(rarity_2))


@pytest.mark.parametrize('rarity', ['bm', 'black market'])
def test_is_black_market(rarity):
    assert Rarity(rarity).is_exactly(BLACK_MARKET)


@pytest.mark.parametrize('rarity', ['common', 'commons'])
def test_is_common(rarity):
    assert Rarity(rarity).is_exactly(COMMON)


@pytest.mark.parametrize('rarity', ['exotic', 'exotics'])
def test_is_exotic(rarity):
    assert Rarity(rarity).is_exactly(EXOTIC)


@pytest.mark.parametrize('rarity', ['import', 'imported', 'importeds', 'imports'])
def test_is_import(rarity):
    assert Rarity(rarity).is_exactly(IMPORT)


@pytest.mark.parametrize('rarity', ['legacy', 'legacies'])
def test_is_legacy(rarity):
    assert Rarity(rarity).is_exactly(LEGACY)


@pytest.mark.parametrize('rarity', ['limited', 'limiteds'])
def test_is_limited(rarity):
    assert Rarity(rarity).is_exactly(LIMITED)


@pytest.mark.parametrize('rarity', ['premium', 'premiums'])
def test_is_premium(rarity):
    assert Rarity(rarity).is_exactly(PREMIUM)


@pytest.mark.parametrize('rarity', ['rare', 'rares'])
def test_is_rare(rarity):
    assert Rarity(rarity).is_exactly(RARE)


@pytest.mark.parametrize('rarity', ['uncommon', 'uncommons'])
def test_is_uncommon(rarity):
    assert Rarity(rarity).is_exactly(UNCOMMON)


@pytest.mark.parametrize('rarity', ['very rare', 'vr', 'very rares'])
def test_is_very_rare(rarity):
    assert Rarity(rarity).is_exactly(VERY_RARE)
