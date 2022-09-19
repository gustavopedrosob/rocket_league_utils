from json import load

from rl_data_utils.item.attribute.attribute import Name, Platform, Rarity, Slot
from rl_data_utils.item.attribute_data.attribute_data import Colors, Platforms
from rl_data_utils.item.item.data_item import DataItem
from rl_data_utils.item.attribute_data.constants import PLATFORMS
from rl_data_utils.items.items import Items

with open('sample-gameflip-data.json', 'r') as file:
    json = load(file)

items_json = json['data']

gameflip_data = Items(
    [DataItem(platform=Platforms.from_str_list(PLATFORMS) if data['platform'] == 'all' else Platform(data['platform']),
              color=Colors.from_str_list([e['name'] for e in data.get('colors', [])]),
              name=Name(data['name']),
              rarity=Rarity(data['rarity']),
              slot=Slot(data['slot'])) for data in items_json])
