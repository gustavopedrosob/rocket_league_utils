from rl_data_utils.exceptions import CertifiedNotExists, InvalidCertificatesList, CertifiedIsNotInString
from rl_data_utils.utils.item.certified.certified import all_are_certificates, compare_certified, \
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
from tests.utils.utils_attribute import all_are, compare, contains, has, get_in_string, get_respective, is_, \
    validate_list, validate

inventory_certificates = ['Aviator', 'Acrobat', 'Victor', 'Striker', 'Sniper', 'Scorer', 'Playmaker', 'Guardian',
                          'Paragon', 'Sweeper', 'Turtle', 'Tactician', 'Show-off', 'Juggler', 'Goalkeeper']

pair_equals = [['aviator', 'Aviator'], ['acrobat', 'Acrobat'], ['victor', 'Victor'], ['striker', 'Striker'],
               ['sniper', 'Sniper'], ['scorer', 'Scorer'], ['playmaker', 'Playmaker'], ['guardian', 'Guardian'],
               ['paragon', 'Paragon'], ['sweeper', 'Sweeper'], ['turtle', 'Turtle'], ['tactician', 'Tactician'],
               ['show-off', 'Show-off'], ['juggler', 'Juggler'], ['goalkeeper', 'Goalkeeper']]


samples = [inventory_certificates, CERTIFICATES]


def test_all_are_certificates():
    all_are(all_are_certificates, samples)


def test_compare_certificates():
    compare(compare_certified, pair_equals, CertifiedNotExists)


def test_contains_certificates():
    contains(contains_certificates, samples)


def test_has_certified():
    has(has_certified, inventory_certificates, CertifiedNotExists, InvalidCertificatesList)


def test_get_certified_in_string():
    get_in_string(get_certified_in_string, 'Dingo Titanium White Striker', 'Striker', CertifiedIsNotInString)


def test_get_respective_certified():
    get_respective(get_respective_certified, pair_equals, CertifiedNotExists)


def test_is_certified():
    is_(is_certified, samples)


def test_validate_certificates_list():
    validate_list(validate_certificates_list, samples, InvalidCertificatesList)


def test_validate_certified():
    validate(validate_certified, samples, CertifiedNotExists)


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
