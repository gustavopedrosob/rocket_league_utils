from rl_data_utils.item.item.item_attribute import ItemAttribute
from rl_data_utils.item.paintable.abc_base_paintable import ABCBasePaintable


class ABCPaintable(ABCBasePaintable, ItemAttribute):
    pass


class Paintable:
    def __init__(self, paintable: bool):
        self.paintable = paintable

    def get_paintable(self):
        return self.paintable
