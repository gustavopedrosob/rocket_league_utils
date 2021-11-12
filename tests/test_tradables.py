from test_items import sample_items


def test_get_items_by_tradable():
    print(sample_items.get_items_by_tradable(True).items)
    print(sample_items.get_items_by_tradable(False).items)


def test_get_items_tradable():
    print(sample_items.get_items_tradable().items)


def test_get_items_not_tradable():
    print(sample_items.get_items_not_tradable().items)
