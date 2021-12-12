from contextlib import suppress

from re import search, IGNORECASE

from typing import Type, Dict

from rl_data_utils.exceptions import IsNotInString
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedAttribute
from rl_data_utils.item.attribute.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.attribute_string.attribute_string import AttributeString


class RegexBasedAttributeString(AttributeString):
    attribute_class: Type[RegexBasedAttribute]
    attributes_class: Type[RegexBasedListAttribute]
    contains_reg: Dict[str, str]
    is_not_in_string_exception: Type[Exception]

    def contains(self) -> bool:
        """
        It says if contains an attribute
        :return: If self string match with any regex in contains_reg
        """
        try:
            _ = self.get()
        except IsNotInString:
            return False
        else:
            return True

    def contains_exactly(self, pattern_key: str) -> bool:
        """
        It says if contains a specific attribute
        :param pattern_key: It's a key to a pattern regex
        :raise KeyError: If the pattern_key is invalid
        :return: If self string match with a specific regex given by pattern_key
        """
        try:
            _ = self.get_exactly(pattern_key)
        except IsNotInString:
            return False
        else:
            return True

    def get(self) -> RegexBasedAttribute:
        """
        Gets an attribute
        :raise IsNotInString: If any regex doesn't match
        :return: A attribute found
        """
        for key in self.contains_reg:
            with suppress(self.is_not_in_string_exception):
                return self.get_exactly(key)
        raise self.is_not_in_string_exception

    def get_exactly(self, pattern_key: str) -> RegexBasedAttribute:
        """
        Gets a specific attribute
        :param pattern_key: It's a key to a pattern regex
        :raise IsNotInString: If regex doesn't match
        :raise KeyError: If the pattern_key is invalid
        :return: A specific attribute found
        """
        try:
            return self.attribute_class(search(self.contains_reg[pattern_key], self.string, IGNORECASE).group(0))
        except AttributeError:
            raise self.is_not_in_string_exception

    def get_respective(self) -> RegexBasedAttribute:
        """
        Gets an attribute and then transform it to his respective
        :raise IsNotInString: If regex doesn't match
        :return: A respective attribute found
        """
        return self.attributes_class.create_default().get_respective(self.get())

    def get_exactly_respective(self, pattern_key: str) -> RegexBasedAttribute:
        """
        Gets a specific attribute and then transform it to his respective
        :param pattern_key: It's a key to a pattern regex
        :raise IsNotInString: If regex doesn't match
        :raise KeyError: If the pattern_key is invalid
        :return: A specific respective attribute found
        """
        return self.attributes_class.create_default().get_respective(self.get_exactly(pattern_key))
