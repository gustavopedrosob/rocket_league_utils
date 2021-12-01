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
    sales = trades.filter_sales()
    print(sales)


def test_filter_buys():
    buys = trades.filter_buys()
    print(buys)


def test_filter_item_by_item():
    item_by_item = trades.filter_trades()
    print(item_by_item)


def test_filter_by_him_items():
    him_items = trades.filter_by_him_item(Item(name='Anodized'))
    print(him_items)


def test_filter_by_my_items():
    my_items = trades.filter_by_my_item(Item(name='Anodized'))
    print(my_items)
