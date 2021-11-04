from rl_data_utils.name import is_credits


def test_is_credit():
    assert is_credits("Credits")
    assert is_credits("Credit")
