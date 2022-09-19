import re

from rl_data_utils.item.attribute.constants import ACROBAT, AVIATOR, GOALKEEPER, GUARDIAN, JUGGLER, NONE, PARAGON, \
    PLAYMAKER, SCORER, SHOW_OFF, SNIPER, STRIKER, SWEEPER, TACTICIAN, TURTLE, VICTOR, PC, XBOX, PS4, SWITCH, \
    BLACK_MARKET, COMMON, EXOTIC, IMPORT, LEGACY, LIMITED, PREMIUM, RARE, UNCOMMON, VERY_RARE, ACCELERATOR_SERIES, \
    ACCOLADE_SERIES_1, ACCOLADE_SERIES_2, AURIGA_SERIES, BEACH_BLAST_SERIES, BONUS_GIFT, CHAMPIONS_1_SERIES, \
    CHAMPIONS_2_SERIES, CHAMPIONS_3_SERIES, CHAMPIONS_4_SERIES, ELEVATION_SERIES, FEROCITY_SERIES, GOLDEN_EGG_2020, \
    GOLDEN_EGG_2019, GOLDEN_EGG_2018, GOLDEN_GIFT_2020, GOLDEN_GIFT_2019, GOLDEN_GIFT_2018, GOLDEN_LANTERN_2021, \
    GOLDEN_LANTERN_2020, GOLDEN_LANTERN_2019, GOLDEN_PUMPKIN_2020, GOLDEN_PUMPKIN_2019, GOLDEN_PUMPKIN_2018, \
    HAUNTED_HALLOWS_SERIES, IGNITION_SERIES, IMPACT_SERIES, MOMENTUM_SERIES, NITRO_SERIES, NON_CRATE, OVERDRIVE_SERIES, \
    PLAYERS_CHOICE_SERIES, RLCS_REWARD, SEASON_1, SECRET_SANTA_SERIES, SPRING_FEVER_SERIES, TOTALLY_AWESOME_SERIES, \
    TRIUMPH_SERIES, TURBO_SERIES, VELOCITY_SERIES, VICTORY_SERIES, VINDICATOR_SERIES, ZEPHYR_SERIES, WWE_PROMO_CODE, \
    ANTENNA, BORDER, BANNER, BLUEPRINT, BOOST, CAR, DECAL, ENGINE_AUDIO, GIFT_PACK, GOAL_EXPLOSION, PAINT_FINISH, \
    ANTHEM, TITLE, TOPPER, TRAIL, WHEEL, BLACK, BURNT_SIENNA, COBALT, CRIMSON, DEFAULT, FOREST_GREEN, GREY, LIME, \
    ORANGE, PINK, PURPLE, SAFFRON, SKY_BLUE, TITANIUM_WHITE

COLOR_REGEX_TABLE = {
    BLACK: re.compile('black', re.IGNORECASE),
    BURNT_SIENNA: re.compile('burnt[_\\- ]?sienna|bs|sienna', re.IGNORECASE),
    COBALT: re.compile('cobalt|blue', re.IGNORECASE),
    CRIMSON: re.compile('crimson|carmesim|red', re.IGNORECASE),
    DEFAULT: re.compile('default|regular|none', re.IGNORECASE),
    FOREST_GREEN: re.compile('forest[_\\- ]green|fg|green', re.IGNORECASE),
    GREY: re.compile('grey', re.IGNORECASE),
    LIME: re.compile('lime', re.IGNORECASE),
    ORANGE: re.compile('orange', re.IGNORECASE),
    PINK: re.compile('pink', re.IGNORECASE),
    PURPLE: re.compile('purple', re.IGNORECASE),
    SAFFRON: re.compile('saffron|yellow', re.IGNORECASE),
    SKY_BLUE: re.compile('sky[_\\- ]?blue|sb', re.IGNORECASE),
    TITANIUM_WHITE: re.compile('titanium[_\\- ]white|white|tw', re.IGNORECASE)}
