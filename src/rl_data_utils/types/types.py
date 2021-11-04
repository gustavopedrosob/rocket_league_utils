from rl_data_utils.item.abc_item import get_items_by_condition
from rl_data_utils.items.abc_items import ABCItems
from rl_data_utils.type.type import ABCType, validate_type
from rl_data_utils.__others import _regex_found
from re import IGNORECASE
from abc import abstractmethod


class ABCTypes(ABCItems):
    @abstractmethod
    def get_items_by_type_regex(self, type_pattern: str, flags=IGNORECASE):
        pass

    @abstractmethod
    def get_items_by_type(self, type_: str):
        pass

    @abstractmethod
    def get_items_by_type_equal_to(self, type_: str):
        pass

    @abstractmethod
    def get_items_by_type_contains(self, type_: str):
        pass

    @abstractmethod
    def get_types(self):
        pass

    @abstractmethod
    def get_items_antenna(self) -> bool:
        pass

    @abstractmethod
    def get_items_avatar_border(self) -> bool:
        pass

    @abstractmethod
    def get_items_banner(self) -> bool:
        pass

    @abstractmethod
    def get_items_boost(self) -> bool:
        pass

    @abstractmethod
    def get_items_car(self) -> bool:
        pass

    @abstractmethod
    def get_items_decal(self) -> bool:
        pass

    @abstractmethod
    def get_items_engine_audio(self) -> bool:
        pass

    @abstractmethod
    def get_items_gift_pack(self) -> bool:
        pass

    @abstractmethod
    def get_items_goal_explosion(self) -> bool:
        pass

    @abstractmethod
    def get_items_paint_finish(self) -> bool:
        pass

    @abstractmethod
    def get_items_player_anthem(self):
        pass

    @abstractmethod
    def get_items_topper(self) -> bool:
        pass

    @abstractmethod
    def get_items_trail(self) -> bool:
        pass

    @abstractmethod
    def get_items_wheel(self) -> bool:
        pass


class ABCStrTypes(ABCTypes):
    def get_items_by_type_regex(self, type_pattern: str, flags=IGNORECASE):
        return get_items_by_type_regex(type_pattern, self.get_items(), flags)

    def get_items_by_type(self, type_: str):
        return get_items_by_type(type_, self.get_items())

    def get_items_by_type_equal_to(self, type_: str):
        return get_items_by_type_equal_to(type_, self.get_items())

    def get_items_by_type_contains(self, type_: str):
        return get_items_by_type_contains(type_, self.get_items())

    def get_types(self):
        return get_types(self.get_items())

    def get_items_antenna(self) -> bool:
        return get_items_antenna(self.get_items())

    def get_items_avatar_border(self) -> bool:
        return get_items_avatar_border(self.get_items())

    def get_items_banner(self) -> bool:
        return get_items_banner(self.get_items())

    def get_items_boost(self) -> bool:
        return get_items_boost(self.get_items())

    def get_items_car(self) -> bool:
        return get_items_car(self.get_items())

    def get_items_decal(self) -> bool:
        return get_items_decal(self.get_items())

    def get_items_engine_audio(self) -> bool:
        return get_items_engine_audio(self.get_items())

    def get_items_gift_pack(self) -> bool:
        return get_items_gift_pack(self.get_items())

    def get_items_goal_explosion(self) -> bool:
        return get_items_goal_explosion(self.get_items())

    def get_items_paint_finish(self) -> bool:
        return get_items_paint_finish(self.get_items())

    def get_items_player_anthem(self):
        return get_items_player_anthem(self.get_items())

    def get_items_topper(self) -> bool:
        return get_items_topper(self.get_items())

    def get_items_trail(self) -> bool:
        return get_items_trail(self.get_items())

    def get_items_wheel(self) -> bool:
        return get_items_wheel(self.get_items())


def get_items_by_type_regex(type_pattern: str, items: list[ABCType], flags=IGNORECASE):
    return get_items_by_condition(lambda item: _regex_found(type_pattern, item.get_type(), flags), items)


def get_types(items: list[ABCType]):
    return {item.get_type() for item in items}


def get_items_by_type(type_: str, items: list[ABCType]):
    validate_type(type_)
    return get_items_by_condition(lambda item: item.compare_types(type_), items)


def get_items_by_type_equal_to(type_: str, items: list[ABCType]):
    return get_items_by_condition(lambda item: item.get_type() == type_, items)


def get_items_by_type_contains(type_: str, items: list[ABCType]):
    return get_items_by_condition(lambda item: type_ in item.get_type(), items)


def get_items_antenna(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_antenna(), items)


def get_items_avatar_border(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_avatar_border(), items)


def get_items_banner(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_banner(), items)


def get_items_boost(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_boost(), items)


def get_items_car(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_car(), items)


def get_items_decal(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_decal(), items)


def get_items_engine_audio(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_engine_audio(), items)


def get_items_gift_pack(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_gift_pack(), items)


def get_items_goal_explosion(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_goal_explosion(), items)


def get_items_paint_finish(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_paint_finish(), items)


def get_items_player_anthem(items: list[ABCType]):
    return get_items_by_condition(lambda item: item.is_player_anthem(), items)


def get_items_topper(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_topper(), items)


def get_items_trail(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_trail(), items)


def get_items_wheel(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_wheel(), items)
