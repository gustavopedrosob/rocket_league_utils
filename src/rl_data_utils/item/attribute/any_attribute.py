from typing import Union

from rl_data_utils.item.archived.archived import Archived
from rl_data_utils.item.blueprint.blueprint import Blueprint
from rl_data_utils.item.certified.certified import Certified
from rl_data_utils.item.color.color import Color, Colors
from rl_data_utils.item.name.name import Name
from rl_data_utils.item.paintable.paintable import Paintable
from rl_data_utils.item.platform.platform import Platform, Platforms
from rl_data_utils.item.price.price import Price
from rl_data_utils.item.quantity.quantity import Quantity
from rl_data_utils.item.rarity.rarity import Rarity, Rarities
from rl_data_utils.item.serie.serie import Serie, Series
from rl_data_utils.item.slot.slot import Slot
from rl_data_utils.item.tradable.tradable import Tradable

AnyAttribute = Union[Archived, Name, Slot, Color, Rarity, Certified, Quantity, Blueprint, Paintable, Platform, Price,
                     Serie, Tradable]
AnyDataAttribute = Union[Colors, Rarities, Platforms, Series]
AnyAllAttribute = Union[AnyAttribute, AnyDataAttribute]
