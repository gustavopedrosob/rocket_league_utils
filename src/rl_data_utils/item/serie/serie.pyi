from __future__ import annotations

from typing import Literal

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.item.constants import SERIE
from rl_data_utils.item.serie.constants import SERIES

SeriePatternKey = Literal[
    'Accelerator Series', 'Accolade 1 Series', 'Accolade 2 Series', 'Auriga Series', 'Beach Blast Series',
    'Bonus Gift', 'Champions 1 Series', 'Champions 2 Series', 'Champions 3 Series', 'Champions 4 Series',
    'Elevation Series', 'Ferocity Series', 'Golden Egg 2018', 'Golden Egg 2019', 'Golden Egg 2020', 'Golden Gift 2018',
    'Golden Gift 2019', 'Golden Gift 2020', 'Golden Lantern 2019', 'Golden Lantern 2020', 'Golden Lantern 2021',
    'Golden Pumpkin 2018', 'Golden Pumpkin 2019', 'Golden Pumpkin 2020', 'Haunted Hallows Series', 'Ignition Series',
    'Impact Series', 'Momentum Series', 'Nitro Series', 'Non Crate', 'Overdrive Series', "Player's Choice Series",
    'RLCS Reward', 'Season 1', 'Secret Santa Series', 'Spring Fever Series', 'Totally Awesome Series',
    'Triumph Series', 'Turbo Series', 'Velocity Series', 'Victory Series', 'Vindicator Series', 'Zephyr Series',
    'WWE Promo Code']


class SerieInfo(AttributeInfo): ...


class Serie(RegexBasedItemAttribute, SerieInfo): ...


class Series(RegexBasedListAttribute[Serie], SerieInfo): ...
