from rl_data_utils.exceptions import CertifiedNotExists, InvalidCertificatesList, CertifiedIsNotInString
from rl_data_utils.utils.item.certified.certified import all_are_certificates, compare_certificates, \
    contains_certificates, has_certified, get_certified_in_string, get_respective_certified, \
    is_certified, validate_certificates_list, validate_certified
from rl_data_utils.utils.item.certified.constants import CERTIFICATES
from rl_data_utils.utils.item.certified.contains import contains_acrobat, contains_aviator, contains_goalkeeper, \
    contains_guardian, contains_juggler, contains_paragon, contains_playmaker, contains_scorer, contains_show_off, \
    contains_sniper, contains_striker, contains_sweeper, contains_tactician, contains_victor, contains_turtle, \
    contains_none
from rl_data_utils.utils.item.certified.is_functions import is_acrobat, is_goalkeeper, is_aviator, is_guardian, \
    is_juggler, is_paragon, is_playmaker, is_scorer, is_show_off, is_sniper, is_striker, is_sweeper, is_tactician, \
    is_turtle, is_victor, is_none
import pytest

inventory_certificates = ['Aviator', 'Acrobat', 'Victor', 'Striker', 'Sniper', 'Scorer', 'Playmaker', 'Guardian',
                          'Paragon', 'Sweeper', 'Turtle', 'Tactician', 'Show-off', 'Juggler', 'Goalkeeper']

pair_equals = [['aviator', 'Aviator'], ['acrobat', 'Acrobat'], ['victor', 'Victor'], ['striker', 'Striker'],
               ['sniper', 'Sniper'], ['scorer', 'Scorer'], ['playmaker', 'Playmaker'], ['guardian', 'Guardian'],
               ['paragon', 'Paragon'], ['sweeper', 'Sweeper'], ['turtle', 'Turtle'], ['tactician', 'Tactician'],
               ['show-off', 'Show-off'], ['juggler', 'Juggler'], ['goalkeeper', 'Goalkeeper']]


samples = [inventory_certificates, CERTIFICATES]


def test_all_are_certificates():
    for container in samples:
        assert all_are_certificates(container)


def test_compare_certificates():
    for pair in pair_equals:
        assert compare_certificates(*pair)
    with pytest.raises(CertifiedNotExists):
        compare_certificates('', 'striker')
        compare_certificates('striker', '')


def test_contains_certificates():
    for container in samples:
        for certified in container:
            assert contains_certificates(certified)


def test_has_certified():
    assert has_certified('striker', inventory_certificates)
    with pytest.raises(CertifiedNotExists):
        has_certified('', inventory_certificates)
    with pytest.raises(InvalidCertificatesList):
        has_certified('striker', [''])


def test_get_certified_in_string():
    assert get_certified_in_string('Dingo Titanium White Striker') == 'Striker'
    with pytest.raises(CertifiedIsNotInString):
        get_certified_in_string('Dingo Titanium White')


def test_get_respective_certified():
    for c1, c2 in pair_equals:
        assert get_respective_certified(c1) == c2
    with pytest.raises(CertifiedNotExists):
        get_respective_certified('')


def test_is_certified():
    for container in samples:
        for certified in container:
            assert is_certified(certified)


def test_validate_certificates_list():
    for container in samples:
        validate_certificates_list(container)
    with pytest.raises(InvalidCertificatesList):
        validate_certificates_list([''])


def test_validate_certified():
    for container in samples:
        for certified in container:
            validate_certified(certified)
    with pytest.raises(CertifiedNotExists):
        validate_certified('')


def test_is_acrobat():
    assert is_acrobat("acrobat")


def test_is_aviator():
    assert is_aviator('aviator')


def test_is_goalkeeper():
    assert is_goalkeeper('goalkeeper')


def test_is_guardian():
    assert is_guardian('guardian')


def test_is_juggler():
    assert is_juggler('juggler')


def test_is_paragon():
    assert is_paragon('paragon')


def test_is_playmaker():
    assert is_playmaker('playmaker')


def test_is_scorer():
    assert is_scorer('scorer')


def test_is_show_off():
    assert is_show_off('showoff')


def test_is_sniper():
    assert is_sniper('sniper')


def test_is_striker():
    assert is_striker('striker')


def test_is_sweeper():
    assert is_sweeper('sweeper')


def test_is_tactician():
    assert is_tactician('tactician')


def test_is_turtle():
    assert is_turtle('turtle')


def test_is_victor():
    assert is_victor('victor')


def test_is_none():
    assert is_none('none')


def test_contains_acrobat():
    assert contains_acrobat("acrobat")


def test_contains_aviator():
    assert contains_aviator('aviator')


def test_contains_goalkeeper():
    assert contains_goalkeeper('goalkeeper')


def test_contains_guardian():
    assert contains_guardian('guardian')


def test_contains_juggler():
    assert contains_juggler('juggler')


def test_contains_paragon():
    assert contains_paragon('paragon')


def test_contains_playmaker():
    assert contains_playmaker('playmaker')


def test_contains_scorer():
    assert contains_scorer('scorer')


def test_contains_show_off():
    assert contains_show_off('showoff')


def test_contains_sniper():
    assert contains_sniper('sniper')


def test_contains_striker():
    assert contains_striker('striker')


def test_contains_sweeper():
    assert contains_sweeper('sweeper')


def test_contains_tactician():
    assert contains_tactician('tactician')


def test_contains_turtle():
    assert contains_turtle('turtle')


def test_contains_victor():
    assert contains_victor('victor')


def test_contains_none():
    assert contains_none('none')
