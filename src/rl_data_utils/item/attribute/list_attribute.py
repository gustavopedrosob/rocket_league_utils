from __future__ import annotations
from rl_data_utils.exceptions import AttributeNotExists
from rl_data_utils.item.attribute.attribute import Attribute
from rl_data_utils.item.attribute.attribute_info import AttributeInfo


class ListAttribute(Attribute, AttributeInfo):
    attribute_type = list
    sub_attribute: Attribute.__class__
    undefined_value = []

    def is_valid(self) -> bool:
        """
        It says if all elements in a list are attributes
        :return: If all elements in a container are attributes, returns False if container is empty or None
        :raises TypeError: If container is not list
        :raises NullOrEmptyAttribute: If the any element of container is None or empty
        """
        try:
            self.validate()
        except AttributeNotExists:
            return False
        else:
            return True

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        if value is None or value == self.undefined_value:
            self._attribute = self.undefined_value
        elif isinstance(value, list):
            for index, each in enumerate(value):
                value[index] = self.sub_attribute.initialize(each)
                # if not isinstance(each, self.sub_attribute):
                #     raise TypeError(f'Invalid item inside the list when creating {self.__class__.__name__},'
                #                     f'expected {self.sub_attribute.__name__}')
            self._attribute = value
        else:
            raise TypeError(f'Invalid type to create {self.__class__.__name__},'
                            f'expected list[{self.sub_attribute.__name__}]')

    def has(self, attribute: Attribute) -> bool:
        """
        :raises TypeError: If the string parameter is not a str or container is not a list
        :raises NullOrEmptyAttribute: If any string is None or empty
        :return: If has any attribute equal in container
        """
        for e in self.attribute:
            if e.compare(attribute):
                return True
        return False

    @classmethod
    def initialize(cls, value) -> ListAttribute:
        if value is None or value == cls.undefined_value:
            return cls(cls.undefined_value)
        elif isinstance(value, cls):
            return value
        elif isinstance(value, cls.sub_attribute):
            return cls(value)
        elif isinstance(value, cls.attribute_type):
            return cls(value)
        elif isinstance(value, cls.sub_attribute.attribute_type):
            return cls(cls.sub_attribute(value))
        else:
            msg = f'Invalid type to property {cls.attribute_name}' \
                  f', expected {cls.__name__}, {cls.sub_attribute.__name__},' \
                  f' {cls.attribute_type} or {cls.sub_attribute.attribute_type}.'
            raise TypeError(msg)

    def validate(self) -> None:
        """
        It raises if any elements of container parameter is not a attribute
        :raises AttributeNotExists: If any string from container is a invalid attribute
        :raises TypeError: If container parameter is not a list
        :raises NullOrEmptyAttribute: If the any element of container is None or empty
        """
        for e in self.attribute:
            e.validate()
