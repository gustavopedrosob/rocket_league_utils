from rl_data_utils.items.items.items import Items
from re import IGNORECASE
from rl_data_utils.items.names.abc_base_names import ABCBaseNames
from rl_data_utils.utils.items.names.names import get_items_by_name_regex, get_names, get_items_by_name, \
    get_items_by_name_equal_to, get_items_by_name_contains


class Names(ABCBaseNames, Items):
    def get_items_by_name_regex(self, name_pattern: str, flags=IGNORECASE):
        return self.__class__(get_items_by_name_regex(name_pattern, self.items, flags))

    def get_names(self):
        return get_names(self.items)

    def get_items_by_name_equal_to(self, name: str):
        return self.__class__(get_items_by_name_equal_to(name, self.items))

    def get_items_by_name(self, name: str):
        return self.__class__(get_items_by_name(name, self.items))

    def get_items_by_name_contains(self, name: str):
        return self.__class__(get_items_by_name_contains(name, self.items))
