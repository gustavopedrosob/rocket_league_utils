from rl_data_utils.item import Item
from datetime import datetime
from rl_data_utils.names.names import get_decal_and_car_name
from rl_data_utils.names import compare_names

init = datetime.now()
item_1 = Item.from_string('tw dingo imported')
item_2 = Item.from_string('titanium white dingo import')
print(item_2 == item_1)
print(get_decal_and_car_name('Silencer (Insidio)'))
print(get_decal_and_car_name('Slimline [Fennec])'))
print(get_decal_and_car_name("Breakout Type-S: S'mored"))
print(compare_names('Slimline [Fennec]', 'Slimline (Fennec)'))
end = datetime.now()
print(f'time to finish {end - init}')
