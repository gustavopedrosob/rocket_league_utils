from rl_data_utils.exceptions import InvalidTrade
from rl_data_utils.items.trade_items import TradeInventory
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject
from rl_data_utils.trade.constants import ITEM_FOR_ITEM, SELL, BUY


class Trade(RocketLeagueObject):
    def __init__(self, my_offer: TradeInventory, him_offer: TradeInventory, date=None):
        self.him_offer = him_offer
        self.my_offer = my_offer
        self.date = date

    def is_sell(self):
        """
        Says if it's a sale trade
        :return:
        """
        return self.my_offer.is_only_items() and self.him_offer.is_only_credits()

    def is_buy(self):
        """
        Says if it's a buy trade
        :return:
        """
        return self.him_offer.is_only_items() and self.my_offer.is_only_credits()

    def is_item_for_item(self):
        """
        Says if it's an item by item trade
        :return:
        """
        return self.him_offer.is_only_items() and self.my_offer.is_only_items()

    def get_type(self):
        if self.is_buy():
            return BUY
        elif self.is_sell():
            return SELL
        elif self.is_item_for_item():
            return ITEM_FOR_ITEM
        else:
            raise InvalidTrade()
