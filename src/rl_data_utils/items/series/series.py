from rl_data_utils.items.items.items import Items
from rl_data_utils.items.series.abc_base_series import ABCBaseSeries
from rl_data_utils.utils.items.series.series import *


class Series(ABCBaseSeries, Items):
    def get_items_with_valid_serie(self):
        return self.__class__(get_items_with_valid_serie(self.items))

    def get_items_by_serie_regex(self, serie_pattern, flags=IGNORECASE):
        return self.__class__(get_items_by_serie_regex(serie_pattern, self.items, flags))

    def get_items_by_serie(self, serie: str):
        return self.__class__(get_items_by_serie(serie, self.items))

    def get_items_by_serie_equal_to(self, serie: str):
        return self.__class__(get_items_by_serie_equal_to(serie, self.items))

    def get_items_by_serie_contains(self, serie: str):
        return self.__class__(get_items_by_serie_contains(serie, self.items))

    def get_series(self):
        return get_series(self.items)

    def get_items_accelerator_series(self):
        return self.__class__(get_items_accelerator_series(self.items))

    def get_items_beach_blast_series(self):
        return self.__class__(get_items_beach_blast_series(self.items))

    def get_items_bonus_gift(self):
        return self.__class__(get_items_bonus_gift(self.items))

    def get_items_champions_1_series(self):
        return self.__class__(get_items_champions_1_series(self.items))

    def get_items_champions_2_series(self):
        return self.__class__(get_items_champions_2_series(self.items))

    def get_items_champions_3_series(self):
        return self.__class__(get_items_champions_3_series(self.items))

    def get_items_champions_4_series(self):
        return self.__class__(get_items_champions_4_series(self.items))

    def get_items_elevation_series(self):
        return self.__class__(get_items_elevation_series(self.items))

    def get_items_ferocity_series(self):
        return self.__class__(get_items_ferocity_series(self.items))

    def get_items_golden_egg_2018(self):
        return self.__class__(get_items_golden_egg_2018(self.items))

    def get_items_golden_egg_2019(self):
        return self.__class__(get_items_golden_egg_2019(self.items))

    def get_items_golden_egg_2020(self):
        return self.__class__(get_items_golden_egg_2020(self.items))

    def get_items_golden_gift_2018(self):
        return self.__class__(get_items_golden_gift_2018(self.items))

    def get_items_golden_gift_2019(self):
        return self.__class__(get_items_golden_gift_2019(self.items))

    def get_items_golden_gift_2020(self):
        return self.__class__(get_items_golden_gift_2020(self.items))

    def get_items_golden_lantern_2020(self):
        return self.__class__(get_items_golden_lantern_2020(self.items))

    def get_items_golden_lantern_2021(self):
        return self.__class__(get_items_golden_lantern_2021(self.items))

    def get_items_golden_pumpkin_2018(self):
        return self.__class__(get_items_golden_pumpkin_2018(self.items))

    def get_items_golden_pumpkin_2019(self):
        return self.__class__(get_items_golden_pumpkin_2019(self.items))

    def get_items_golden_pumpkin_2020(self):
        return self.__class__(get_items_golden_pumpkin_2020(self.items))

    def get_items_haunted_hallows_series(self):
        return self.__class__(get_items_haunted_hallows_series(self.items))

    def get_items_impact_series(self):
        return self.__class__(get_items_impact_series(self.items))

    def get_items_nitro_series(self):
        return self.__class__(get_items_nitro_series(self.items))

    def get_items_non_crate(self):
        return self.__class__(get_items_non_crate(self.items))

    def get_items_overdrive_series(self):
        return self.__class__(get_items_overdrive_series(self.items))

    def get_items_players_choice_series(self):
        return self.__class__(get_items_players_choice_series(self.items))

    def get_items_secret_santa_series(self):
        return self.__class__(get_items_secret_santa_series(self.items))

    def get_items_spring_fever_series(self):
        return self.__class__(get_items_spring_fever_series(self.items))

    def get_items_totally_awesome_series(self):
        return self.__class__(get_items_totally_awesome_series(self.items))

    def get_items_triumph_series(self):
        return self.__class__(get_items_triumph_series(self.items))

    def get_items_turbo_series(self):
        return self.__class__(get_items_turbo_series(self.items))

    def get_items_velocity_series(self):
        return self.__class__(get_items_velocity_series(self.items))

    def get_items_victory_series(self):
        return self.__class__(get_items_victory_series(self.items))

    def get_items_vindicator_series(self):
        return self.__class__(get_items_vindicator_series(self.items))

    def get_items_zephyr_series(self):
        return self.__class__(get_items_zephyr_series(self.items))
