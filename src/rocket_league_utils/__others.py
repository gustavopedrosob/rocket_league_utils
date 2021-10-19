from re import search, IGNORECASE
from inspect import getmembers, isfunction


def _regex_found(pattern, string) -> bool:
    return bool(search(pattern, string, IGNORECASE))


class IsSomethingAndCompare:
    module = None

    @classmethod
    def is_(cls, string: str) -> bool:
        functions: list[callable] = cls.get_functions()
        return any(map(lambda f: f(string), functions))

    @classmethod
    def compare_(cls, string_1: str, string_2) -> bool:
        functions: list[callable] = cls.get_functions()
        return any(map(lambda f: f(string_1) and f(string_2), functions))

    @classmethod
    def get_functions(cls):
        return [f for fn, f in filter(lambda f: not f[0].startswith("_"), getmembers(cls.module, isfunction))]
