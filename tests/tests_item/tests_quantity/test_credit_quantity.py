import pytest

from rl_data_utils.exceptions import InvalidCreditsQuantity
from rl_data_utils.item.attribute.attribute import CreditsQuantity


def test_raises_lower_than_zero():
    with pytest.raises(InvalidCreditsQuantity):
        CreditsQuantity(-1)
