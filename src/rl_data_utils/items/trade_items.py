from rl_data_utils.exceptions import TradeSizeError
from rl_data_utils.items.items import Items
from rl_data_utils.rocket_league.rocket_league import TradeAttribute


class TradeItems(Items, TradeAttribute):
    def validate(self):
        super().validate()
        if len(self.items) > 24:
            raise TradeSizeError()
