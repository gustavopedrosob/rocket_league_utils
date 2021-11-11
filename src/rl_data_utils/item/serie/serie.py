from rl_data_utils.item.item.item_attribute import ItemAttribute
from rl_data_utils.item.serie.abc_base_serie import ABCBaseSerie
from rl_data_utils.utils.item.serie.is_functions import *


class ABCSerie(ABCBaseSerie, ItemAttribute):
    def is_accelerator_series(self) -> bool:
        return is_accelerator_series(self.get_serie())

    def is_beach_blast_series(self) -> bool:
        return is_beach_blast_series(self.get_serie())

    def is_bonus_gift(self) -> bool:
        return is_bonus_gift(self.get_serie())

    def is_champions_1_series(self) -> bool:
        return is_champions_1_series(self.get_serie())

    def is_champions_2_series(self) -> bool:
        return is_champions_2_series(self.get_serie())

    def is_champions_3_series(self) -> bool:
        return is_champions_3_series(self.get_serie())

    def is_champions_4_series(self) -> bool:
        return is_champions_4_series(self.get_serie())

    def is_elevation_series(self) -> bool:
        return is_elevation_series(self.get_serie())

    def is_ferocity_series(self) -> bool:
        return is_ferocity_series(self.get_serie())

    def is_golden_egg_2018(self) -> bool:
        return is_golden_egg_2018(self.get_serie())

    def is_golden_egg_2019(self) -> bool:
        return is_golden_egg_2019(self.get_serie())

    def is_golden_egg_2020(self) -> bool:
        return is_golden_egg_2020(self.get_serie())

    def is_golden_gift_2018(self) -> bool:
        return is_golden_gift_2018(self.get_serie())

    def is_golden_gift_2019(self) -> bool:
        return is_golden_gift_2019(self.get_serie())

    def is_golden_gift_2020(self) -> bool:
        return is_golden_gift_2020(self.get_serie())

    def is_golden_lantern_2020(self) -> bool:
        return is_golden_lantern_2020(self.get_serie())

    def is_golden_lantern_2021(self) -> bool:
        return is_golden_lantern_2021(self.get_serie())

    def is_golden_pumpkin_2018(self) -> bool:
        return is_golden_pumpkin_2018(self.get_serie())

    def is_golden_pumpkin_2019(self) -> bool:
        return is_golden_pumpkin_2019(self.get_serie())

    def is_golden_pumpkin_2020(self) -> bool:
        return is_golden_pumpkin_2020(self.get_serie())

    def is_haunted_hallows_series(self) -> bool:
        return is_haunted_hallows_series(self.get_serie())

    def is_impact_series(self) -> bool:
        return is_impact_series(self.get_serie())

    def is_nitro_series(self) -> bool:
        return is_nitro_series(self.get_serie())

    def is_overdrive_series(self) -> bool:
        return is_overdrive_series(self.get_serie())

    def is_players_choice_series(self) -> bool:
        return is_players_choice_series(self.get_serie())

    def is_secret_santa_series(self) -> bool:
        return is_secret_santa_series(self.get_serie())

    def is_spring_fever_series(self) -> bool:
        return is_spring_fever_series(self.get_serie())

    def is_totally_awesome_series(self) -> bool:
        return is_totally_awesome_series(self.get_serie())

    def is_triumph_series(self) -> bool:
        return is_triumph_series(self.get_serie())

    def is_turbo_series(self) -> bool:
        return is_turbo_series(self.get_serie())

    def is_velocity_series(self) -> bool:
        return is_velocity_series(self.get_serie())

    def is_victory_series(self) -> bool:
        return is_victory_series(self.get_serie())

    def is_vindicator_series(self) -> bool:
        return is_vindicator_series(self.get_serie())

    def is_zephyr_series(self) -> bool:
        return is_zephyr_series(self.get_serie())


class Serie(ABCSerie):
    def __init__(self, serie: str):
        self.serie = serie

    def get_serie(self) -> str:
        return self.serie
