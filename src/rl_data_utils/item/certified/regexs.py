from typing import Dict

from rl_data_utils.item.certified.constants import *

CONTAINS: Final[Dict[str, str]] = {
    ACROBAT: 'acrobat',
    AVIATOR: 'aviator',
    GOALKEEPER: 'goalkeeper',
    GUARDIAN: 'guardian',
    JUGGLER: 'juggler',
    NONE: 'default|regular|none',
    PARAGON: 'paragon',
    PLAYMAKER: 'playmaker',
    SCORER: 'scorer',
    SHOW_OFF: 'show[_\\- ]?off',
    SNIPER: 'sniper',
    STRIKER: 'striker',
    SWEEPER: 'sweeper',
    TACTICIAN: 'tactician',
    TURTLE: 'turtle',
    VICTOR: 'victor'}
