from test_items_rl_insider import sample_items


def test_get_items_paintables():
    assert sample_items.get_items_paintable()


def test_get_items_not_paintable():
    assert sample_items.get_items_not_paintable()


def test_get_items_by_paintable():
    assert sample_items.get_items_by_paintable(True)
    assert sample_items.get_items_by_paintable(False)
