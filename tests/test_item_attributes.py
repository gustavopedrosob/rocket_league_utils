from rl_data_utils.item.item.item import Item
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


item = Item('Octane', 'Car', 'Titanium White')
item_2 = Item('Octane', 'body', 'tw')


def test_validate():
    item.validate()


def test_is_valid():
    assert item.is_valid()


def test_compare_attributes():
    assert item.compare_attributes(color='tw', type='car')


def test_compare_items():
    assert item.compare_items(item_2)
    assert item == item_2


def test_item_attributes_to_dict():
    print(item.item_attributes_to_dict())
