from contextlib import suppress
from re import search, IGNORECASE
from rl_data_utils.item.attribute.str_attribute import StrAttribute


class AttributeString:
    attribute_class: StrAttribute.__class__
    contains_reg: dict
    is_not_in_string_exception: Exception

    def __init__(self, string):
        self.string = string

    def contains(self) -> bool:
        """
        Says if has a attribute inside the string
        :raises IsNotInString: If it don't found a attribute inside string
        :raises TypeError: If the string parameter is not a str
        :raises NullOrEmptyAttribute: If the string parameter is None or empty
        :return: If string parameter contains a attribute
        """
        for key in self.contains_reg:
            if self.contains_exactly(key):
                return True
        return False

    def contains_exactly(self, attribute: str) -> bool:
        return bool(search(self.contains_reg[attribute], self.string, IGNORECASE))

    def get(self) -> StrAttribute:
        for key in self.contains_reg:
            with suppress(self.is_not_in_string_exception):
                return self.get_exactly(key)
        raise self.is_not_in_string_exception

    def get_exactly(self, attribute: str) -> StrAttribute:
        try:
            return self.attribute_class(search(self.contains_reg[attribute], self.string, IGNORECASE).group(0))
        except AttributeError:
            raise self.is_not_in_string_exception
