import pytest

from rl_data_utils.item import Paintable


@pytest.mark.parametrize('paintable', [None])
def test_is_undefined(paintable):
    assert Paintable(paintable).is_undefined()
