from abc import abstractmethod, ABC
from rl_data_utils.item.item.item_attribute import ItemAttribute
from rl_data_utils.utils.item.platform.is_functions import is_pc, is_xbox, is_ps4, is_switch
from rl_data_utils.utils.item.platform.platform import validate_platform, compare_platforms, is_platform


class ABCPlatform(ABC, ItemAttribute):
    def is_pc(self) -> bool:
        return is_pc(self.get_platform())

    def is_xbox(self) -> bool:
        return is_xbox(self.get_platform())

    def is_ps4(self) -> bool:
        return is_ps4(self.get_platform())

    def is_switch(self) -> bool:
        return is_switch(self.get_platform())

    def validate_platform(self):
        validate_platform(self.get_platform())

    def compare_platforms(self, platform: str) -> bool:
        return compare_platforms(self.get_platform(), platform)

    def is_valid_platform(self) -> bool:
        return is_platform(self.get_platform())

    @abstractmethod
    def get_platform(self) -> str:
        pass


class Platform(ABCPlatform):
    def __init__(self, platform: str):
        self.platform = platform

    def get_platform(self) -> str:
        return self.platform
