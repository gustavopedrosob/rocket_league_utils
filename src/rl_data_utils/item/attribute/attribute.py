from __future__ import annotations
from rl_data_utils.exceptions import AttributeNotExists
from rl_data_utils.item.attribute.attribute_info import AttributeInfo


class Attribute(AttributeInfo):
    undefined_value: object

    def __init__(self, attribute=None):
        self.attribute = attribute

    def __repr__(self):
        return f'{self.__class__.__name__}({self.attribute})'

    def _auto_setter(self, value):
        if isinstance(value, self.attribute_type):
            return value
        elif value is None:
            return self.undefined_value
        else:
            raise TypeError(f'Invalid type attribute, expected {self.attribute_type}.')

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = self._auto_setter(value)

    def compare(self, attribute: Attribute) -> bool:
        if isinstance(attribute, self.__class__):
            return self.attribute == attribute.attribute or self.is_undefined() and attribute.is_undefined()
        else:
            return False

    @classmethod
    def initialize(cls, value) -> Attribute:
        if isinstance(value, cls.attribute_type):
            return cls(value)
        elif isinstance(value, cls):
            return value
        elif value is None:
            return cls()
        else:
            msg = f'Invalid type to property {cls.attribute_name}, expected {cls.__name__} or {cls.attribute_type}.'
            raise TypeError(msg)

    def is_undefined(self):
        return self.attribute == self.undefined_value

    def is_valid(self):
        """
        It says if a string is a determined attribute
        :return: If string parameter is a determined attribute, if its None or a empty string returns False
        :raises TypeError: If the parameter is not a str or NoneType
        :raises NullOrEmptyAttribute: If the string parameter is None or empty
        """
        try:
            self.validate()
        except AttributeNotExists:
            return False
        else:
            return True

    def validate(self):
        pass

    @classmethod
    def create_undefined(cls) -> Attribute:
        return cls(cls.undefined_value)
