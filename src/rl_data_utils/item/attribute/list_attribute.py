from __future__ import annotations

from typing import Union, Any, Type, List, Final, Optional

from rl_data_utils.item.attribute.attribute import Attribute, InitializeAttribute
from rl_data_utils.item.attribute.attribute_info import AttributeInfo


SetListAttribute = Optional[List[InitializeAttribute]]


class ListAttribute(Attribute, AttributeInfo):
    attribute_type: Final[Type[list]] = list
    sub_attribute: Type[Attribute]
    undefined_value: Final[list] = []

    def __init__(self, attribute: list) -> None:
        super().__init__(attribute)

    def _auto_setter(self, value: SetListAttribute) -> Any:
        """
        It's used to set the self attribute
        :param value: It needs to be an instance of attribute_type, an undefined_value or None
        :raise TypeError: If value doesn't match with expected value
        :return: An instance of attribute_type
        """
        if value is None or value == self.undefined_value:
            return self.undefined_value
        elif isinstance(value, list):
            value = value.copy()
            for index, each in enumerate(value):
                value[index] = self.sub_attribute.initialize(each)
            return value
        else:
            raise TypeError(f'Invalid type, expected List[{self.sub_attribute.__name__}].')

    def has(self, attribute: Attribute) -> bool:
        """
        Says if it has an attribute
        :param attribute: An attribute for find
        :return: If the same attribute was found
        """
        for e in self.attribute:
            if e.compare(attribute):
                return True
        return False

    @classmethod
    def initialize(cls, value: InitializeListAttribute) -> ListAttribute:
        """
        Tries to transform some value into an instance of class
        :param value: It's need to be an instance of class, List[Union[sub_attribute, None]] or None
        :raise TypeError: If value doesn't match with expected value
        :return: An instance of class
        """
        if value is None or value == cls.undefined_value:
            return cls(cls.undefined_value)
        elif isinstance(value, cls):
            return value
        elif isinstance(value, cls.attribute_type):
            value = value.copy()
            for index, each in enumerate(value):
                value[index] = cls.sub_attribute.initialize(each)
            return cls(value)
        else:
            raise TypeError(f'Invalid type, expected {cls.__name__}, List[Union[{cls.sub_attribute, None}] or None.')

    def validate(self):
        """
        Validates all attributes
        :raise AttributeNotExists: If any of attribute doesn't exist
        """
        for e in self.attribute:
            e.validate()


InitializeListAttribute = Union[ListAttribute, List[InitializeAttribute], None]
