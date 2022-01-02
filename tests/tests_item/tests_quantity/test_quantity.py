import pytest

from rl_data_utils.exceptions import NegativeItemAttribute
from rl_data_utils.item.quantity.quantity import Quantity


def test_raises_lower_than_zero():
    with pytest.raises(NegativeItemAttribute):
        Quantity(-1).validate()


def test_from_random():
    print(Quantity.create_random())
