from __future__ import annotations

from abc import abstractmethod, ABCMeta

from rl_data_utils.exceptions import InvalidItemAttribute
from rl_data_utils.item.attribute.attribute import ItemAttribute
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject, Validable, Comparable, CanBeEmpty, Contains, \
    Identifiable


class HasAttributes(Validable, Comparable, CanBeEmpty, Contains):
    @abstractmethod
    def get_attributes(self):
        pass

    def is_empty(self):
        return len(self.get_attributes()) == 0

    def is_valid(self):
        return self._is_valid_by_validate(InvalidItemAttribute)

    def validate(self):
        for attr in self.get_attributes():
            if isinstance(attr, Validable):
                attr.validate()


class AttributesData(RocketLeagueObject, HasAttributes, Identifiable, metaclass=ABCMeta):
    pass


class AttributesManagement(HasAttributes):
    def __init__(self, attributes):
        self.attributes = attributes

    def compare(self, other, condition=None) -> bool:
        if condition:
            return all(other.has(attr) for attr in self.attributes if condition(attr))
        else:
            return all(other.has(attr) for attr in self.attributes)

    def get_attributes(self):
        return self.attributes

    def get_respective(self, other):
        for attr in self.attributes:
            if other.compare(attr):
                return attr
        return None

    def has(self, attribute) -> bool:
        return any(attr.compare(attribute) for attr in self.attributes)


class AttributesCollectionManagement(HasAttributes):
    def compare(self, other, condition=None):
        if self.is_empty():
            return False
        elif condition:
            return all(getattr(other, k).compare(attr)
                       for k, attr in self.get_attributes_dict().items() if condition(attr))
        else:
            return all(getattr(other, k).compare(attr) for k, attr in self.get_attributes_dict().items())

    def get_attributes(self):
        return tuple(self.get_attributes_dict().values())

    def get_attributes_dict(self):
        return {k: v for k, v in self.__dict__.items()
                if v and (isinstance(v, ItemAttribute) or isinstance(v, AttributesData))}

    def has(self, attribute):
        our_attr = getattr(self, attribute.identifier)
        return attribute.compare(our_attr)
