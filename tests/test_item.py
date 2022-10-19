from rl_data_utils.item.item.item import Item


def test_compare():
    item_1 = Item(archived=True, name="Dingo", slot="Car", color="Titanium White", rarity="Imported",
                  certified="Striker", quantity=1, blueprint=False, tradable=True, serie="non crate")
    item_2 = Item(archived=False, name="Dingo", slot="Car", color="Grey", rarity="Imported",
                  certified="Goalkeeper", quantity=5, blueprint=False, tradable=True, serie="non crate")
    assert item_1.compare_identity(item_2)
