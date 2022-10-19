from __future__ import annotations

from typing import List, Callable


from rl_data_utils.item.item.identity_item import IdentityItem
from rl_data_utils.item.item.item import Item, RepresentsItem


class Inventory:
    def __init__(self, items: List[Item] = None):
        if items is None:
            items = []
        self.items = items

    def __iter__(self):
        yield from self.items

    def filter_by_condition(self, condition: Callable[[Item], bool]) -> Inventory:
        return Inventory(list(filter(condition, self.items)))

    def filter_by_identity_item(self, identity_item: IdentityItem) -> Inventory:
        return self.filter_by_condition(lambda identity_item_: identity_item_.compare_identity(identity_item))

    def filter_by_represents_item(self, represents_item: RepresentsItem) -> Inventory:
        return self.filter_by_condition(lambda represents_item_: represents_item_.compare_identity(represents_item))

    def is_empty(self) -> bool:
        return self.items == []
