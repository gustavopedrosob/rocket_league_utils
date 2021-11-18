from abc import abstractmethod, ABC


class ABCBasePlatforms(ABC):
    @abstractmethod
    def get_items_pc(self):
        pass

    @abstractmethod
    def get_items_ps4(self):
        pass

    @abstractmethod
    def get_items_xbox(self):
        pass

    @abstractmethod
    def get_items_switch(self):
        pass
