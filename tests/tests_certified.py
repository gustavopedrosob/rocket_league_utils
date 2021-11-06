from rl_data_utils.item.certified import all_are_certificates
from rl_data_utils.utils.item.certified.constants import CERTIFICATES

inventory_certificates = ['Aviator', 'Acrobat', 'Victor', 'Striker', 'Sniper', 'Scorer', 'Playmaker', 'Guardian',
                          'Paragon', 'Sweeper', 'Turtle', 'Tactician', 'Show-off', 'Juggler', 'Goalkeeper']


def test_is_certified():
    assert all_are_certificates(inventory_certificates)
    assert all_are_certificates(CERTIFICATES)
