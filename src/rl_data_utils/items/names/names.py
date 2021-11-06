from rl_data_utils.items.items.items import ABCItems
from re import IGNORECASE
from rl_data_utils.items.names.abc_base_names import ABCBaseNames
from rl_data_utils.utils.items.names.names import get_items_by_name_regex, get_names, get_items_by_name, \
    get_items_by_name_equal_to, get_items_by_name_contains


class ABCNames(ABCBaseNames, ABCItems):
    def get_items_by_name_regex(self, name_pattern: str, flags=IGNORECASE):
        return get_items_by_name_regex(name_pattern, self.get_items(), flags)

    def get_names(self):
        return get_names(self.get_items())

    def get_items_by_name_equal_to(self, name: str):
        return get_items_by_name_equal_to(name, self.get_items())

    def get_items_by_name(self, name: str, items=None):
        if items is None:
            items = self.get_items()
        return get_items_by_name(name, items)

    def get_items_by_name_contains(self, name: str):
        return get_items_by_name_contains(name, self.get_items())
