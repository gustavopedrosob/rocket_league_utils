from __future__ import annotations
from re import sub, IGNORECASE, compile
from contextlib import suppress
from functools import lru_cache
from rl_data_utils.exceptions import NameHaveNotCarName
from rl_data_utils.item.name.constants import CARS_NAMES_WITH_DECAL
from rl_data_utils.item.name.name_info import NameInfo
from rl_data_utils.item.slot.constants import DECAL
from rl_data_utils.item.slot.slot import Slot
from rl_data_utils.item.attribute.attribute import Attribute


class Name(Attribute, NameInfo):
    attribute_type = str

    @lru_cache
    def compare(self, name: Name) -> str:
        with suppress(NameHaveNotCarName):
            name_1 = self._get_string_to_compare()
            name_2 = name._get_string_to_compare()
        return name_1 == name_2

    def get_decal_and_car(self):
        reo = compile(r'[([]?(' + '|'.join(CARS_NAMES_WITH_DECAL) + r')[)\]:]?')
        result = reo.search(self.attribute, IGNORECASE)
        try:
            car_full_name = result.group(0)
            car_name = result.group(1)
        except AttributeError:
            raise NameHaveNotCarName(self.attribute)
        # remove car_name from string
        name = self.attribute.replace(car_full_name, '').strip()
        return name, car_name

    def _get_string_to_compare(self) -> str:
        name = self.attribute
        try:
            name_decal, car_name = self.get_decal_and_car()
        except NameHaveNotCarName:
            pass
        else:
            name = f'{name_decal} {car_name}'
        return sub(r'\W', '', name).lower()

    def is_car_decal_name(self, slot: Slot = None) -> bool:
        if isinstance(slot, Slot):
            with suppress(NameHaveNotCarName):
                if slot.is_exactly(DECAL) and self.get_decal_and_car():
                    return True
        else:
            if self.get_decal_and_car():
                return True
        return False
