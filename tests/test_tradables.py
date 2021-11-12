from test_items import sample_items


def test_get_tradable():
    print(sample_items.get_items_tradable().items)


def test_get_not_tradable():
    print(sample_items.get_items_not_tradable().items)
