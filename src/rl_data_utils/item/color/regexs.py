import re

from rl_data_utils.item.color.constants import BLACK, BURNT_SIENNA, COBALT, CRIMSON, DEFAULT, FOREST_GREEN, GREY, \
    LIME, ORANGE, PINK, PURPLE, SAFFRON, SKY_BLUE, TITANIUM_WHITE

REGEX_TABLE = {
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
