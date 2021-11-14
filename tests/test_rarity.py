import pytest
from rl_data_utils.exceptions import RarityNotExists, InvalidRaritiesList, RarityIsNotInString
from rl_data_utils.utils.item.rarity.contains import contains_black_market, contains_common, contains_exotic, \
    contains_import, contains_legacy, contains_limited, contains_premium, contains_rare, contains_uncommon, \
    contains_very_rare
from rl_data_utils.utils.item.rarity.is_functions import is_black_market, is_common, is_exotic, is_import, is_legacy, \
    is_limited, is_premium, is_rare, is_uncommon, is_very_rare
from rl_data_utils.utils.item.rarity.rarity import all_are_rarities, compare_rarities, contains_rarities, \
    get_rarity_in_string, get_respective_rarity, is_rarity, validate_rarities_list, validate_rarity, \
    has_rarity
from rl_data_utils.utils.item.rarity.constants import RARITIES

insider_rarities = ['Limited', 'Uncommon', 'Rare', 'Very Rare', 'Import', 'Exotic', 'Black Market']

inventory_rarities = ['Import', 'Limited', 'Uncommon', 'Black market', 'Rare', 'Very rare', 'Exotic']

pair_equals = [['black market', 'Black market'], ['common', 'Common'], ['exotic', 'Exotic'], ['import', 'Import'],
               ['limited', 'Limited'], ['premium', 'Premium'], ['rare', 'Rare'], ['uncommon', 'Uncommon'],
               ['very rare', 'Very rare'], ['legacy', 'Legacy']]

samples = [inventory_rarities, insider_rarities, RARITIES]


def test_all_are_rarities():
    for container in samples:
        assert all_are_rarities(container)


def test_compare_rarities():
    for pair in pair_equals:
        assert compare_rarities(*pair)
    with pytest.raises(RarityNotExists):
        compare_rarities('', 'vr')
        compare_rarities('vr', '')


def test_contains_rarities():
    for container in samples:
        for rarity in container:
            assert contains_rarities(rarity)


def test_has_rarity():
    assert has_rarity('vr', inventory_rarities)
    with pytest.raises(RarityNotExists):
        has_rarity('', inventory_rarities)
    with pytest.raises(InvalidRaritiesList):
        has_rarity('vr', [''])


def test_get_rarity_in_string():
    assert get_rarity_in_string('Dingo Titanium White Striker Imported') == 'Imported'
    with pytest.raises(RarityIsNotInString):
        get_rarity_in_string('Dingo Titanium White Striker')


def test_get_respective_rarity():
    for c1, c2 in pair_equals:
        assert get_respective_rarity(c1) == c2
    with pytest.raises(RarityNotExists):
        get_respective_rarity('')


def test_is_rarity():
    for container in samples:
        for rarity in container:
            assert is_rarity(rarity)


def test_validate_rarities_list():
    for container in samples:
        validate_rarities_list(container)
    with pytest.raises(InvalidRaritiesList):
        validate_rarities_list([''])


def test_validate_rarity():
    for container in samples:
        for rarity in container:
            validate_rarity(rarity)


# quando estamos falando do inglês é interessante que adjetivos não usam plural quando estão acompanhados do
# substantivo, então talvez não deveríamos aceitar o plural das raridades.


def test_is_black_market():
    assert is_black_market('black market')
    assert is_black_market('black markets')
    assert is_black_market('bm')
    assert is_black_market('bms')


def test_is_common():
    assert is_common('common')
    assert is_common('commons')


def test_is_exotic():
    assert is_exotic('exotic')
    assert is_exotic('exotics')


def test_is_import():
    assert is_import('import')
    assert is_import('imports')
    assert is_import('imported')
    assert is_import('importeds')


def test_is_legacy():
    assert is_legacy('legacy')


def test_is_limited():
    assert is_limited('limited')
    assert is_limited('limiteds')


def test_is_premium():
    assert is_premium('premium')
    assert is_premium('premiums')


def test_is_rare():
    assert is_rare('rare')
    assert is_rare('rares')


def test_is_uncommon():
    assert is_uncommon('uncommon')
    assert is_uncommon('uncommons')


def test_is_very_rare():
    assert is_very_rare('vr')
    assert is_very_rare('vrs')
    assert is_very_rare('very rare')
    assert is_very_rare('very rares')


def test_contains_black_market():
    assert contains_black_market('black market')
    assert contains_black_market('black markets')
    assert contains_black_market('bm')
    assert contains_black_market('bms')


def test_contains_common():
    assert contains_common('common')
    assert contains_common('commons')


def test_contains_exotic():
    assert contains_exotic('exotic')
    assert contains_exotic('exotics')


def test_contains_import():
    assert contains_import('import')
    assert contains_import('imports')
    assert contains_import('imported')
    assert contains_import('importeds')


def test_contains_legacy():
    assert contains_legacy('legacy')


def test_contains_limited():
    assert contains_limited('limited')
    assert contains_limited('limiteds')


def test_contains_premium():
    assert contains_premium('premium')
    assert contains_premium('premiums')


def test_contains_rare():
    assert contains_rare('rare')
    assert contains_rare('rares')


def test_contains_uncommon():
    assert contains_uncommon('uncommon')
    assert contains_uncommon('uncommons')


def test_contains_very_rare():
    assert contains_very_rare('vr')
    assert contains_very_rare('vrs')
    assert contains_very_rare('very rare')
    assert contains_very_rare('very rares')
