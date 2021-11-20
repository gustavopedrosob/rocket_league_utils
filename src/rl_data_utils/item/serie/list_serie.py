from abc import abstractmethod
from rl_data_utils.exceptions import ItemHaveNotSerie
from rl_data_utils.item.item.item_data import ItemDataAttribute
from rl_data_utils.utils.item.serie.series import get_respective_serie, validate_serie_list, all_are_series, has_serie
from rl_data_utils.utils.item.serie.has_functions import *


class ABCListSerie(ItemDataAttribute):
    @abstractmethod
    def get_list_serie(self) -> list[str]:
        pass

    def contains_serie(self, serie: str):
        return has_serie(serie, self.get_list_serie())

    def validate_contains_serie(self, serie: str):
        if not self.contains_serie(serie):
            raise ItemHaveNotSerie(serie)

    def has_valid_serie_list(self):
        return all_are_series(self.get_list_serie())

    def validate_serie_list(self):
        validate_serie_list(self.get_list_serie())

    def get_respective_serie(self, serie: str):
        return get_respective_serie(serie, self.get_list_serie())
    
    def has_accelerator_series(self) -> bool:
        return has_accelerator_series(self.get_list_serie())

    def has_beach_blast_series(self) -> bool:
        return has_beach_blast_series(self.get_list_serie())

    def has_bonus_gift(self) -> bool:
        return has_bonus_gift(self.get_list_serie())

    def has_champions_1_series(self) -> bool:
        return has_champions_1_series(self.get_list_serie())

    def has_champions_2_series(self) -> bool:
        return has_champions_2_series(self.get_list_serie())

    def has_champions_3_series(self) -> bool:
        return has_champions_3_series(self.get_list_serie())

    def has_champions_4_series(self) -> bool:
        return has_champions_4_series(self.get_list_serie())

    def has_elevation_series(self) -> bool:
        return has_elevation_series(self.get_list_serie())

    def has_ferocity_series(self) -> bool:
        return has_ferocity_series(self.get_list_serie())

    def has_golden_egg_2018(self) -> bool:
        return has_golden_egg_2018(self.get_list_serie())

    def has_golden_egg_2019(self) -> bool:
        return has_golden_egg_2019(self.get_list_serie())

    def has_golden_egg_2020(self) -> bool:
        return has_golden_egg_2020(self.get_list_serie())

    def has_golden_gift_2018(self) -> bool:
        return has_golden_gift_2018(self.get_list_serie())

    def has_golden_gift_2019(self) -> bool:
        return has_golden_gift_2019(self.get_list_serie())

    def has_golden_gift_2020(self) -> bool:
        return has_golden_gift_2020(self.get_list_serie())

    def has_golden_lantern_2020(self) -> bool:
        return has_golden_lantern_2020(self.get_list_serie())

    def has_golden_lantern_2021(self) -> bool:
        return has_golden_lantern_2021(self.get_list_serie())

    def has_golden_pumpkin_2018(self) -> bool:
        return has_golden_pumpkin_2018(self.get_list_serie())

    def has_golden_pumpkin_2019(self) -> bool:
        return has_golden_pumpkin_2019(self.get_list_serie())

    def has_golden_pumpkin_2020(self) -> bool:
        return has_golden_pumpkin_2020(self.get_list_serie())

    def has_haunted_hallows_series(self) -> bool:
        return has_haunted_hallows_series(self.get_list_serie())

    def has_impact_series(self) -> bool:
        return has_impact_series(self.get_list_serie())

    def has_nitro_series(self) -> bool:
        return has_nitro_series(self.get_list_serie())

    def has_non_crate(self) -> bool:
        return has_non_crate(self.get_list_serie())

    def has_overdrive_series(self) -> bool:
        return has_overdrive_series(self.get_list_serie())

    def has_players_choice_series(self) -> bool:
        return has_players_choice_series(self.get_list_serie())

    def has_secret_santa_series(self) -> bool:
        return has_secret_santa_series(self.get_list_serie())

    def has_spring_fever_series(self) -> bool:
        return has_spring_fever_series(self.get_list_serie())

    def has_totally_awesome_series(self) -> bool:
        return has_totally_awesome_series(self.get_list_serie())

    def has_triumph_series(self) -> bool:
        return has_triumph_series(self.get_list_serie())

    def has_turbo_series(self) -> bool:
        return has_turbo_series(self.get_list_serie())

    def has_velocity_series(self) -> bool:
        return has_velocity_series(self.get_list_serie())

    def has_victory_series(self) -> bool:
        return has_victory_series(self.get_list_serie())

    def has_vindicator_series(self) -> bool:
        return has_vindicator_series(self.get_list_serie())

    def has_zephyr_series(self) -> bool:
        return has_zephyr_series(self.get_list_serie())