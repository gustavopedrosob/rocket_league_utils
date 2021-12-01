import pytest

from rl_data_utils.item import Quantity


@pytest.mark.parametrize('quantity', [None])
def test_is_undefined(quantity):
    assert Quantity(quantity).is_undefined()
