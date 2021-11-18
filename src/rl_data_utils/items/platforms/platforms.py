from rl_data_utils.items.items.items import Items
from rl_data_utils.items.platforms.abc_base_platforms import ABCBasePlatforms
from rl_data_utils.utils.items.platforms.platforms import get_items_pc, get_items_ps4, get_items_xbox, get_items_switch


class Platforms(ABCBasePlatforms, Items):
    def get_items_pc(self):
        return self.__class__(get_items_pc(self.items))

    def get_items_ps4(self):
        return self.__class__(get_items_ps4(self.items))

    def get_items_xbox(self):
        return self.__class__(get_items_xbox(self.items))

    def get_items_switch(self):
        return self.__class__(get_items_switch(self.items))
