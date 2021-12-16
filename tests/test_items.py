from json import load
from logging import info

from rl_data_utils.item.item.constants import INDENTIFIER
from rl_data_utils.item.item.item import Item
from rl_data_utils.items.items import Items

with open('sample-inventory-items.json', 'r') as file:
    json = load(file)

items_json = json['items']
inventory_items = Items([Item(**item) for item in items_json])


def test_filter_by_item_indentifier_mode():
    item = Item(True, 'Dingo', 'Car', 'Saffron', 'Import', 'GoalKeeper', 6)
    i = inventory_items.filter_by_item(item, INDENTIFIER)
    info(i.items)


def test_filter_by():
    i = inventory_items.filter_by_item(dict(
        name='Octane: Buzz Kill'
    )
    )
    info(i.items)


def test_filter_by_string():
    info(inventory_items.filter_by_item('Octane: Buzz Kill').items)


def test_filter_by_item():
    item = Item(name='Octane: Buzz Kill')
    info(inventory_items.filter_by_item(item).items)


def test_filter_valid():
    info(inventory_items.filter_valid().items)

