from __future__ import annotations

from typing import Optional, Type, Union, Any

from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedAttribute
from rl_data_utils.item.attribute.regex_based_list_attribute import RegexBasedListAttribute

SetAttributeDict = Optional[dict]


class AttributeDict:
    _cls_attribute: Type[RegexBasedAttribute]
    _cls_list_attribute: Type[RegexBasedListAttribute]

    def __init__(self, dictionary: SetAttributeDict = None):
        self.dictionary: dict = dictionary

    @property
    def dictionary(self):
        return self._dictionary

    @dictionary.setter
    def dictionary(self, value: SetAttributeDict):
        if value is None:
            self._dictionary = {}
        elif isinstance(value, dict):
            self._dictionary = value
            self.validate()
        else:
            raise TypeError('Invalid type, expected dict or None.')

    def validate(self) -> None:
        for key in self._dictionary.keys():
            self._cls_attribute(key).validate()

    def __getitem__(self, item: str) -> Any:
        """
        Returns some value by a respective key
        :param item: It's a key for some value
        :raise KeyError: If item is invalid
        :return: Can return anything that was stored in key
        """
        item = self._cls_attribute.initialize(item)
        for key, value in self._dictionary.items():
            if self._cls_attribute(key).compare(item):
                return value
        raise KeyError(str)

    def __setitem__(self, key: str, value: Any):
        """
        It set some key in dictionary, if the same key already exists, so it overrides the previous value
        :param key: Some string value
        :param value: Any value
        :raise ValueError: If key is unsupported
        """
        attribute = self._cls_attribute(key)
        attributes = self._cls_list_attribute.create_default()
        respective = attributes.get_respective(attribute)
        if respective:
            self._dictionary[respective.attribute] = value
        else:
            raise ValueError(f'Unsupported key {key}.')

    @classmethod
    def initialize(cls, value: InitializeAttributeDict) -> AttributeDict:
        if isinstance(value, dict) or value is None:
            return cls(value)
        elif isinstance(value, cls):
            return value
        else:
            TypeError('Invalid type, expected AttributeDict, dict or None.')


InitializeAttributeDict = Union[AttributeDict, SetAttributeDict]
