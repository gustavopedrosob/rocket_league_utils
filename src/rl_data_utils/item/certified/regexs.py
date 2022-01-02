import re

from rl_data_utils.item.certified.constants import ACROBAT, AVIATOR, GOALKEEPER, GUARDIAN, JUGGLER, NONE, PARAGON, \
    PLAYMAKER, SCORER, SHOW_OFF, SNIPER, STRIKER, SWEEPER, TACTICIAN, TURTLE, VICTOR

REGEX_TABLE = {
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
