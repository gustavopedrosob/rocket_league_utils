from abc import ABC, abstractmethod
from re import IGNORECASE


class ABCBaseSeries(ABC):
    @abstractmethod
    def get_items_with_valid_serie(self):
        pass

    @abstractmethod
    def get_items_by_serie_regex(self, serie_pattern, flags=IGNORECASE):
        pass

    @abstractmethod
    def get_items_by_serie(self, serie: str):
        pass

    @abstractmethod
    def get_items_by_serie_equal_to(self, serie: str):
        pass

    @abstractmethod
    def get_items_by_serie_contains(self, serie: str):
        pass

    @abstractmethod
    def get_series(self):
        pass
    
    @abstractmethod
    def get_items_accelerator_series(self):
        pass

    @abstractmethod
    def get_items_beach_blast_series(self):
        pass

    @abstractmethod
    def get_items_bonus_gift(self):
        pass

    @abstractmethod
    def get_items_champions_1_series(self):
        pass

    @abstractmethod
    def get_items_champions_2_series(self):
        pass

    @abstractmethod
    def get_items_champions_3_series(self):
        pass

    @abstractmethod
    def get_items_champions_4_series(self):
        pass

    @abstractmethod
    def get_items_elevation_series(self):
        pass

    @abstractmethod
    def get_items_ferocity_series(self):
        pass

    @abstractmethod
    def get_items_golden_egg_2018(self):
        pass

    @abstractmethod
    def get_items_golden_egg_2019(self):
        pass

    @abstractmethod
    def get_items_golden_egg_2020(self):
        pass

    @abstractmethod
    def get_items_golden_gift_2018(self):
        pass

    @abstractmethod
    def get_items_golden_gift_2019(self):
        pass

    @abstractmethod
    def get_items_golden_gift_2020(self):
        pass

    @abstractmethod
    def get_items_golden_lantern_2020(self):
        pass

    @abstractmethod
    def get_items_golden_lantern_2021(self):
        pass

    @abstractmethod
    def get_items_golden_pumpkin_2018(self):
        pass

    @abstractmethod
    def get_items_golden_pumpkin_2019(self):
        pass

    @abstractmethod
    def get_items_golden_pumpkin_2020(self):
        pass

    @abstractmethod
    def get_items_haunted_hallows_series(self):
        pass

    @abstractmethod
    def get_items_impact_series(self):
        pass

    @abstractmethod
    def get_items_nitro_series(self):
        pass

    @abstractmethod
    def get_items_overdrive_series(self):
        pass

    @abstractmethod
    def get_items_players_choice_series(self):
        pass

    @abstractmethod
    def get_items_secret_santa_series(self):
        pass

    @abstractmethod
    def get_items_spring_fever_series(self):
        pass

    @abstractmethod
    def get_items_totally_awesome_series(self):
        pass

    @abstractmethod
    def get_items_triumph_series(self):
        pass

    @abstractmethod
    def get_items_turbo_series(self):
        pass

    @abstractmethod
    def get_items_velocity_series(self):
        pass

    @abstractmethod
    def get_items_victory_series(self):
        pass

    @abstractmethod
    def get_items_vindicator_series(self):
        pass

    @abstractmethod
    def get_items_zephyr_series(self):
        pass
