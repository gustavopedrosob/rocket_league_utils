from rl_data_utils.item import Item
from datetime import datetime

init = datetime.now()
item_1 = Item.from_string('tw dingo imported')
item_2 = Item.from_string('titanium white dingo import')
print(item_2 == item_1)
end = datetime.now()
print(f'time to finish {end - init}')
