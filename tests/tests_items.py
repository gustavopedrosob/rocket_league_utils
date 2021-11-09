from rl_data_utils.item import ABCColor, ABCRarity, ABCType, ABCCertified, ABCName, ABCQuantity
from rl_data_utils.items import ABCColors, ABCRarities, ABCTypes, ABCCertificates, ABCNames, ABCQuantities
from json import load
from pytest import mark


class SampleItem(ABCName, ABCRarity, ABCType, ABCCertified, ABCQuantity, ABCColor):
    def __init__(self, name, color, type_, certified, quantity, rarity):
        self.name = name
        self.color = color
        self.type = type_
        self.certified = certified
        self.rarity = rarity
        self.quantity = quantity

    def set_name(self, name: str):
        self.name = name

    def get_rarity(self):
        return self.rarity

    def set_rarity(self, rarity: str):
        self.rarity = rarity

    def get_type(self):
        return self.type

    def set_type(self, type_: str):
        self.type = type_

    def get_certified(self):
        return self.certified

    def set_certified(self, certified: str):
        self.certified = certified

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        self.quantity = quantity

    def get_color(self):
        return self.color

    def set_color(self, color: str):
        self.color = color

    def get_name(self):
        return self.name


class SampleItems(ABCColors, ABCRarities, ABCTypes, ABCCertificates, ABCNames, ABCQuantities):
    def get_items(self):
        return self.items

    def set_items(self, items):
        self.items = items

    def __init__(self, items: list):
        self.items = items


with open('sample-items.json', 'r') as file:
    json = load(file)

items_json = json['items']
sample_items = SampleItems([SampleItem(**item) for item in items_json])


def test_get_item_by():
    shibuya = sample_items.get_item_by(
        name='Breakout: Shibuya',
        certified='striker',
        type_='decals',
        rarity='rare',
        color='default')
    print(shibuya)


def test_get_items_by():
    octane_items = sample_items.get_items_by(
        name='Octane: Buzz Kill'
    )
    print(octane_items)


def test_get_items_by_string():
    print(sample_items.get_items_by_string('bs'))


def test_get_item_by_string():
    print(sample_items.get_item_by_string('Crimson'))


@mark.skip(reason="We need to fix it, because the function is validating the null arguments.")
def test_get_items_by_item():
    item = SampleItem('Octane: Buzz Kill', "", "", "", "", "")
    print(sample_items.get_items_by_item(item))


@mark.skip(reason="We need to fix it, because the function is validating the null arguments.")
def test_get_item_by_item():
    item = SampleItem('Octane: Buzz Kill', "", "", "", "", "")
    print(sample_items.get_item_by_item(item))
