from json import load

from rl_data_utils.item.item.credit import Credit
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.attribute.attribute import Name, CreditsQuantity
from rl_data_utils.items.trade_items import TradeItems
from rl_data_utils.trade.offer import Offer
from rl_data_utils.trade.trade import Trade
from rl_data_utils.trades.trades import Trades

with open('sample-trade.json', 'r') as file:
    content_file = load(file)

trades = Trades([Trade(my_offer=Offer(Credit(quantity=CreditsQuantity(trade['LocalCurrencyAmount'])),
                                      TradeItems([Item(name=Name(e)) for e in trade['LocalProducts']])),
                       him_offer=Offer(Credit(quantity=CreditsQuantity(trade['RemoteCurrencyAmount'])),
                                       TradeItems([Item(name=Name(e)) for e in trade['RemoteProducts']])))
                 for trade in content_file])


def test_filter_sales():
    sales = trades.filter_by_trade(lambda trade: trade.is_sale())
    print(sales)


def test_filter_buys():
    buys = trades.filter_by_trade(lambda trade: trade.is_buy())
    print(buys)


def test_filter_item_by_item():
    item_by_item = trades.filter_by_trade(lambda trade: trade.is_item_by_item())
    print(item_by_item)


def test_filter_by_him_items():
    item = Item(name=Name('Anodized'))
    him_items = trades.filter_by_him_offer(lambda offer: offer.items.filter_by_item(item).is_empty())
    print(him_items)


def test_filter_by_my_items():
    item = Item(name=Name('Anodized'))
    my_items = trades.filter_by_my_offer(lambda offer: offer.items.filter_by_item(item).is_empty())
    print(my_items)
