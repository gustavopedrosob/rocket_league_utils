from abc import ABC, abstractmethod


class ABCBaseCertified(ABC):
    @abstractmethod
    def is_valid_certified(self):
        pass

    @abstractmethod
    def compare_certificates(self, certified: str) -> bool:
        pass

    @abstractmethod
    def get_respective_certified(self) -> str:
        pass

    @abstractmethod
    def is_acrobat(self) -> bool:
        pass

    @abstractmethod
    def is_aviator(self) -> bool:
        pass

    @abstractmethod
    def is_goalkeeper(self) -> bool:
        pass

    @abstractmethod
    def is_guardian(self) -> bool:
        pass

    @abstractmethod
    def is_juggler(self) -> bool:
        pass

    @abstractmethod
    def is_paragon(self) -> bool:
        pass

    @abstractmethod
    def is_playmaker(self) -> bool:
        pass

    @abstractmethod
    def is_scorer(self) -> bool:
        pass

    @abstractmethod
    def is_show_off(self) -> bool:
        pass

    @abstractmethod
    def is_sniper(self) -> bool:
        pass

    @abstractmethod
    def is_striker(self) -> bool:
        pass

    @abstractmethod
    def is_sweeper(self) -> bool:
        pass

    @abstractmethod
    def is_tactician(self) -> bool:
        pass

    @abstractmethod
    def is_turtle(self) -> bool:
        pass

    @abstractmethod
    def is_victor(self) -> bool:
        pass

    @abstractmethod
    def is_none(self) -> bool:
        pass

    @abstractmethod
    def validate_certified(self):
        pass

    @abstractmethod
    def get_certified(self):
        pass
