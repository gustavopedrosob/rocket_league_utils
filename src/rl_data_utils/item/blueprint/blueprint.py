from abc import abstractmethod, ABC
from rl_data_utils.item.item.item_attribute import ItemAttribute


class ABCBlueprint(ABC, ItemAttribute):
    @abstractmethod
    def get_blueprint(self) -> bool:
        pass


class Blueprint(ABCBlueprint):
    def __init__(self, blueprint: bool):
        self.blueprint = blueprint

    def get_blueprint(self) -> bool:
        return self.blueprint
