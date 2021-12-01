import pytest

from rl_data_utils.item import Tradable


@pytest.mark.parametrize('tradable', [None])
def test_is_undefined(tradable):
    assert Tradable(tradable).is_undefined()
