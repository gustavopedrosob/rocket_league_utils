from abc import ABC, abstractmethod


class ABCBaseBlueprints(ABC):
    @abstractmethod
    def get_items_blueprint(self):
        pass

    @abstractmethod
    def get_items_not_blueprint(self):
        pass
