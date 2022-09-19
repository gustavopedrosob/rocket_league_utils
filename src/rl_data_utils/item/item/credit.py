from __future__ import annotations

from rl_data_utils.item.attribute.attribute import Archived, Name, Rarity, Tradable
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.attribute.constants import CREDITS, PREMIUM


class Credit(Item):
    def __init__(self, platform=None, quantity=None):
        super().__init__(
            archived=Archived(False),
            name=Name(CREDITS),
            rarity=Rarity(PREMIUM),
            quantity=quantity,
            platform=platform,
            tradable=Tradable(True))
