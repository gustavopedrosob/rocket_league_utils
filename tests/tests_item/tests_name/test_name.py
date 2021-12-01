import pytest

from rl_data_utils.item import Name


def test_compare_name():
    assert Name('Wall Breaker II').compare(Name('Wall Breaker II'))


@pytest.mark.parametrize('name', [None, ''])
def test_is_undefined(name):
    assert Name(name).is_undefined()
