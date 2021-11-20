from rl_data_utils.exceptions import IsNotInString
from rl_data_utils.utils.item.certified.certified import get_certified_in_string, get_respective_certified,\
    validate_certified
from rl_data_utils.utils.item.certified.is_functions import is_none
from rl_data_utils.utils.item.color.color import get_color_in_string, get_respective_color, validate_color
from rl_data_utils.utils.item.color.is_functions import is_default
from rl_data_utils.utils.item.rarity.rarity import get_rarity_in_string, get_respective_rarity, validate_rarity
from rl_data_utils.utils.item.slot.slot import get_slot_in_string, get_respective_slot, validate_slot


def get_attributes_in_string(string: str) -> dict:
    response = {}
    for function, key in [(get_certified_in_string, 'certified'), (get_color_in_string, 'color'),
                          (get_rarity_in_string, 'rarity'), (get_slot_in_string, 'type_')]:
        try:
            result = function(string)
        except IsNotInString:
            pass
        else:
            string = string.replace(result, '')
            response[key] = result
    name = string.strip()
    if name:
        response['name'] = name
    return response


def get_respective_attributes_in_string(string: str) -> dict:
    response = get_attributes_in_string(string)
    for function, key in [(get_respective_certified, 'certified'), (get_respective_color, 'color'),
                          (get_respective_rarity, 'rarity'), (get_respective_slot, 'type_')]:
        if key in response:
            response[key] = function(response[key])
    return response


def validate_attributes(**kwargs):
    if 'color' in kwargs:
        validate_color(kwargs.get('color'))
    if 'type_' in kwargs:
        validate_slot(kwargs.get('type_'))
    if 'rarity' in kwargs:
        validate_rarity(kwargs.get('rarity'))
    if 'certified' in kwargs:
        validate_certified(kwargs.get('certified'))


def get_repr(**kwargs):
    attributes = []
    if 'quantity' in kwargs:
        quantity = kwargs.get('quantity')
        if quantity > 1:
            attributes.append(str(quantity))
    if 'color' in kwargs:
        color = kwargs.get('color')
        if color and not is_default(color):
            attributes.append(color)
    if 'rarity' in kwargs:
        attributes.append(kwargs.get('rarity'))
    if 'type_' in kwargs:
        attributes.append(kwargs.get('type_'))
    if 'certified' in kwargs:
        certified = kwargs.get('certified')
        if certified and not is_none(certified):
            attributes.append(certified)
    if 'name' in kwargs:
        attributes.append(kwargs.get('name'))
    return ' '.join(attributes)

