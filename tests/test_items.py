from json import load
from rl_data_utils.item.item.item import Item
from rl_data_utils.items.items import Items

with open('sample-inventory-items.json', 'r') as file:
    json = load(file)

items_json = json['items']
inventory_items = Items([Item(**item) for item in items_json])


def test_filter_by():
    i = inventory_items.filter_by(dict(
        name='Octane: Buzz Kill'
    )
    )
    print(i.items)


def test_filter_by_string():
    print(inventory_items.filter_by('Octane: Buzz Kill').items)


def test_filter_by_item():
    item = Item(name='Octane: Buzz Kill')
    print(inventory_items.filter_by(item).items)


def test_filter_valid():
    print(inventory_items.filter_valid().items)

