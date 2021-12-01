from __future__ import annotations
from rl_data_utils.item.attribute.str_attribute import StrAttribute


class AttributeDict:
    _cls_attribute: StrAttribute.__class__

    def __init__(self, dictionary=None):
        self.dictionary = dictionary

    @property
    def dictionary(self):
        return self._dict

    @dictionary.setter
    def dictionary(self, value):
        if value is None:
            self._dict = {}
        elif isinstance(value, dict):
            self._dict = value
        else:
            raise TypeError()
        self.validate()

    def validate(self):
        for key in self._dict.keys():
            self._cls_attribute(key).validate()

    def __getitem__(self, item):
        item = self._cls_attribute.initialize(item)
        for key, value in self._dict.items():
            if self._cls_attribute(key).compare(item):
                return value
        raise KeyError()

    def __setitem__(self, key, value):
        self._cls_attribute(key).validate()
        self._dict[key] = value

    @classmethod
    def initialize(cls, value) -> AttributeDict:
        if isinstance(value, dict):
            return cls(value)
        elif isinstance(value, cls):
            return value
        else:
            TypeError()
