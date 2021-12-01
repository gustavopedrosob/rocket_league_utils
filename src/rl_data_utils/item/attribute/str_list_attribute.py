from rl_data_utils.item.attribute.list_attribute import ListAttribute
from rl_data_utils.item.attribute.str_attribute import StrAttribute


class StrListAttribute(ListAttribute):
    sub_attribute = StrAttribute

    def has_exactly(self, name: str) -> bool:
        for e in self.attribute:
            if e.is_exactly(name):
                return True
        return False

    def get_respective(self, attribute) -> str:
        """
        Search for the respective inside a container
        :param container:
        :raises TypeError: If the string parameter is not a str or container is not a list
        :raises NullOrEmptyAttribute: If any string is None or empty
        :return: The respective string inside container
        """
        attribute = self.sub_attribute.initialize(attribute)
        for e in self.attribute:
            if attribute.compare(e):
                return e
