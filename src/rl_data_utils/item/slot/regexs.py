import re

from rl_data_utils.item.slot.constants import ANTENNA, BORDER, BANNER, BLUEPRINT, BOOST, CAR, DECAL, ENGINE_AUDIO, \
    GIFT_PACK, GOAL_EXPLOSION, PAINT_FINISH, ANTHEM, TITLE, TOPPER, TRAIL, WHEEL

REGEX_TABLE = {
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
