from json import load

from rl_data_utils.item.item.item import Item
from rl_data_utils.trade.trade import Trade
from rl_data_utils.trades.trades import Trades

with open('sample-trade.json', 'r') as file:
    content_file = load(file)

trades = Trades([Trade(my_items=[Item(name=e) for e in trade['LocalProducts']],
                       my_credits=trade['LocalCurrencyAmount'],
                       him_items=[Item(name=e) for e in trade['RemoteProducts']],
                       him_credits=trade['RemoteCurrencyAmount']) for trade in content_file])


def test_filter_sales():
    sales = trades.filter_by_trade_condition(lambda trade: trade.is_sale())
    print(sales)


def test_filter_buys():
    buys = trades.filter_by_trade_condition(lambda trade: trade.is_buy())
    print(buys)


def test_filter_item_by_item():
    item_by_item = trades.filter_by_trade_condition(lambda trade: trade.is_item_by_item())
    print(item_by_item)


def test_filter_by_him_items():
    item = Item(name='Anodized')
    him_items = trades.filter_by_trade_condition(lambda trade: not trade.him_items.filter_by_item(item).is_undefined())
    print(him_items)


def test_filter_by_my_items():
    item = Item(name='Anodized')
    my_items = trades.filter_by_trade_condition(lambda trade: not trade.my_items.filter_by_item(item).is_undefined())
    print(my_items)
