import pytest

from rl_data_utils.item.attribute.constants import AVIATOR, ACROBAT, GOALKEEPER, GUARDIAN, JUGGLER, PARAGON, PLAYMAKER,\
    SCORER, SHOW_OFF, SNIPER
from rl_data_utils.item.attribute.attribute import Certified


@pytest.mark.parametrize('certified_string,certified_expected', [['sTRIKEr', 'Striker']])
def test_get_respective(certified_string, certified_expected):
    assert Certified.from_text(certified_string).get_representative() == certified_expected


@pytest.mark.parametrize('certified_string', ['acrobat'])
def test_contains_acrobat(certified_string):
    assert Certified.from_text(certified_string, ACROBAT)


@pytest.mark.parametrize('certified_string', ['aviator'])
def test_contains_aviator(certified_string):
    assert Certified.from_text(certified_string, AVIATOR)


@pytest.mark.parametrize('certified_string', ['goalkeeper'])
def test_contains_goalkeeper(certified_string):
    assert Certified.from_text(certified_string, GOALKEEPER)


@pytest.mark.parametrize('certified_string', ['guardian'])
def test_contains_guardian(certified_string):
    assert Certified.from_text(certified_string, GUARDIAN)


@pytest.mark.parametrize('certified_string', ['juggler'])
def test_contains_juggler(certified_string):
    assert Certified.from_text(certified_string, JUGGLER)


@pytest.mark.parametrize('certified_string', ['paragon'])
def test_contains_paragon(certified_string):
    assert Certified.from_text(certified_string, PARAGON)


@pytest.mark.parametrize('certified_string', ['playmaker'])
def test_contains_playmaker(certified_string):
    assert Certified.from_text(certified_string, PLAYMAKER)


@pytest.mark.parametrize('certified_string', ['scorer'])
def test_contains_scorer(certified_string):
    assert Certified.from_text(certified_string, SCORER)


@pytest.mark.parametrize('certified_string', ['show_off'])
def test_contains_show_off(certified_string):
    assert Certified.from_text(certified_string, SHOW_OFF)


@pytest.mark.parametrize('certified_string', ['sniper'])
def test_contains_sniper(certified_string):
    assert Certified.from_text(certified_string, SNIPER)


@pytest.mark.parametrize('certified_string', ['acrobat'])
def test_get_exactly_respective_acrobat(certified_string):
    assert Certified.from_text(certified_string, ACROBAT).get_representative() == ACROBAT


@pytest.mark.parametrize('certified_string', ['aviator'])
def test_get_exactly_respective_aviator(certified_string):
    assert Certified.from_text(certified_string, AVIATOR).get_representative() == AVIATOR


@pytest.mark.parametrize('certified_string', ['goalkeeper'])
def test_get_exactly_respective_goalkeeper(certified_string):
    assert Certified.from_text(certified_string, GOALKEEPER).get_representative() == GOALKEEPER


@pytest.mark.parametrize('certified_string', ['guardian'])
def test_get_exactly_respective_guardian(certified_string):
    assert Certified.from_text(certified_string, GUARDIAN).get_representative() == GUARDIAN


@pytest.mark.parametrize('certified_string', ['juggler'])
def test_get_exactly_respective_juggler(certified_string):
    assert Certified.from_text(certified_string, JUGGLER).get_representative() == JUGGLER


@pytest.mark.parametrize('certified_string', ['paragon'])
def test_get_exactly_respective_paragon(certified_string):
    assert Certified.from_text(certified_string, PARAGON).get_representative() == PARAGON


@pytest.mark.parametrize('certified_string', ['playmaker'])
def test_get_exactly_respective_playmaker(certified_string):
    assert Certified.from_text(certified_string, PLAYMAKER).get_representative() == PLAYMAKER


@pytest.mark.parametrize('certified_string', ['scorer'])
def test_get_exactly_respective_scorer(certified_string):
    assert Certified.from_text(certified_string, SCORER).get_representative() == SCORER


@pytest.mark.parametrize('certified_string', ['show_off'])
def test_get_exactly_respective_show_off(certified_string):
    assert Certified.from_text(certified_string, SHOW_OFF).get_representative() == SHOW_OFF


@pytest.mark.parametrize('certified_string', ['sniper'])
def test_get_exactly_respective_sniper(certified_string):
    assert Certified.from_text(certified_string, SNIPER).get_representative() == SNIPER
