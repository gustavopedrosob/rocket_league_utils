from json import load

from rl_data_utils.item.attribute.attribute import Archived, Certified, Color, Name, Quantity, Rarity, Serie, Slot, \
    Tradable
from rl_data_utils.item.item.constants import INDENTIFIER
from rl_data_utils.item.item.item import Item
from rl_data_utils.items.items import Items

with open('sample-inventory-items.json', 'r') as file:
    json = load(file)

items_json = json['items']
inventory_items = Items([Item(color=Color(item['color']),
                              rarity=Rarity(item['rarity']),
                              slot=Slot(item['slot']),
                              certified=Certified(item['certified']),
                              name=Name(item['name']),
                              quantity=Quantity(item['quantity']),
                              tradable=Tradable(item['tradable']),
                              serie=Serie(item['serie'])) for item in items_json])


def test_filter_by_item_indentifier_mode():
    item = Item(Archived(True), Name('Dingo'), Slot('Car'), Color('Saffron'), Rarity('Import'), Certified('GoalKeeper'),
                Quantity(6))
    i = inventory_items.filter_by_item(item, INDENTIFIER)
    print(i.items)


def test_filter_by():
    i = inventory_items.filter_by_item(Item(
        name=Name('Octane: Buzz Kill')
    ))
    print(i.items)


def test_filter_by_string():
    print(inventory_items.filter_by_item(Item.from_str('Octane: Buzz Kill')).items)


def test_filter_by_item():
    item = Item(name=Name('Octane: Buzz Kill'))
    print(inventory_items.filter_by_item(item).items)


def test_filter_valid():
    print(inventory_items.filter_valid().items)

