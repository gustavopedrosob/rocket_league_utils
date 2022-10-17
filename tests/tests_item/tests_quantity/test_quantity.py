import pytest

from rl_data_utils.exceptions import NegativeItemAttribute
from rl_data_utils.item.attribute.attribute import Quantity


def test_raises_lower_than_zero():
    with pytest.raises(NegativeItemAttribute):
        Quantity(-1)

