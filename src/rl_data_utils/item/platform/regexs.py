from typing import Dict

from rl_data_utils.item.platform.constants import *

CONTAINS: Final[Dict[str, str]] = {
    PC: '(:?pc|computer)',
    XBOX: 'xbox',
    PS4: '(:?ps|play(:?station)?)[_\\- ]?4?',
    SWITCH: 'switch'}

