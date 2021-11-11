from abc import ABC, abstractmethod


class ABCBaseBlueprint(ABC):
    @abstractmethod
    def get_blueprint(self) -> bool:
        pass
