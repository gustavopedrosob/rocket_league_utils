import pytest

from rl_data_utils.item.quantity.quantity import Quantity


def test_raises_lower_than_zero():
    with pytest.raises(ValueError):
        Quantity(-1)


def test_from_random():
    print(Quantity.create_random())


@pytest.mark.parametrize('quantity', [None])
def test_is_undefined(quantity):
    assert Quantity(quantity).is_undefined()
