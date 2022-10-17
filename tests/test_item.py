from logging import info

from rl_data_utils.item.attribute.attribute import Archived, Blueprint, Certified, Color, Name, Platform, Quantity, \
    Rarity, Slot
from rl_data_utils.item.attribute.constants import EXOTIC, IMPORT, RARE, VERY_RARE
from rl_data_utils.item.item.constants import INDENTIFIER
from rl_data_utils.item.item.credit import Credit
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.attribute_data.attribute_data import Paintable


def test_indentifier_compare():
    item_1 = Item(Archived(True), Name("Dingo"), Slot("Car"), Color("Titanium White"), Rarity("Imported"),
                  Certified("Striker"), Quantity(1), Blueprint(False), Paintable(True), Platform("pc"))
    item_2 = Item(Archived(False), Name("Dingo"), Slot("Car"), Color("Grey"), Rarity("Imported"),
                  Certified("Goalkeeper"), Quantity(5), Blueprint(False), Paintable(True), Platform("pc"))
    assert item_1.compare(item_2, lambda attr: attr.identifier in INDENTIFIER)


def test_is_ncr():
    ncvr_item = Item(rarity=Rarity(RARE))
    assert ncvr_item.is_non_crate(Rarity("rare"))


def test_is_ncvr():
    ncvr_item = Item(rarity=Rarity(VERY_RARE))
    assert ncvr_item.is_non_crate(Rarity("vr"))


def test_is_nci():
    ncvr_item = Item(rarity=Rarity(IMPORT))
    assert ncvr_item.is_non_crate(Rarity("import"))


def test_is_nce():
    ncvr_item = Item(rarity=Rarity(EXOTIC))
    assert ncvr_item.is_non_crate(Rarity("exotic"))


def test_credit():
    assert Credit()


# @pytest.mark.parametrize("quantity", [10, 100, 110, 120, 20])
# def test_credits_is_valid(quantity):
#     assert Credit.initialize(quantity).is_valid()
#
#
# @pytest.mark.parametrize("quantity", [1, 5, 6, 19, 15])
# def test_credits_is_not_valid(quantity):
#     assert not Credit.initialize(quantity).is_valid()
#
#
# @pytest.mark.parametrize("item_1,item_2", [["dingo tw imported", "dingo titanium white import"]])
# def test_comparing_items(item_1, item_2):
#     assert Item.initialize(item_1).compare(Item.initialize(item_2))
