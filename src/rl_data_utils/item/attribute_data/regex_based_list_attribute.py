from rl_data_utils.item.attribute_data.attribute_data import AttributesManagement, AttributesData
from rl_data_utils.rocket_league.rocket_league import FromStrList


class RegexBasedListAttribute(AttributesData, FromStrList, AttributesManagement):
    @classmethod
    def from_str_list(cls, str_list):
        return cls(list(map(lambda str_: cls.attribute_class(str_), str_list)))
