import pytest
from rl_data_utils.exceptions import NameHaveNotCarName
from rl_data_utils.utils.item.name.is_functions import is_credits
from rl_data_utils.utils.item.name.name import get_decal_and_car_name, compare_name


def test_is_credit():
    assert is_credits("Credits")
    assert is_credits("Credit")


def test_get_decal_and_car_name():
    with pytest.raises(NameHaveNotCarName):
        get_decal_and_car_name('')


def test_compare_names():
    assert compare_name('Buzz Kill [Octane]', 'Octane: Buzz Kill')
