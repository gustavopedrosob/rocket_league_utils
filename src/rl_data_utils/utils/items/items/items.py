from rl_data_utils.__others import filter_container_by_condition
from rl_data_utils.exceptions import ItemNotFound


def get_items_by_condition(lamb, items):
    return filter_container_by_condition(lamb, items)


def get_list_sample(func_name, items):
    result = set()
    for item in items:
        result.update(getattr(item, func_name)())
    return result


def get_item_by_index(items, index=0):
    try:
        return items[index]
    except IndexError:
        raise ItemNotFound("Probably your search results in nothing.")
