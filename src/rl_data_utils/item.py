from rl_data_utils.colors.colors import Color
from rl_data_utils.types.types import Type
from rl_data_utils.rarities.rarities import Rarity
from rl_data_utils.certificates.certificates import Certified
from rl_data_utils.names.names import Name


def compare_items(item_1, item_2):
    from rl_data_utils.certificates.certificates import compare_certificates
    from rl_data_utils.colors.colors import compare_colors
    from rl_data_utils.names.names import compare_names
    from rl_data_utils.rarities.rarities import compare_rarities
    from rl_data_utils.types.types import compare_types
    for key, function in [('certified', compare_certificates), ('color', compare_colors), ('name', compare_names),
                          ('rarity', compare_rarities), ('type', compare_types)]:
        item_1_value = getattr(item_1, key)
        item_2_value = getattr(item_2, key)
        if item_1_value and item_2_value:
            if not function(item_1_value, item_2_value):
                return False
    return True


def get_attributes_in_string(string: str) -> dict:
    from rl_data_utils.certificates.certificates import get_certified_in_string
    from rl_data_utils.colors.colors import get_color_in_string
    from rl_data_utils.rarities.rarities import get_rarity_in_string
    from rl_data_utils.types.types import get_type_in_string
    response = {}
    for function, key in [(get_certified_in_string, 'certified'), (get_color_in_string, 'color'),
                          (get_rarity_in_string, 'rarity'), (get_type_in_string, 'type_')]:
        result = function(string)
        if result:
            string = string.replace(result, '')
            response[key] = result
    name = string.strip()
    response['name'] = name
    return response


def get_respective_attributes_in_string(string: str) -> dict:
    from rl_data_utils.certificates.certificates import get_respective_certified
    from rl_data_utils.colors.colors import get_respective_color
    from rl_data_utils.rarities.rarities import get_respective_rarity
    from rl_data_utils.types.types import get_respective_type
    response = get_attributes_in_string(string)
    for function, key in [(get_respective_certified, 'certified'), (get_respective_color, 'color'),
                          (get_respective_rarity, 'rarity'), (get_respective_type, 'type_')]:
        if key in response:
            response[key] = function(response[key])
    return response


def validate_attributes(color: str = None, type_: str = None, rarity: str = None, certified: str = None):
    from rl_data_utils.certificates.certificates import validate_certified
    from rl_data_utils.colors.colors import validate_color
    from rl_data_utils.rarities.rarities import validate_rarity
    from rl_data_utils.types.types import validate_type
    if color:
        validate_color(color)
    if type_:
        validate_type(type_)
    if rarity:
        validate_rarity(rarity)
    if certified:
        validate_certified(certified)


class Item(Name, Color, Type, Rarity, Certified):
    def __init__(self, name: str, color: str = "", type_: str = "", rarity: str = "", certified: str = ""):
        self.name = name
        self.color = color
        self.type = type_
        self.rarity = rarity
        self.certified = certified

    def validate(self):
        validate_attributes(self.color, self.type, self.rarity, self.certified)

    def __eq__(self, other):
        if isinstance(other, Item):
            return compare_items(self, other)
        else:
            return False

    @staticmethod
    def from_string(string: str):
        return Item(**get_attributes_in_string(string))
