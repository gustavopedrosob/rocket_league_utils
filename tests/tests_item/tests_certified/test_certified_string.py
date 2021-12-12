import pytest

from rl_data_utils.item.certified.certified import CertifiedString
from rl_data_utils.item.certified.constants import *


@pytest.mark.parametrize('certified_string,certified_expected', [['sTRIKEr', 'Striker']])
def test_get_respective(certified_string, certified_expected):
    assert CertifiedString(certified_string).get_respective().attribute == certified_expected


@pytest.mark.parametrize('certified_string', ['acrobat'])
def test_contains_acrobat(certified_string):
    assert CertifiedString(certified_string).get_exactly(ACROBAT)


@pytest.mark.parametrize('certified_string', ['aviator'])
def test_contains_aviator(certified_string):
    assert CertifiedString(certified_string).get_exactly(AVIATOR)


@pytest.mark.parametrize('certified_string', ['goalkeeper'])
def test_contains_goalkeeper(certified_string):
    assert CertifiedString(certified_string).get_exactly(GOALKEEPER)


@pytest.mark.parametrize('certified_string', ['guardian'])
def test_contains_guardian(certified_string):
    assert CertifiedString(certified_string).get_exactly(GUARDIAN)


@pytest.mark.parametrize('certified_string', ['juggler'])
def test_contains_juggler(certified_string):
    assert CertifiedString(certified_string).get_exactly(JUGGLER)


@pytest.mark.parametrize('certified_string', ['paragon'])
def test_contains_paragon(certified_string):
    assert CertifiedString(certified_string).get_exactly(PARAGON)


@pytest.mark.parametrize('certified_string', ['playmaker'])
def test_contains_playmaker(certified_string):
    assert CertifiedString(certified_string).get_exactly(PLAYMAKER)


@pytest.mark.parametrize('certified_string', ['scorer'])
def test_contains_scorer(certified_string):
    assert CertifiedString(certified_string).get_exactly(SCORER)


@pytest.mark.parametrize('certified_string', ['show_off'])
def test_contains_show_off(certified_string):
    assert CertifiedString(certified_string).get_exactly(SHOW_OFF)


@pytest.mark.parametrize('certified_string', ['sniper'])
def test_contains_sniper(certified_string):
    assert CertifiedString(certified_string).get_exactly(SNIPER)


@pytest.mark.parametrize('certified_string', ['acrobat'])
def test_get_exactly_respective_acrobat(certified_string):
    assert CertifiedString(certified_string).get_exactly_respective(ACROBAT).attribute == ACROBAT


@pytest.mark.parametrize('certified_string', ['aviator'])
def test_get_exactly_respective_aviator(certified_string):
    assert CertifiedString(certified_string).get_exactly_respective(AVIATOR).attribute == AVIATOR


@pytest.mark.parametrize('certified_string', ['goalkeeper'])
def test_get_exactly_respective_goalkeeper(certified_string):
    assert CertifiedString(certified_string).get_exactly_respective(GOALKEEPER).attribute == GOALKEEPER


@pytest.mark.parametrize('certified_string', ['guardian'])
def test_get_exactly_respective_guardian(certified_string):
    assert CertifiedString(certified_string).get_exactly_respective(GUARDIAN).attribute == GUARDIAN


@pytest.mark.parametrize('certified_string', ['juggler'])
def test_get_exactly_respective_juggler(certified_string):
    assert CertifiedString(certified_string).get_exactly_respective(JUGGLER).attribute == JUGGLER


@pytest.mark.parametrize('certified_string', ['paragon'])
def test_get_exactly_respective_paragon(certified_string):
    assert CertifiedString(certified_string).get_exactly_respective(PARAGON).attribute == PARAGON


@pytest.mark.parametrize('certified_string', ['playmaker'])
def test_get_exactly_respective_playmaker(certified_string):
    assert CertifiedString(certified_string).get_exactly_respective(PLAYMAKER).attribute == PLAYMAKER


@pytest.mark.parametrize('certified_string', ['scorer'])
def test_get_exactly_respective_scorer(certified_string):
    assert CertifiedString(certified_string).get_exactly_respective(SCORER).attribute == SCORER


@pytest.mark.parametrize('certified_string', ['show_off'])
def test_get_exactly_respective_show_off(certified_string):
    assert CertifiedString(certified_string).get_exactly_respective(SHOW_OFF).attribute == SHOW_OFF


@pytest.mark.parametrize('certified_string', ['sniper'])
def test_get_exactly_respective_sniper(certified_string):
    assert CertifiedString(certified_string).get_exactly_respective(SNIPER).attribute == SNIPER
