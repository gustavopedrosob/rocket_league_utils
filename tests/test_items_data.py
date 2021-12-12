from json import load

from rl_data_utils.item.color.color import Color
from rl_data_utils.item.item.data_item import DataItem
from rl_data_utils.item.platform.constants import PLATFORMS
from rl_data_utils.item.platform.platform import Platforms, Platform
from rl_data_utils.items.items import Items

with open('sample-gameflip-data.json', 'r') as file:
    json = load(file)

items_json = json['data']

gameflip_data = Items(
    [DataItem(platform=Platforms(PLATFORMS) if data['platform'] == 'all' else Platform(data['platform']),
              color=[Color(e['name']) for e in data.get('colors', [])],
              name=data['name'],
              rarity=data['rarity'],
              slot=data['slot']) for data in items_json])
