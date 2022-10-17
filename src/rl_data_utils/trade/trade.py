from rl_data_utils.exceptions import InvalidTrade
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject


class Trade(RocketLeagueObject):
    def __init__(self, my_offer, him_offer, date=None):
        self.him_offer = him_offer
        self.my_offer = my_offer
        self.date = date

    def is_sale(self):
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

    def is_item_by_item(self):
        """
        Says if it's an item by item trade
        :return:
        """
        return self.him_offer.is_only_items() and self.my_offer.is_only_items()

    def validate(self):
        """
        Validates
        :raise InvalidTrade: if isn't a sale, buy or item by item
        """
        if not (self.is_sale() or self.is_buy() or self.is_item_by_item()):
            raise InvalidTrade()

    def get_type(self):
        # TODO: substituir por constants e criar exception
        if self.is_buy():
            return "buy"
        elif self.is_sale():
            return "sale"
        elif self.is_item_by_item():
            return "item-by-item"
        else:
            raise Exception()

    def is_valid(self):
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
