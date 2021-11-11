from rl_data_utils.item.blueprint.abc_base_blueprint import ABCBaseBlueprint
from rl_data_utils.item.item.item_attribute import ItemAttribute


class ABCBlueprint(ABCBaseBlueprint, ItemAttribute):
    pass


class Blueprint(ABCBlueprint):
    def __init__(self, blueprint: bool):
        self.blueprint = blueprint

    def get_blueprint(self) -> bool:
        return self.blueprint
