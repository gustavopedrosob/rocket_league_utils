from __future__ import annotations

from rl_data_utils.exceptions import AttributeNotExists
from rl_data_utils.item.attribute.attribute_info import AttributeInfo

from typing import Union, Optional

SetAttribute = Union[str, int, list, bool, None]


class Attribute(AttributeInfo):
    undefined_value: Union[str, int, list, bool]
    default_value: Union[str, int, list, bool]

    def __init__(self, attribute: InitializeAttribute = None):
        self.attribute: SetAttribute = attribute

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._attribute})'

    def get_repr(self, attribute: Union[str, int, None] = None, maxsize: Optional[int] = None) -> str:
        if attribute is None:
            attribute = self.attribute
        value = 'UNDEFINED' if self.is_undefined() else str(attribute)
        if maxsize is not None:
            if len(value) > maxsize:
                value = value[:maxsize - 3] + '...'
        return value

    def _auto_setter(self, value: SetAttribute) -> Union[str, int, list, bool]:
        """
        It's used to set the self attribute
        :param value: Needs to be an instance of attribute_type or None
        :raise TypeError: If value doesn't match with expected value
        :return: An instance of attribute_type
        """
        if isinstance(value, self.attribute_type):
            return value
        elif value is None:
            return self.undefined_value
        else:
            raise TypeError(f'Invalid type to attribute, expected {self.attribute_type}.')

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value: SetAttribute):
        self._attribute = self._auto_setter(value)

    def compare(self, attribute: InitializeAttribute) -> bool:
        """
        Compare itself with another attribute
        :param attribute: An instance of Attribute
        :return: If both are the same attribute
        """
        if isinstance(attribute, self.__class__):
            return self.attribute == attribute.attribute or self.is_undefined() and attribute.is_undefined()
        else:
            return False

    @classmethod
    def initialize(cls, value: InitializeAttribute) -> Attribute:
        """
        Tries to transform some value into an instance of class
        :param value: It needs to be an instance of attribute_type, an instance of class or None
        :raise TypeError: If value doesn't match with expected value
        :return: An instance of class
        """
        if isinstance(value, cls.attribute_type):
            return cls(value)
        elif isinstance(value, cls):
            return value
        elif value is None or value == cls.undefined_value:
            return cls(cls.undefined_value)
        else:
            msg = f'Invalid type to property {cls.attribute_name}, expected {cls.__name__} or {cls.attribute_type}.'
            raise TypeError(msg)

    def is_undefined(self) -> bool:
        """
        :return: If self attribute is equal to the undefined_value
        """
        return self.attribute == self.undefined_value

    def is_valid(self) -> bool:
        """
        It tries self validate and if it has an error, then it's not valid
        :return: If self attribute is valid
        """
        try:
            self.validate()
        except AttributeNotExists:
            return False
        else:
            return True

    def validate(self):
        """
        It validates the self instance, if it's not valid it will raise some error
        """
        pass

    @classmethod
    def create_undefined(cls) -> Attribute:
        """
        :return: A self instance from the undefined_value in class
        """
        return cls(cls.undefined_value)

    @classmethod
    def create_default(cls) -> Attribute:
        """
        :return: A self instance from the default_value in class
        """
        return cls(cls.default_value)

    @classmethod
    def create_random(cls) -> Attribute:
        """
        :return: A self instance from a random value
        """
        pass


InitializeAttribute = Union[Attribute, str, list, int, bool, None]
