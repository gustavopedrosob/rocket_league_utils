from rl_data_utils.item.item.item_data import ABCItemData
from rl_data_utils.items import ABCListColors, ABCRarities, ABCTypes, ABCNames
from rl_data_utils.item import ABCListColor, ABCRarity, ABCType, ABCName, ABCColor
from json import load
from rl_data_utils.utils.item.color.is_functions import is_default
from pytest import mark


class SampleItemData(ABCItemData, ABCListColor, ABCRarity, ABCType, ABCName):
    def __init__(self, id, name, rarity, platform, icon, type, icon_url, colors=[], customizable=False, unit=''):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.platform = platform
        self.icon = icon
        self.type = type
        self.icon_url = icon_url
        self.colors = colors
        self.customizable = customizable
        self.unit = unit

    def get_list_color(self) -> list[str]:
        result = []
        for color in self.colors:
            result.append(color['name'])
        return result

    def get_rarity(self):
        return self.rarity

    def set_rarity(self, rarity: str):
        self.rarity = rarity

    def get_type(self):
        return self.type

    def set_type(self, type_: str):
        self.type = type_

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_color_info(self, color: str) -> dict:
        for data in self.colors:
            if data['name'] == color:
                return data

    def to_item(self, **kwargs):
        color = kwargs.get('color')
        if color and not is_default(color):
            data_color = self.get_color_info(color)
            icon = data_color['icon']
            icon_url = data_color['icon_url']
        else:
            color = "Default"
            icon = self.icon
            icon_url = self.icon_url
        return SampleItem(self.id, self.name, self.rarity, self.platform, icon, self.type, icon_url, color,
                          self.customizable, self.unit)


class SampleItem(ABCRarity, ABCType, ABCName, ABCColor):
    def __init__(self, id, name, rarity, platform, icon, type, icon_url, color='Default', customizable=False, unit=''):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.platform = platform
        self.icon = icon
        self.type = type
        self.icon_url = icon_url
        self.color = color
        self.customizable = customizable
        self.unit = unit

    def get_rarity(self):
        return self.rarity

    def set_rarity(self, rarity: str):
        self.rarity = rarity

    def get_type(self):
        return self.type

    def set_type(self, type_: str):
        self.type = type_

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


class SampleItemsData(ABCListColors, ABCRarities, ABCTypes, ABCNames):
    def get_items(self):
        return self.items

    def set_items(self, items):
        self.items = items

    def __init__(self, items: list):
        self.items = items


with open('sample-items-data.json', 'r') as file:
    json = load(file)

items_json = json['data']
sample_items = SampleItemsData([SampleItemData(**item) for item in items_json])


def test_get_item_by():
    shibuya = sample_items.get_item_by(
        name='Breakout: Shibuya',
        type_='decals',
        rarity='rare')
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
