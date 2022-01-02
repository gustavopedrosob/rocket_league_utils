import re

from rl_data_utils.item.serie.constants import ACCELERATOR_SERIES, ACCOLADE_SERIES_1, ACCOLADE_SERIES_2, \
    AURIGA_SERIES, BEACH_BLAST_SERIES, BONUS_GIFT, CHAMPIONS_1_SERIES, CHAMPIONS_2_SERIES, CHAMPIONS_3_SERIES, \
    CHAMPIONS_4_SERIES, ELEVATION_SERIES, FEROCITY_SERIES, GOLDEN_EGG_2020, GOLDEN_EGG_2019, GOLDEN_EGG_2018, \
    GOLDEN_GIFT_2020, GOLDEN_GIFT_2019, GOLDEN_GIFT_2018, GOLDEN_LANTERN_2021, GOLDEN_LANTERN_2020, \
    GOLDEN_LANTERN_2019, GOLDEN_PUMPKIN_2020, GOLDEN_PUMPKIN_2019, GOLDEN_PUMPKIN_2018, HAUNTED_HALLOWS_SERIES, \
    IGNITION_SERIES, IMPACT_SERIES, MOMENTUM_SERIES, NITRO_SERIES, NON_CRATE, OVERDRIVE_SERIES,\
    PLAYERS_CHOICE_SERIES, RLCS_REWARD, SEASON_1, SECRET_SANTA_SERIES, SPRING_FEVER_SERIES, TOTALLY_AWESOME_SERIES, \
    TRIUMPH_SERIES, TURBO_SERIES, VELOCITY_SERIES, VICTORY_SERIES, VINDICATOR_SERIES, ZEPHYR_SERIES, WWE_PROMO_CODE

