from contextlib import suppress
from re import search

from rl_data_utils.exceptions import IsNotInString


class AttributeString:
    def __init__(self, attribute_string, string):
        self.attribute_string = attribute_string
        self.string = string

    def get(self):
        """
        Gets an attribute
        :return: A attribute found
        """
        for key in self.attribute_string.regex_table:
            with suppress(IsNotInString):
                return self.get_exactly(key)
        raise IsNotInString()

    def get_exactly(self, pattern_key):
        """
        Gets a specific attribute
        :param pattern_key: It's a key to a pattern regex
        :raise IsNotInString: If regex doesn't match
        :raise KeyError: If the pattern_key is invalid
        :return: A specific attribute found
        """
        match = search(self.attribute_string.regex_table[pattern_key], self.string)
        if match:
            return self.attribute_string(match.group(0))
        raise IsNotInString()
