from rl_data_utils.item.name.name import Name


def test_from_random():
    print(Name.create_random(), end='')


def test_compare_name():
    assert Name('Wall Breaker II').compare(Name('Wall Breaker II'))
