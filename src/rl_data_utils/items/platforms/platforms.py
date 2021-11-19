from re import IGNORECASE
from rl_data_utils.items.items.items import Items
from rl_data_utils.utils.items.platforms.platforms import get_items_pc, get_items_ps4, get_items_xbox, get_items_switch, \
    get_items_with_valid_platform, get_items_by_platform_regex, get_items_by_platform, get_items_by_platform_equal_to, \
    get_items_by_platform_contains, get_platforms


class Platforms(Items):
    def get_items_with_valid_platform(self):
        return self.__class__(get_items_with_valid_platform(self.items))

    def get_items_by_platform_regex(self, platform_pattern, flags=IGNORECASE):
        return self.__class__(get_items_by_platform_regex(self.items, platform_pattern, flags))

    def get_items_by_platform(self, platform: str):
        return self.__class__(get_items_by_platform(self.items, platform))

    def get_items_by_platform_equal_to(self, platform: str):
        return self.__class__(get_items_by_platform_equal_to(self.items, platform))

    def get_items_by_platform_contains(self, platform: str):
        return self.__class__(get_items_by_platform_contains(self.items, platform))

    def get_platforms(self):
        return self.__class__(get_platforms(self.items))

    def get_items_pc(self):
        return self.__class__(get_items_pc(self.items))

    def get_items_ps4(self):
        return self.__class__(get_items_ps4(self.items))

    def get_items_xbox(self):
        return self.__class__(get_items_xbox(self.items))

    def get_items_switch(self):
        return self.__class__(get_items_switch(self.items))
