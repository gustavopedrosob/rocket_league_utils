from rl_data_utils.items.blueprints.abc_base_blueprints import ABCBaseBlueprints
from rl_data_utils.items.items.items import Items
from rl_data_utils.utils.items.blueprints.blueprints import get_items_not_blueprint, get_items_blueprint,\
    get_items_by_blueprint


class Blueprints(ABCBaseBlueprints, Items):
    def get_items_by_blueprint(self, blueprint: bool):
        return self.__class__(get_items_by_blueprint(blueprint, self.items))

    def get_items_not_blueprint(self):
        return self.__class__(get_items_not_blueprint(self.items))

    def get_items_blueprint(self):
        return self.__class__(get_items_blueprint(self.items))
