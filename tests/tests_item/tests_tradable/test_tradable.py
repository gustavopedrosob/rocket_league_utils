import pytest

from rl_data_utils.item.tradable.tradable import Tradable


def test_from_random():
    print(Tradable.create_random())


@pytest.mark.parametrize('tradable', [None])
def test_is_undefined(tradable):
    assert Tradable(tradable).is_undefined()
