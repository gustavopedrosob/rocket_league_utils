from rl_data_utils.items.items import Items
from rl_data_utils.rocket_league.rocket_league import TradeAttribute


class TradeItems(Items, TradeAttribute):
    def validate(self) -> None: ...
