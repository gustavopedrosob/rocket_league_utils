import pytest
from rl_data_utils.exceptions import ItemNotFound
from rl_data_utils.item import ABCColor, ABCRarity, ABCType, ABCCertified, ABCName, ABCQuantity
from rl_data_utils.item.serie.serie import ABCSerie
from rl_data_utils.item.tradable.tradable import ABCTradable
from rl_data_utils.items import Colors, Rarities, Types, Certificates, Names, Quantities
from rl_data_utils.items.series.series import Series
from rl_data_utils.items.tradables.tradables import Tradables
from json import load


class SampleItem(ABCName, ABCRarity, ABCType, ABCCertified, ABCQuantity, ABCColor, ABCTradable, ABCSerie):
    def __init__(self, name, color, type_, certified, quantity, rarity, tradable, serie):
        self.name = name
        self.color = color
        self.type = type_
        self.certified = certified
        self.rarity = rarity
        self.quantity = quantity
        self.tradable = tradable
        self.serie = serie

    def get_tradable(self) -> bool:
        return self.tradable

    def get_serie(self) -> str:
        return self.serie

    def get_rarity(self):
        return self.rarity

    def get_type(self):
        return self.type

    def get_certified(self):
        return self.certified

    def get_quantity(self) -> int:
        return self.quantity

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name


class SampleItems(Colors, Rarities, Types, Certificates, Names, Quantities, Tradables, Series):
    pass


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
    print(octane_items.items)


def test_get_items_by_string():
    print(sample_items.get_items_by_string('bs').items)


def test_get_item_by_string():
    print(sample_items.get_item_by_string('Crimson'))


def test_get_items_by_item():
    item = SampleItem('Octane: Buzz Kill', "", "", "", "", "", True, "")
    print(sample_items.get_items_by_item(item).items)


def test_get_item_by_item():
    item = SampleItem('Octane: Buzz Kill', "", "", "", "", "", True, "")
    print(sample_items.get_item_by_item(item))


def test_get_item_by_item_item_not_found():
    with pytest.raises(ItemNotFound):
        sample_items.get_item_by(name='')


def test_get_items_valid():
    print(sample_items.get_items_valid().items)
