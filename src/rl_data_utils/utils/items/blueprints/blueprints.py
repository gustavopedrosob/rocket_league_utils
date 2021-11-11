from rl_data_utils.item.blueprint.blueprint import ABCBlueprint
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_not_blueprint(items: list[ABCBlueprint]):
    return get_items_by_condition(lambda item: item.get_blueprint(), items)


def get_items_blueprint(items: list[ABCBlueprint]):
    return get_items_by_condition(lambda item: not item.get_blueprint(), items)
