from typing import Optional

from rl_data_utils.item.attribute.attribute import Platform


class Account:
    def __init__(self, name: str, platform: Optional[Platform], avatar: Optional[str]) -> None:
        self.name = name
        self.platform = platform
        self.avatar = avatar
