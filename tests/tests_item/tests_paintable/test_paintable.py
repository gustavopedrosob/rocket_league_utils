import pytest

from rl_data_utils.item.paintable.paintable import Paintable


def test_from_random():
    print(Paintable.create_random())


@pytest.mark.parametrize('paintable', [None])
def test_is_undefined(paintable):
    assert Paintable(paintable).is_undefined()
