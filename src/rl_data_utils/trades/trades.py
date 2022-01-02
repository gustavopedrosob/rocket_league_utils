from __future__ import annotations


class Trades:
    def __init__(self, trades):
        self.trades = trades

    def filter_by_trade(self, condition):
        """
        Filter self trades by a condition function that receives a trade as parameter and returns a boolean
        :param condition: A function that works as condition, receives a trade as parameter and return a boolean
        :return: A filtered trades instance
        """
        return self.__class__(list(filter(condition, self.trades)))

    def filter_by_him_offer(self, condition):
        return self.filter_by_trade(lambda trade: condition(trade.him_offer))

    def filter_by_my_offer(self, condition):
        return self.filter_by_trade(lambda trade: condition(trade.my_offer))

    def filter_by_date(self, condition):
        return self.filter_by_trade(lambda trade: condition(trade.date) if trade.date else False)
