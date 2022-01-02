import re

from rl_data_utils.item.rarity.constants import BLACK_MARKET, COMMON, EXOTIC, IMPORT, LEGACY, LIMITED, PREMIUM, RARE, \
    UNCOMMON, VERY_RARE

# noinspection SpellCheckingInspection
REGEX_TABLE = {
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
