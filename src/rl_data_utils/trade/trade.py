from rl_data_utils.exceptions import InvalidTrade
from rl_data_utils.item.item.credits import Credits
from rl_data_utils.items.trade_items import TradeItems


class Trade:
    def __init__(self, my_items=None, him_items=None, my_credits=None, him_credits=None):
        self.him_credits = him_credits
        self.him_items = him_items
        self.my_credits = my_credits
        self.my_items = my_items

    def __repr__(self):
        if self.is_sale():
            return f'[SOLD] {self.my_items} [FOR] {self.him_credits}'
        elif self.is_buy():
            return f'[BOUGHT] {self.him_items} [FOR] {self.my_credits}'
        elif self.is_item_by_item():
            return f'[ITEM-BY-ITEM] [MY ITEMS] {self.my_items} [HIM ITEMS] {self.him_items}'
        else:
            return f'[INVALID TRADE]'

    @staticmethod
    def _auto_setter_items(value):
        return TradeItems.initialize(value)

    @property
    def him_credits(self):
        return self._him_credits

    @him_credits.setter
    def him_credits(self, value):
        self._him_credits = Credits.initialize(value)

    @property
    def him_items(self):
        return self._him_items

    @him_items.setter
    def him_items(self, value):
        self._him_items = self._auto_setter_items(value)

    @property
    def my_credits(self):
        return self._my_credits

    @my_credits.setter
    def my_credits(self, value):
        self._my_credits = Credits.initialize(value)

    @property
    def my_items(self):
        return self._my_items

    @my_items.setter
    def my_items(self, value):
        self._my_items = self._auto_setter_items(value)

    def is_sale(self):
        return not self.my_items.is_undefined() and not self.him_credits.quantity.is_undefined()

    def is_buy(self):
        return not self.him_items.is_undefined() and not self.my_credits.quantity.is_undefined()

    def is_item_by_item(self):
        return not self.him_items.is_undefined() and self.him_items.is_valid()\
               and not self.my_items.is_undefined() and self.my_items.is_valid()\
               and self.him_credits.quantity.is_undefined() and self.my_credits.quantity.is_undefined()

    def validate(self):
        if self.is_sale() or self.is_buy() or self.is_item_by_item():
            pass
        else:
            raise InvalidTrade()

    def is_valid(self):
        try:
            self.validate()
        except InvalidTrade:
            return False
        else:
            return True
