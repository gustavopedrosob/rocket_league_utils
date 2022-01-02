from __future__ import annotations

from typing import Callable, List, Union, Optional, Iterator

from rl_data_utils.item.attribute.attribute import ItemAttribute
from rl_data_utils.item.attribute_data.attribute_data import AttributesData
from rl_data_utils.item.item.constants import AttributeName
from rl_data_utils.item.item.data_item import DataItem
from rl_data_utils.item.item.item import Item
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject, Filterable, Validable, CanBeEmpty


class Items(RocketLeagueObject, Filterable, Validable, CanBeEmpty):
    def __init__(self, items: List[Union[Item, DataItem]]) -> None:
        self.items = items

    def __iter__(self) -> Iterator[Union[Item, DataItem]]: ...

    def filter_by_item(self, item: Item, attrs: Optional[List[AttributeName]] = ...) -> Items: ...

    def filter_by_attributes(self, attributes: List[Union[ItemAttribute, AttributesData]]) -> Items: ...

    def filter_by_attribute(self, attribute: ItemAttribute) -> Items: ...

    def filter_by_condition(self, condition: Callable[[Union[Item, DataItem]], bool]) -> Items: ...

    def filter_valid(self) -> Items: ...

    def is_valid(self) -> bool: ...

    def validate(self) -> None: ...

    def is_empty(self) -> bool: ...
