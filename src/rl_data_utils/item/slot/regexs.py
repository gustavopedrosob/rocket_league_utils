from typing import Dict

from rl_data_utils.item.slot.constants import *

CONTAINS: Final[Dict[str, str]] = {
    ANTENNA: 'antennas?',
    BORDER: 'avatar[_\\- ]?borders?',
    BANNER: '(player)?[_\\- ]?banners?',
    BLUEPRINT: 'blueprints?',
    BOOST: '(rocket)?[_\\- ]?boosts?',
    CAR: 'cars?|body|bodies',
    DECAL: '(animated)?[_\\- ]?decals?',
    ENGINE_AUDIO: 'engine[_\\- ]?audios?',
    GIFT_PACK: 'gift[_\\- ]?packs?',
    GOAL_EXPLOSION: 'goal[_\\- ]?explosions?',
    PAINT_FINISH: 'paint[_\\- ]?finish(es)?',
    ANTHEM: '(player[_\\- ]?)?anthems?',
    TITLE: '(player)?[_\\- ]?titles?',
    TOPPER: 'toppers?|hats?',
    TRAIL: 'trails?',
    WHEEL: 'wheels?'}