CERTIFIED_REGEX_TABLE = {
    ACROBAT: re.compile('acrobat', re.IGNORECASE),
    AVIATOR: re.compile('aviator', re.IGNORECASE),
    GOALKEEPER: re.compile('goalkeeper', re.IGNORECASE),
    GUARDIAN: re.compile('guardian', re.IGNORECASE),
    JUGGLER: re.compile('juggler', re.IGNORECASE),
    NONE: re.compile('default|regular|none', re.IGNORECASE),
    PARAGON: re.compile('paragon', re.IGNORECASE),
    PLAYMAKER: re.compile('playmaker', re.IGNORECASE),
    SCORER: re.compile('scorer', re.IGNORECASE),
    SHOW_OFF: re.compile('show[_\\- ]?off', re.IGNORECASE),
    SNIPER: re.compile('sniper', re.IGNORECASE),
    STRIKER: re.compile('striker', re.IGNORECASE),
    SWEEPER: re.compile('sweeper', re.IGNORECASE),
    TACTICIAN: re.compile('tactician', re.IGNORECASE),
    TURTLE: re.compile('turtle', re.IGNORECASE),
    VICTOR: re.compile('victor', re.IGNORECASE)}
CONTAINS_CREDITS = r'credits?'
IS_CREDITS = r'^credits?$'
PLATFORM_REGEX_TABLE = {
    PC: re.compile('(:?pc|computer)', re.IGNORECASE),
    XBOX: re.compile('xbox', re.IGNORECASE),
    PS4: re.compile('(:?ps|play(:?station)?)[_\\- ]?4?', re.IGNORECASE),
    SWITCH: re.compile('switch', re.IGNORECASE)}
RARITY_REGEX_TABLE = {
    BLACK_MARKET: re.compile('black[_\\- ]?markets?|bms?', re.IGNORECASE),
    COMMON: re.compile('commons?', re.IGNORECASE),
    EXOTIC: re.compile('exotics?', re.IGNORECASE),
    IMPORT: re.compile('importeds?|imports?', re.IGNORECASE),
    LEGACY: re.compile('legac(y|ies)', re.IGNORECASE),
    LIMITED: re.compile('limiteds?', re.IGNORECASE),
    PREMIUM: re.compile('premiums?', re.IGNORECASE),
    RARE: re.compile('rares?', re.IGNORECASE),
    UNCOMMON: re.compile('uncommons?', re.IGNORECASE),
    VERY_RARE: re.compile('very[_\\- ]?rares?|vrs?', re.IGNORECASE)}
SERIE_REGEX_TABLE = {
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
SLOT_REGEX_TABLE = {
    ANTENNA: re.compile('antennas?', re.IGNORECASE),
    BORDER: re.compile('avatar[_\\- ]?borders?', re.IGNORECASE),
    BANNER: re.compile('(player)?[_\\- ]?banners?', re.IGNORECASE),
    BLUEPRINT: re.compile('blueprints?', re.IGNORECASE),
    BOOST: re.compile('(rocket)?[_\\- ]?boosts?', re.IGNORECASE),
    CAR: re.compile('cars?|body|bodies', re.IGNORECASE),
    DECAL: re.compile('(animated)?[_\\- ]?decals?', re.IGNORECASE),
    ENGINE_AUDIO: re.compile('engine[_\\- ]?audios?', re.IGNORECASE),
    GIFT_PACK: re.compile('gift[_\\- ]?packs?', re.IGNORECASE),
    GOAL_EXPLOSION: re.compile('goal[_\\- ]?explosions?', re.IGNORECASE),
    PAINT_FINISH: re.compile('paint[_\\- ]?finish(es)?', re.IGNORECASE),
    ANTHEM: re.compile('(player[_\\- ]?)?anthems?', re.IGNORECASE),
    TITLE: re.compile('(player)?[_\\- ]?titles?', re.IGNORECASE),
    TOPPER: re.compile('toppers?|hats?', re.IGNORECASE),
    TRAIL: re.compile('trails?', re.IGNORECASE),
    WHEEL: re.compile('wheels?', re.IGNORECASE)}
