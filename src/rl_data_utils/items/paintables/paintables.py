from rl_data_utils.items.items.items import Items
from rl_data_utils.utils.items.paintables.paintables import get_items_paintable, get_items_not_paintable,\
    get_items_by_paintable


class Paintables(Items):
    def get_items_by_paintable(self, paintable: bool):
        return self.__class__(get_items_by_paintable(paintable, self.items))

    def get_items_paintable(self):
        return self.__class__(get_items_paintable(self.items))

    def get_items_not_paintable(self):
        return self.__class__(get_items_not_paintable(self.items))
