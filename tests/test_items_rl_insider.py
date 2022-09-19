from json import load

from rl_data_utils.item.attribute.attribute import Color, Name, Platform, Price, CreditsQuantity, Slot
from rl_data_utils.item.attribute_data.attribute_data import CraftingCost, Paintable, DataPrice, PriceData
from rl_data_utils.item.item.data_item import DataItem
from rl_data_utils.items.items import Items

with open('sample-items-rl-insider.json', 'r') as file:
    json = load(file)

items = []

for item in json:
    price_data = []
    for platform, platform_value in item['prices'].items():
        for color, color_value in platform_value.items():
            data_price = dict(
                color=Color(color),
                platform=Platform(platform))
            if color_value:
                price = []
                if isinstance(color_value, dict):
                    if color_value.get('k') is not None:
                        price = [CreditsQuantity(v) for v in color_value['k']]
                data_price.update(dict(
                    crafting_cost=CraftingCost(color_value['b']) if color_value else None,
                    price=Price(*price) if price else None))
            price_data.append(DataPrice(**data_price))
    data_item = DataItem(
        name=Name(item['name']),
        paintable=Paintable(item['paintable']),
        slot=Slot(item['slot']),
        price=PriceData(price_data)
    )
    items.append(data_item)

rl_insider_items = Items(items)


def test_getting_price():
    results = rl_insider_items.filter_by_attribute(Name('hexed'))
    for result in results:
        print(result.price.get_price(color=Color('Default')))
