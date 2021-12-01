import pytest

from rl_data_utils.item.certified.certified_string import CertifiedString
from rl_data_utils.item.certified.constants import *


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
