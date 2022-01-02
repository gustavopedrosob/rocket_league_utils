from __future__ import annotations

from rl_data_utils.item.archived.archived import Archived
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.name.constants import CREDITS
from rl_data_utils.item.name.name import Name
from rl_data_utils.item.rarity.constants import PREMIUM
from rl_data_utils.item.rarity.rarity import Rarity
from rl_data_utils.item.tradable.tradable import Tradable


class Credit(Item):
    def __init__(self, platform=None, quantity=None):
        super().__init__(
            archived=Archived(False),
            name=Name(CREDITS),
            rarity=Rarity(PREMIUM),
            quantity=quantity,
            platform=platform,
            tradable=Tradable(True))
