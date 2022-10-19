from json import load

from rl_data_utils.exceptions import InvalidAttribute
from rl_data_utils.item.attribute.attribute import Archived, Certified, Color, Name, Quantity, Rarity, Serie, Slot, \
    Tradable
from rl_data_utils.item.item.constants import INDENTIFIER
from rl_data_utils.item.item.item import Item
from rl_data_utils.items.inventory import Inventory

with open("sample-inventory-items.json", "r") as file:
    json = load(file)

items_json = json["items"]
inventory_items = Inventory()
for item in items_json:
    try:
        item_object = Item(
            color=item["color"],
            rarity=item["rarity"],
            slot=item["slot"],
            certified=item["certified"],
            name=item["name"],
            quantity=item["quantity"],
            tradable=item["tradable"],
            serie=item["serie"],
            blueprint=item["slot"] == "Blueprint"
        )
    except InvalidAttribute:
        continue
    else:
        inventory_items.add_items(item_object)


def test_filter_by_item_indentifier_mode():
    item_ = Item(Archived(True), Name("Dingo"), Slot("Car"), Color("Saffron"), Rarity("Import"),
                 Certified("GoalKeeper"), Quantity(6))
    i = inventory_items.filter_by_item(item_, INDENTIFIER)
    print(i.items)


# def test_filter_by():
#     i = inventory_items.filter_by_item(Item(name=Name("Octane: Buzz Kill")))
#     print(i.items)
#
#
# def test_filter_by_item():
#     item_ = Item(name=Name("Octane: Buzz Kill"))
#     print(inventory_items.filter_by_item(item_).items)
