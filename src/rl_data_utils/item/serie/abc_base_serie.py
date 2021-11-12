from abc import ABC, abstractmethod


class ABCBaseSerie(ABC):
    @abstractmethod
    def is_valid_serie(self):
        pass

    @abstractmethod
    def get_serie(self) -> str:
        pass

    @abstractmethod
    def is_accelerator_series(self) -> bool:
        pass

    @abstractmethod
    def is_beach_blast_series(self) -> bool:
        pass

    @abstractmethod
    def is_bonus_gift(self) -> bool:
        pass

    @abstractmethod
    def is_champions_1_series(self) -> bool:
        pass

    @abstractmethod
    def is_champions_2_series(self) -> bool:
        pass

    @abstractmethod
    def is_champions_3_series(self) -> bool:
        pass

    @abstractmethod
    def is_champions_4_series(self) -> bool:
        pass

    @abstractmethod
    def is_elevation_series(self) -> bool:
        pass

    @abstractmethod
    def is_ferocity_series(self) -> bool:
        pass

    @abstractmethod
    def is_golden_egg_2018(self) -> bool:
        pass

    @abstractmethod
    def is_golden_egg_2019(self) -> bool:
        pass

    @abstractmethod
    def is_golden_egg_2020(self) -> bool:
        pass

    @abstractmethod
    def is_golden_gift_2018(self) -> bool:
        pass

    @abstractmethod
    def is_golden_gift_2019(self) -> bool:
        pass

    @abstractmethod
    def is_golden_gift_2020(self) -> bool:
        pass

    @abstractmethod
    def is_golden_lantern_2020(self) -> bool:
        pass

    @abstractmethod
    def is_golden_lantern_2021(self) -> bool:
        pass

    @abstractmethod
    def is_golden_pumpkin_2018(self) -> bool:
        pass

    @abstractmethod
    def is_golden_pumpkin_2019(self) -> bool:
        pass

    @abstractmethod
    def is_golden_pumpkin_2020(self) -> bool:
        pass

    @abstractmethod
    def is_haunted_hallows_series(self) -> bool:
        pass

    @abstractmethod
    def is_impact_series(self) -> bool:
        pass

    @abstractmethod
    def is_nitro_series(self) -> bool:
        pass

    @abstractmethod
    def is_overdrive_series(self) -> bool:
        pass

    @abstractmethod
    def is_players_choice_series(self) -> bool:
        pass

    @abstractmethod
    def is_secret_santa_series(self) -> bool:
        pass

    @abstractmethod
    def is_spring_fever_series(self) -> bool:
        pass

    @abstractmethod
    def is_totally_awesome_series(self) -> bool:
        pass

    @abstractmethod
    def is_triumph_series(self) -> bool:
        pass

    @abstractmethod
    def is_turbo_series(self) -> bool:
        pass

    @abstractmethod
    def is_velocity_series(self) -> bool:
        pass

    @abstractmethod
    def is_victory_series(self) -> bool:
        pass

    @abstractmethod
    def is_vindicator_series(self) -> bool:
        pass

    @abstractmethod
    def is_zephyr_series(self) -> bool:
        pass
