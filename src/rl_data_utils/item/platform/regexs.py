import re

from rl_data_utils.item.platform.constants import PC, XBOX, PS4, SWITCH

REGEX_TABLE = {
    PC: re.compile('(:?pc|computer)', re.IGNORECASE),
    XBOX: re.compile('xbox', re.IGNORECASE),
    PS4: re.compile('(:?ps|play(:?station)?)[_\\- ]?4?', re.IGNORECASE),
    SWITCH: re.compile('switch', re.IGNORECASE)}

