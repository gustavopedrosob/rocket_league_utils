from typing import Dict

from rl_data_utils.item.rarity.constants import *

# noinspection SpellCheckingInspection
CONTAINS: Final[Dict[str, str]] = {
    BLACK_MARKET: 'black[_\\- ]?markets?|bms?',
    COMMON: 'commons?',
    EXOTIC: 'exotics?',
    IMPORT: 'importeds?|imports?',
    LEGACY: 'legac(y|ies)',
    LIMITED: 'limiteds?',
    PREMIUM: 'premiums?',
    RARE: 'rares?',
    UNCOMMON: 'uncommons?',
    VERY_RARE: 'very[_\\- ]?rares?|vrs?'}
