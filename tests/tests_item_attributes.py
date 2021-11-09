from rl_data_utils.utils.item_attributes.item_attributes import get_attributes_in_string, \
    get_respective_attributes_in_string, validate_attributes, get_repr


def test_get_attributes_in_string():
    assert get_attributes_in_string('Dingo Titanium White Striker Imported') ==\
           dict(name='Dingo', color='Titanium White', certified='Striker', rarity='Imported')


def test_get_respective_attributes_in_string():
    assert get_respective_attributes_in_string('dingo titanium white striker imported') ==\
           dict(name='dingo', color='Titanium White', certified='Striker', rarity='Import')


def test_validate_attributes():
    validate_attributes(name='Dingo', color='Titanium White', certified='Striker', rarity='Imported')


def test_get_repr():
    assert get_repr(name='Dingo', color='Titanium White', certified='Striker', rarity='Imported') ==\
           'Titanium White Imported Striker Dingo'
