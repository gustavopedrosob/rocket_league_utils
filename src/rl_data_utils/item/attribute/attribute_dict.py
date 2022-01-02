from __future__ import annotations


class AttributeDict:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __getitem__(self, item):
        """
        Returns some value by a respective key
        :param item: It's a key for some value
        :raise KeyError: If item is invalid
        :return: Can return anything that was stored in key
        """
        for key, value in self.dictionary:
            if key.compare(item):
                return value
        raise KeyError()

    def __setitem__(self, key, value):
        """
        It set some key in dictionary, if the same key already exists, so it overrides the previous value
        :param key: Some string value
        :param value: Any value
        :raise KeyError: If key is unsupported
        """
        for _key, _value in self.dictionary:
            if _key.compare(key):
                raise KeyError()
        self.dictionary.append((key, value))
