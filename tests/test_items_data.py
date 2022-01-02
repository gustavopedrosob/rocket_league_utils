from json import load

from rl_data_utils.item.color.color import Colors
from rl_data_utils.item.item.data_item import DataItem
from rl_data_utils.item.name.name import Name
from rl_data_utils.item.platform.constants import PLATFORMS
from rl_data_utils.item.platform.platform import Platforms, Platform
from rl_data_utils.item.rarity.rarity import Rarity
from rl_data_utils.item.slot.slot import Slot
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
