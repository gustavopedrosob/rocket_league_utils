from __future__ import annotations

from typing import Optional

from rl_data_utils.item.item.item import Item
from rl_data_utils.item.attribute.attribute import Platform, CreditsQuantity


class Credit(Item):
    def __init__(self,
                 platform: Optional[Platform] = ...,
                 quantity: Optional[CreditsQuantity] = ...) -> None: ...

