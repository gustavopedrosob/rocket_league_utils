import pytest

from rl_data_utils.item.certified.certified import Certified
from rl_data_utils.item.color.color import Color


def test_comparing_two_different_attributes():
    with pytest.raises(TypeError):
        _ = Color('tw').compare(Certified('striker'))


def test_comparing_equal_attributes():
    assert Color('Tw').compare('Titanium White')
