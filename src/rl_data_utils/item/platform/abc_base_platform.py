from abc import ABC, abstractmethod


class ABCBasePlatform(ABC):
    @abstractmethod
    def get_platform(self) -> str:
        pass

    @abstractmethod
    def is_pc(self) -> bool:
        pass

    @abstractmethod
    def is_xbox(self) -> bool:
        pass

    @abstractmethod
    def is_ps4(self) -> bool:
        pass

    @abstractmethod
    def is_switch(self) -> bool:
        pass

    @abstractmethod
    def validate_platform(self):
        pass

    @abstractmethod
    def compare_platforms(self, platform: str) -> bool:
        pass

    @abstractmethod
    def is_valid_platform(self) -> bool:
        pass