# noinspection SpellCheckingInspection
REGEX_TABLE = {
    ACCELERATOR_SERIES: re.compile("Accelerator[_\\- ]?(Series)?", re.IGNORECASE),
    ACCOLADE_SERIES_1: re.compile("Accolade[_\\- ]?[1I][_\\- ]?(Series)?", re.IGNORECASE),
    ACCOLADE_SERIES_2: re.compile("Accolade[_\\- ]?(2|II)[_\\- ]?(Series)?", re.IGNORECASE),
    AURIGA_SERIES: re.compile("Auriga[_\\- ]?(Series)?", re.IGNORECASE),
    BEACH_BLAST_SERIES: re.compile("Beach[_\\- ]?Blast[_\\- ]?(Series)?", re.IGNORECASE),
    BONUS_GIFT: re.compile("Bonus[_\\- ]?Gift", re.IGNORECASE),
    CHAMPIONS_1_SERIES: re.compile("Champions[_\\- ]?1[_\\- ]?(Series)?", re.IGNORECASE),
    CHAMPIONS_2_SERIES: re.compile("Champions[_\\- ]?2[_\\- ]?(Series)?", re.IGNORECASE),
    CHAMPIONS_3_SERIES: re.compile("Champions[_\\- ]?3[_\\- ]?(Series)?", re.IGNORECASE),
    CHAMPIONS_4_SERIES: re.compile("Champions[_\\- ]?4[_\\- ]?(Series)?", re.IGNORECASE),
    ELEVATION_SERIES: re.compile("Elevation[_\\- ]?(Series)?", re.IGNORECASE),
    FEROCITY_SERIES: re.compile("Ferocity[_\\- ]?(Series)?", re.IGNORECASE),
    GOLDEN_EGG_2020: re.compile("Golden[_\\- ]?Egg[_\\- ]?[']?(20)?20", re.IGNORECASE),
    GOLDEN_EGG_2019: re.compile("Golden[_\\- ]?Egg[_\\- ]?[']?(20)?19", re.IGNORECASE),
    GOLDEN_EGG_2018: re.compile("Golden[_\\- ]?Egg[_\\- ]?[']?(20)?18", re.IGNORECASE),
    GOLDEN_GIFT_2020: re.compile("Golden[_\\- ]?Gift[_\\- ]?[']?(20)?20", re.IGNORECASE),
    GOLDEN_GIFT_2019: re.compile("Golden[_\\- ]?Gift[_\\- ]?[']?(20)?19", re.IGNORECASE),
    GOLDEN_GIFT_2018: re.compile("Golden[_\\- ]?Gift[_\\- ]?[']?(20)?18", re.IGNORECASE),
    GOLDEN_LANTERN_2021: re.compile("Golden[_\\- ]?Lantern[_\\- ]?[']?(20)?21", re.IGNORECASE),
    GOLDEN_LANTERN_2020: re.compile("Golden[_\\- ]?Lantern[_\\- ]?[']?(20)?20", re.IGNORECASE),
    GOLDEN_LANTERN_2019: re.compile("Golden[_\\- ]?Lantern[_\\- ]?[']?(20)?19", re.IGNORECASE),
    GOLDEN_PUMPKIN_2020: re.compile("Golden[_\\- ]?Pumpkin[_\\- ]?[']?(20)?20", re.IGNORECASE),
    GOLDEN_PUMPKIN_2019: re.compile("Golden[_\\- ]?Pumpkin[_\\- ]?[']?(20)?19", re.IGNORECASE),
    GOLDEN_PUMPKIN_2018: re.compile("Golden[_\\- ]?Pumpkin[_\\- ]?[']?(20)?18", re.IGNORECASE),
    HAUNTED_HALLOWS_SERIES: re.compile("Haunted[_\\- ]?Hallows[_\\- ]?(Series)?", re.IGNORECASE),
    IGNITION_SERIES: re.compile("Ignition[_\\- ]?(Series)?", re.IGNORECASE),
    IMPACT_SERIES: re.compile("Impact[_\\- ]?(Series)?", re.IGNORECASE),
    MOMENTUM_SERIES: re.compile("Momentum[_\\- ]?(Series)?", re.IGNORECASE),
    NITRO_SERIES: re.compile("Nitro[_\\- ]?(Series)?", re.IGNORECASE),
    NON_CRATE: re.compile("Non[_\\- ]?Crate|Post[_\\- ]?Game", re.IGNORECASE),
    OVERDRIVE_SERIES: re.compile("Overdrive[_\\- ]?(Series)?", re.IGNORECASE),
    PLAYERS_CHOICE_SERIES: re.compile("Player(s|'s)?[_\\- ]?Choice[_\\- ]?(Series)?", re.IGNORECASE),
    RLCS_REWARD: re.compile("RLCS[_\\- ]?Reward", re.IGNORECASE),
    SEASON_1: re.compile("Season[_\\- ]?[1I]", re.IGNORECASE),
    SECRET_SANTA_SERIES: re.compile("Secret[_\\- ]?Santa[_\\- ]?(Series)?", re.IGNORECASE),
    SPRING_FEVER_SERIES: re.compile("Spring[_\\- ]?Fever[_\\- ]?(Series)?", re.IGNORECASE),
    TOTALLY_AWESOME_SERIES: re.compile("Totally[_\\- ]?Awesome[_\\- ]?(Series)?", re.IGNORECASE),
    TRIUMPH_SERIES: re.compile("Triumph[_\\- ]?(Series)?", re.IGNORECASE),
    TURBO_SERIES: re.compile("Turbo[_\\- ]?(Series)?", re.IGNORECASE),
    VELOCITY_SERIES: re.compile("Velocity[_\\- ]?(Series)?", re.IGNORECASE),
    VICTORY_SERIES: re.compile("Victory[_\\- ]?(Series)?", re.IGNORECASE),
    VINDICATOR_SERIES: re.compile("Vindicator[_\\- ]?(Series)?", re.IGNORECASE),
    ZEPHYR_SERIES: re.compile("Zephyr[_\\- ]?(Series)?", re.IGNORECASE),
    WWE_PROMO_CODE: re.compile("WWE[_\\- ]?Promo[_\\- ]?Code", re.IGNORECASE)}
