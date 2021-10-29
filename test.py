from rl_inventory_api.inventory import Inventory

inv = Inventory.read()
item_not_found = inv.get_item_by('iajhsiajnsianjisn')
