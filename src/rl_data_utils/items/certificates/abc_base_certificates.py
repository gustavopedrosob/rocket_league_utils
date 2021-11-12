from abc import ABC, abstractmethod
from re import IGNORECASE


class ABCBaseCertificates(ABC):
    @abstractmethod
    def get_items_with_valid_certified(self):
        pass

    @abstractmethod
    def get_items_by_certified_regex(self, certified_pattern, flags=IGNORECASE):
        pass

    @abstractmethod
    def get_items_by_certified(self, certified: str):
        pass

    @abstractmethod
    def get_items_by_certified_equal_to(self, certified: str):
        pass

    @abstractmethod
    def get_items_by_certified_contains(self, certified: str):
        pass

    @abstractmethod
    def get_certificates(self):
        pass

    @abstractmethod
    def get_items_aviator(self):
        pass

    @abstractmethod
    def get_items_acrobat(self):
        pass

    @abstractmethod
    def get_items_victor(self):
        pass

    @abstractmethod
    def get_items_striker(self):
        pass

    @abstractmethod
    def get_items_sniper(self):
        pass

    @abstractmethod
    def get_items_scorer(self):
        pass

    @abstractmethod
    def get_items_playmaker(self):
        pass

    @abstractmethod
    def get_items_guardian(self):
        pass

    @abstractmethod
    def get_items_paragon(self):
        pass

    @abstractmethod
    def get_items_sweeper(self):
        pass

    @abstractmethod
    def get_items_turtle(self):
        pass

    @abstractmethod
    def get_items_tactician(self):
        pass

    @abstractmethod
    def get_items_showoff(self):
        pass

    @abstractmethod
    def get_items_juggler(self):
        pass

    @abstractmethod
    def get_items_goalkeeper(self):
        pass
