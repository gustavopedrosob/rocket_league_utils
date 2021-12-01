from rl_data_utils.exceptions import InvalidCreditsQuantity
from rl_data_utils.item.attribute.int_attribute import IntAttribute
from rl_data_utils.item.quantity.quantity_info import QuantityInfo


class CreditsQuantity(IntAttribute, QuantityInfo):
    def is_valid(self):
        try:
            self.validate()
        except InvalidCreditsQuantity:
            return False
        else:
            return True

    def validate(self):
        if self.attribute % 10 > 0:
            raise InvalidCreditsQuantity()
