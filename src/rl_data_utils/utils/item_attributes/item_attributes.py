from rl_data_utils.utils.item.certified.certified import get_certified_in_string, get_respective_certified,\
    validate_certified
from rl_data_utils.utils.item.color.color import get_color_in_string, get_respective_color, validate_color
from rl_data_utils.utils.item.rarity.rarity import get_rarity_in_string, get_respective_rarity, validate_rarity
from rl_data_utils.utils.item.type.type import get_type_in_string, get_respective_type, validate_type


def get_attributes_in_string(string: str) -> dict:
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
    response = get_attributes_in_string(string)
    for function, key in [(get_respective_certified, 'certified'), (get_respective_color, 'color'),
                          (get_respective_rarity, 'rarity'), (get_respective_type, 'type_')]:
        if key in response:
            response[key] = function(response[key])
    return response


def validate_attributes(color: str = None, type_: str = None, rarity: str = None, certified: str = None):
    if color:
        validate_color(color)
    if type_:
        validate_type(type_)
    if rarity:
        validate_rarity(rarity)
    if certified:
        validate_certified(certified)
