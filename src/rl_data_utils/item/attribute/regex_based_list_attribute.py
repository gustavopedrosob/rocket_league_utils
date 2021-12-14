from typing import Union, Optional, Type, List

from rl_data_utils.item.attribute.list_attribute import ListAttribute
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedAttribute, InitializeRegexBasedAttribute

SetRegexBasedListAttribute = Optional[List[InitializeRegexBasedAttribute]]


class RegexBasedListAttribute(ListAttribute):
    sub_attribute: Type[RegexBasedAttribute] = RegexBasedAttribute

    def has_exactly(self, pattern_key: str) -> bool:
        """
        Compares all attributes with a regex given by pattern_key
        :param pattern_key: It's a key to a pattern regex
        :raise KeyError: If the pattern_key is invalid
        :return: If any attribute match with the regex
        """
        return any(a.is_exactly(pattern_key) for a in self.attribute)

    def get_respective(self, attribute: InitializeRegexBasedAttribute) -> Optional[RegexBasedAttribute]:
        """
        Search for a respective attribute in the attributes
        :param attribute: An attribute to find his pair
        :return: An pair attribute found in the attributes
        """
        attribute = self.sub_attribute.initialize(attribute)
        for e in self.attribute:
            if attribute.compare(e):
                return e


InitializeRegexBasedListAttribute = Union[RegexBasedListAttribute, List[InitializeRegexBasedAttribute], None]
