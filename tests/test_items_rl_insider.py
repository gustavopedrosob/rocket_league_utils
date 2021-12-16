from json import load

from rl_data_utils.item.item.data_item import DataItem
from rl_data_utils.item.name.name import Name
from rl_data_utils.item.price.data_price import DataPrice
from rl_data_utils.item.price.price_data import PriceData
from rl_data_utils.items.items import Items

with open('sample-items-rl-insider.json', 'r') as file:
    json = load(file)

items = []

for item in json:
    price_data = []
    for platform, platform_value in item['prices'].items():
        for color, color_value in platform_value.items():
            data_price = dict(
                color=color,
                platform=platform)
            if color_value:
                data_price.update(dict(
                    crafting_cost=color_value['b'] if color_value else None,
                    price=color_value['k'])
                )
            price_data.append(DataPrice(**data_price))
    price_data = PriceData(price_data)
    data_item = DataItem(
        name=item['name'],
        paintable=item['paintable'],
        slot=item['slot'],
        price=price_data
    )
    items.append(data_item)

rl_insider_items = Items(items)


def test_getting_price():
    results = rl_insider_items.filter_by_attribute(Name('hexed'))
    for result in results:
        print(result.price.get_price(color='Default'))
