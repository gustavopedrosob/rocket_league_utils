import pytest

from rl_data_utils.item.attribute.constants import AVIATOR, ACROBAT, GOALKEEPER, GUARDIAN, JUGGLER, PARAGON, PLAYMAKER, \
    SCORER, SHOW_OFF, SNIPER
from rl_data_utils.item.attribute_string.attribute_string import AttributeString
from rl_data_utils.item.attribute.attribute import Certified


@pytest.mark.parametrize('certified_string,certified_expected', [['sTRIKEr', 'Striker']])
def test_get_respective(certified_string, certified_expected):
    result = AttributeString(Certified, certified_string).get().get_respective()
    assert result.value == certified_expected


@pytest.mark.parametrize('certified_string', ['acrobat'])
def test_contains_acrobat(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(ACROBAT)


@pytest.mark.parametrize('certified_string', ['aviator'])
def test_contains_aviator(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(AVIATOR)


@pytest.mark.parametrize('certified_string', ['goalkeeper'])
def test_contains_goalkeeper(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(GOALKEEPER)


@pytest.mark.parametrize('certified_string', ['guardian'])
def test_contains_guardian(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(GUARDIAN)


@pytest.mark.parametrize('certified_string', ['juggler'])
def test_contains_juggler(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(JUGGLER)


@pytest.mark.parametrize('certified_string', ['paragon'])
def test_contains_paragon(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(PARAGON)


@pytest.mark.parametrize('certified_string', ['playmaker'])
def test_contains_playmaker(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(PLAYMAKER)


@pytest.mark.parametrize('certified_string', ['scorer'])
def test_contains_scorer(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(SCORER)


@pytest.mark.parametrize('certified_string', ['show_off'])
def test_contains_show_off(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(SHOW_OFF)


@pytest.mark.parametrize('certified_string', ['sniper'])
def test_contains_sniper(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(SNIPER)


@pytest.mark.parametrize('certified_string', ['acrobat'])
def test_get_exactly_respective_acrobat(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(ACROBAT).get_respective().value == ACROBAT


@pytest.mark.parametrize('certified_string', ['aviator'])
def test_get_exactly_respective_aviator(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(AVIATOR).get_respective().value == AVIATOR


@pytest.mark.parametrize('certified_string', ['goalkeeper'])
def test_get_exactly_respective_goalkeeper(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(
        GOALKEEPER).get_respective().value == GOALKEEPER


@pytest.mark.parametrize('certified_string', ['guardian'])
def test_get_exactly_respective_guardian(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(
        GUARDIAN).get_respective().value == GUARDIAN


@pytest.mark.parametrize('certified_string', ['juggler'])
def test_get_exactly_respective_juggler(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(JUGGLER).get_respective().value == JUGGLER


@pytest.mark.parametrize('certified_string', ['paragon'])
def test_get_exactly_respective_paragon(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(PARAGON).get_respective().value == PARAGON


@pytest.mark.parametrize('certified_string', ['playmaker'])
def test_get_exactly_respective_playmaker(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(
        PLAYMAKER).get_respective().value == PLAYMAKER


@pytest.mark.parametrize('certified_string', ['scorer'])
def test_get_exactly_respective_scorer(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(SCORER).get_respective().value == SCORER


@pytest.mark.parametrize('certified_string', ['show_off'])
def test_get_exactly_respective_show_off(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(
        SHOW_OFF).get_respective().value == SHOW_OFF


@pytest.mark.parametrize('certified_string', ['sniper'])
def test_get_exactly_respective_sniper(certified_string):
    assert AttributeString(Certified, certified_string).get_exactly(SNIPER).get_respective().value == SNIPER
