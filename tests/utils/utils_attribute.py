import pytest


def all_are(function, containers):
    assert all(map(function, containers))


def compare(function, pair_equals, exception):
    assert all(map(lambda v: function(*v), pair_equals))
    with pytest.raises(exception):
        sample = pair_equals[0][0]
        function('', sample)
        function(sample, '')


def contains(function, containers):
    for container in containers:
        assert all(map(function, container))


def has(function, container, exception_not_exists, exception_invalid):
    sample = container[0]
    assert function(sample, container)
    with pytest.raises(exception_not_exists):
        function('', container)
    with pytest.raises(exception_invalid):
        function(sample, [''])


def get_in_string(function, string, pattern, exception):
    assert function(string) == pattern
    with pytest.raises(exception):
        function('')


def get_respective(function, pair_equals, exception):
    assert all(map(lambda v: function(v[0]) == v[1], pair_equals))
    with pytest.raises(exception):
        function('')


def is_(function, containers):
    for container in containers:
        assert all(map(function, container))


def validate_list(function, containers, exception):
    all(map(function, containers))
    with pytest.raises(exception):
        function([''])


def validate(function, containers, exception):
    for container in containers:
        all(map(function, container))
    with pytest.raises(exception):
        function('')
