import datetime
from json import load
import rocket_league_utils.main as rl_utils


def get_inventory_items():
    with open("sample-inventory-items.json", "r") as file:
        json = load(file)

    inventory = []
    items_json = json["items"]
    for item in items_json:
        item_object = rl_utils.Item(
            color=item["color"],
            rarity=item["rarity"],
            slot=item["slot"],
            certified=item["certified"],
            name=item["name"],
            quantity=item["quantity"],
            trade_lock=not item["tradable"],
            serie=item["serie"],
            blueprint=item["slot"] == "Blueprint",
            platform="pc",
            acquired=datetime.datetime.now()
        )
        inventory.append(item_object)
    return inventory


inventory_items = get_inventory_items()


def test_filter_by_item_represents():
    item = rl_utils.Item(name="Dingo", slot="Car", color="Tw", rarity="Import", certified="GoalKeeper", quantity=6,
                         blueprint=False, trade_lock=False, platform="pc", serie="Non crate",
                         acquired=datetime.datetime.now())
    print(list(filter(item.compare_repr, inventory_items)))


def test_filter_by_item_identity():
    item = rl_utils.Item(name="Octane: Buzz Kill", slot="Decal", blueprint=False, trade_lock=False, platform="Pc",
                         quantity=1, rarity="rare", serie="Non crate", acquired=datetime.datetime.now())
    print(list(filter(item.compare_identity, inventory_items)))
