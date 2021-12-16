from typing import Union, Final

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.bool_attribute import BoolAttribute, SetBoolAttribute


class BlueprintInfo(AttributeInfo):
    attribute_name: Final[str] = 'blueprint'
    order: Final[int] = 11


class Blueprint(BoolAttribute, BlueprintInfo):
    default_value = False


InitializeBlueprint = Union[Blueprint, bool, None]


class HasBlueprint(BlueprintInfo):
    def __init__(self, blueprint: InitializeBlueprint = None):
        self.blueprint: Blueprint = blueprint

    def get_blueprint(self) -> Blueprint:
        return self._blueprint

    def set_blueprint(self, value: SetBoolAttribute):
        self._blueprint = Blueprint.initialize(value)

    blueprint = property(get_blueprint, set_blueprint)
