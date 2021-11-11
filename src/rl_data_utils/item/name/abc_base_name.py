from abc import ABC, abstractmethod


class ABCBaseName(ABC):
    @abstractmethod
    def have_car_in_name(self) -> bool:
        pass

    @abstractmethod
    def is_credits(self) -> bool:
        pass

    @abstractmethod
    def compare_name(self, name: str) -> bool:
        pass

    @abstractmethod
    def get_decal_and_car_name(self):
        pass

    @abstractmethod
    def get_string_decal_and_car_name(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
