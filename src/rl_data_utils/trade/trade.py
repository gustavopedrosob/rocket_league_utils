from rl_data_utils.exceptions import InvalidTrade
from rl_data_utils.item.item.credit import Credit
from rl_data_utils.item.item.item import InitializeItem
from rl_data_utils.items.trade_items import TradeItems, InitializeTradeItems


class Trade:
    def __init__(self, my_items: InitializeTradeItems = None, him_items: InitializeTradeItems = None,
                 my_credits: InitializeItem = None, him_credits: InitializeItem = None):
        self.him_credits: Credit = him_credits
        self.him_items: TradeItems = him_items
        self.my_credits: Credit = my_credits
        self.my_items: TradeItems = my_items

    def __repr__(self) -> str:
        if self.is_sale():
            return f'[SOLD] {self.my_items} [FOR] {self.him_credits}'
        elif self.is_buy():
            return f'[BOUGHT] {self.him_items} [FOR] {self.my_credits}'
        elif self.is_item_by_item():
            return f'[ITEM-BY-ITEM] [MY ITEMS] {self.my_items} [HIM ITEMS] {self.him_items}'
        else:
            return f'[INVALID TRADE]'

    @staticmethod
    def _auto_setter_items(value) -> TradeItems:
        return TradeItems.initialize(value)

    @property
    def him_credits(self) -> Credit:
        return self._him_credits

    @him_credits.setter
    def him_credits(self, value) -> None:
        self._him_credits = Credit.initialize(value)

    @property
    def him_items(self) -> TradeItems:
        return self._him_items

    @him_items.setter
    def him_items(self, value) -> None:
        self._him_items = self._auto_setter_items(value)

    @property
    def my_credits(self) -> Credit:
        return self._my_credits

    @my_credits.setter
    def my_credits(self, value) -> None:
        self._my_credits = Credit.initialize(value)

    @property
    def my_items(self) -> TradeItems:
        return self._my_items

    @my_items.setter
    def my_items(self, value) -> None:
        self._my_items = self._auto_setter_items(value)

    def is_sale(self) -> bool:
        """
        Says if it's a sale trade
        :return:
        """
        return not self.my_items.is_undefined() and not self.him_credits.quantity.is_undefined()

    def is_buy(self) -> bool:
        """
        Says if it's a buy trade
        :return:
        """
        return not self.him_items.is_undefined() and not self.my_credits.quantity.is_undefined()

    def is_item_by_item(self) -> bool:
        """
        Says if it's an item by item trade
        :return:
        """
        return not self.him_items.is_undefined() and self.him_items.is_valid() \
            and not self.my_items.is_undefined() and self.my_items.is_valid() \
            and self.him_credits.quantity.is_undefined() and self.my_credits.quantity.is_undefined()

    def validate(self) -> None:
        """
        Validates
        :raise InvalidTrade: if isn't a sale, buy or item by item
        """
        if not (self.is_sale() or self.is_buy() or self.is_item_by_item()):
            raise InvalidTrade()

    def is_valid(self) -> bool:
        """
        Says if it's a valid trade
        :return: if it's a valid trade
        """
        try:
            self.validate()
        except InvalidTrade:
            return False
        else:
            return True
