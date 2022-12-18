from __future__ import annotations

import datetime
import functools
import sqlite3
import typing
import re
import numpy
import unidecode
from rocket_league_utils import constants

COLOR_REGEX_TABLE = (
    ((constants.BLACK,), re.compile(r"black", re.I)),
    ((constants.BURNT_SIENNA, constants.SIENNA, constants.BS), re.compile(r"burnt[_\- ]?sienna|bs|sienna", re.I)),
    ((constants.COBALT, constants.BLUE), re.compile(r"cobalt|blue", re.I)),
    ((constants.CRIMSON, constants.CARMESIM, constants.RED), re.compile(r"crimson|carmesim|red", re.I)),
    ((constants.DEFAULT, constants.REGULAR, constants.NONE), re.compile(r"default|regular|none", re.I)),
    ((constants.FOREST_GREEN, constants.GREEN, constants.FG), re.compile(r"forest[_\- ]green|fg|green", re.I)),
    ((constants.GREY, ), re.compile(r"grey", re.I)),
    ((constants.LIME, ), re.compile(r"lime", re.I)),
    ((constants.ORANGE, ), re.compile(r"orange", re.I)),
    ((constants.PINK, ), re.compile(r"pink", re.I)),
    ((constants.PURPLE, ), re.compile(r"purple", re.I)),
    ((constants.SAFFRON, constants.YELLOW), re.compile(r"saffron|yellow", re.I)),
    ((constants.SKY_BLUE, constants.SB), re.compile(r"sky[_\- ]?blue|sb", re.I)),
    ((constants.TITANIUM_WHITE, constants.WHITE, constants.TW), re.compile(r"titanium[_\- ]white|white|tw", re.I)),
    ((constants.GOLDEN, constants.GOLD), re.compile(r"gold(:?en)?", re.I)))
CERTIFIED_REGEX_TABLE = (
    ((constants.ACROBAT, ), re.compile(r"acrobat", re.I)),
    ((constants.AVIATOR, ), re.compile(r"aviator", re.I)),
    ((constants.GOALKEEPER, ), re.compile(r"goalkeeper", re.I)),
    ((constants.GUARDIAN, ), re.compile(r"guardian", re.I)),
    ((constants.JUGGLER, ), re.compile(r"juggler", re.I)),
    ((constants.NONE, ), re.compile(r"default|regular|none", re.I)),
    ((constants.PARAGON, ), re.compile(r"paragon", re.I)),
    ((constants.PLAYMAKER, ), re.compile(r"playmaker", re.I)),
    ((constants.SCORER, ), re.compile(r"scorer", re.I)),
    ((constants.SHOW_OFF, ), re.compile(r"show[_\- ]?off", re.I)),
    ((constants.SNIPER, ), re.compile(r"sniper", re.I)),
    ((constants.STRIKER, ), re.compile(r"striker", re.I)),
    ((constants.SWEEPER, ), re.compile(r"sweeper", re.I)),
    ((constants.TACTICIAN, ), re.compile(r"tactician", re.I)),
    ((constants.TURTLE, ), re.compile(r"turtle", re.I)),
    ((constants.VICTOR, ), re.compile(r"victor", re.I)))
PLATFORM_REGEX_TABLE = (
    ((constants.PC, constants.COMPUTER, constants.EPIC, constants.EPIC_GAMES, constants.STEAM),
        re.compile(r"pc|computer|epic([_\- ]games)?|steam", re.I)),
    ((constants.XBOX, ), re.compile(r"xbox", re.I)),
    ((constants.PLAYSTATION_4, constants.PLAY_4, constants.PS4), re.compile(r"(:?ps|play(:?station)?)[_\- ]?4?", re.I)),
    ((constants.SWITCH, ), re.compile(r"switch", re.I)))
RARITY_REGEX_TABLE = (
    ((constants.BLACK_MARKET, constants.BM), re.compile(r"black[_\- ]?markets?|bms?", re.I)),
    ((constants.COMMON, ), re.compile(r"commons?", re.I)),
    ((constants.EXOTIC, ), re.compile(r"exotics?", re.I)),
    ((constants.IMPORT, ), re.compile(r"imports?", re.I)),
    ((constants.LEGACY, ), re.compile(r"legac(y|ies)", re.I)),
    ((constants.LIMITED, ), re.compile(r"limiteds?", re.I)),
    ((constants.PREMIUM, ), re.compile(r"premiums?", re.I)),
    ((constants.RARE, ), re.compile(r"rares?", re.I)),
    ((constants.UNCOMMON, ), re.compile(r"uncommons?", re.I)),
    ((constants.VERY_RARE, constants.VR), re.compile(r"very[_\- ]?rares?|vrs?", re.I)))
SERIE_REGEX_TABLE = (
    ((constants.ACCELERATOR, ), re.compile(r"accelerator(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.ACCOLADE_1, ), re.compile(r"accolade[_\- ]?[1I](:?[_\- ]?series)?", re.I)),
    ((constants.ACCOLADE_2, ), re.compile(r"accolade[_\- ]?(2|II)(:?[_\- ]?series)?", re.I)),
    ((constants.AURIGA, ), re.compile(r"auriga(:?[_\- ]?series)?", re.I)),
    ((constants.BEACH_BLAST, ), re.compile(r"beach[_\- ]?blast(:?[_\- ]?series)?", re.I)),
    ((constants.BONUS_GIFT, ), re.compile(r"bonus[_\- ]?gift", re.I)),
    ((constants.CHAMPIONS_1, ), re.compile(r"champions[_\- ]?1(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.CHAMPIONS_2, ), re.compile(r"champions[_\- ]?2(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.CHAMPIONS_3, ), re.compile(r"champions[_\- ]?3(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.CHAMPIONS_4, ), re.compile(r"champions[_\- ]?4(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.DORADO, ), re.compile(r"dorado(:?[_\- ]?series)?", re.I)),
    ((constants.ELEVATION, ), re.compile(r"elevation(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.FEROCITY, ), re.compile(r"ferocity(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.FORNAX, ), re.compile(r"fornax(:?[_\- ]?series)?", re.I)),
    ((constants.GOLDEN_EGG_2022, ), re.compile(r"golden[_\- ]?egg[_\- ]?(:?'22|2022)", re.I)),
    ((constants.GOLDEN_EGG_2020, ), re.compile(r"golden[_\- ]?egg[_\- ]?(:?'20|2020)", re.I)),
    ((constants.GOLDEN_EGG_2019, ), re.compile(r"golden[_\- ]?egg[_\- ]?(:?'19|2019)", re.I)),
    ((constants.GOLDEN_EGG_2018, ), re.compile(r"golden[_\- ]?egg[_\- ]?(:?'18|2018)", re.I)),
    ((constants.GOLDEN_GIFT_2021, ), re.compile(r"golden[_\- ]?gift[_\- ]?(:?'21|2021)", re.I)),
    ((constants.GOLDEN_GIFT_2020, ), re.compile(r"golden[_\- ]?gift[_\- ]?(:?'20|2020)", re.I)),
    ((constants.GOLDEN_GIFT_2019, ), re.compile(r"golden[_\- ]?gift[_\- ]?(:?'19|2019)", re.I)),
    ((constants.GOLDEN_GIFT_2018, ), re.compile(r"golden[_\- ]?gift[_\- ]?(:?'18|2018)", re.I)),
    ((constants.GOLDEN_GIFT_BASKET_2022, ), re.compile(r"golden[_\- ]?gift[_\- ]?basket[_\- ]?(:?'22|2022)", re.I)),
    ((constants.GOLDEN_LANTERN_2021, ), re.compile(r"golden[_\- ]?lantern[_\- ]?(:?'21|2021)", re.I)),
    ((constants.GOLDEN_LANTERN_2020, ), re.compile(r"golden[_\- ]?lantern[_\- ]?(:?'20|2020)", re.I)),
    ((constants.GOLDEN_LANTERN_2019, ), re.compile(r"golden[_\- ]?lantern[_\- ]?(:?'19|2019)", re.I)),
    ((constants.GOLDEN_MOON, ), re.compile(r"golden[_\- ]?moon", re.I)),
    ((constants.GOLDEN_PUMPKIN_2022, ), re.compile(r"golden[_\- ]?pumpkin[_\- ]?(:?'22|2022)", re.I)),
    ((constants.GOLDEN_PUMPKIN_2020, ), re.compile(r"golden[_\- ]?pumpkin[_\- ]?(:?'20|2020)", re.I)),
    ((constants.GOLDEN_PUMPKIN_2019, ), re.compile(r"golden[_\- ]?pumpkin[_\- ]?(:?'19|2019)", re.I)),
    ((constants.GOLDEN_PUMPKIN_2018, ), re.compile(r"golden[_\- ]?pumpkin[_\- ]?(:?'18|2018)", re.I)),
    ((constants.HAUNTED_HALLOWS, ), re.compile(r"haunted[_\- ]?hallows(:?[_\- ]?series)?", re.I)),
    ((constants.IGNITION, ), re.compile(r"ignition(:?[_\- ]?series)?", re.I)),
    ((constants.IMPACT, ), re.compile(r"impact(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.MOMENTUM, ), re.compile(r"momentum(:?[_\- ]?series)?", re.I)),
    ((constants.NITRO, ), re.compile(r"nitro(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.NON_CRATE, ), re.compile(r"non[_\- ]?crate|post[_\- ]?game", re.I)),
    ((constants.OVERDRIVE, ), re.compile(r"overdrive(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.PLAYERS_CHOICE, ), re.compile(r"player'?s?[_\- ]?choice(:?[_\- ]?series)?", re.I)),
    ((constants.REVIVAL, ), re.compile(r"revival([_\- ]?series)?", re.I)),
    ((constants.ROCKETPASS_1, ), re.compile(r"rocketpass[_\- ]?[1I]", re.I)),
    ((constants.ROCKETPASS_2, ), re.compile(r"rocketpass[_\- ]?(:?2|II)", re.I)),
    ((constants.ROCKETPASS_3, ), re.compile(r"rocketpass[_\- ]?(:?3|III)", re.I)),
    ((constants.ROCKETPASS_4, ), re.compile(r"rocketpass[_\- ]?(:?4|IV)", re.I)),
    ((constants.ROCKETPASS_5, ), re.compile(r"rocketpass[_\- ]?(:?5|V)", re.I)),
    ((constants.ROCKETPASS_6, ), re.compile(r"rocketpass[_\- ]?(:?6|VI)", re.I)),
    ((constants.ROCKETPASS_7, ), re.compile(r"rocketpass[_\- ]?(:?7|VII)", re.I)),
    ((constants.ROCKETPASS_8, ), re.compile(r"rocketpass[_\- ]?(:?8|VIII)", re.I)),
    ((constants.ROCKETPASS_9, ), re.compile(r"rocketpass[_\- ]?(:?9|IX)", re.I)),
    ((constants.ROCKETPASS_10, ), re.compile(r"rocketpass[_\- ]?(:?10|X)", re.I)),
    ((constants.ROCKETPASS_11, ), re.compile(r"rocketpass[_\- ]?(:?11|XI)", re.I)),
    ((constants.ROCKETPASS_12, ), re.compile(r"rocketpass[_\- ]?(:?12|XII)", re.I)),
    ((constants.ROCKETPASS_13, ), re.compile(r"rocketpass[_\- ]?(:?13|XIII)", re.I)),
    ((constants.ROCKETPASS_14, ), re.compile(r"rocketpass[_\- ]?(:?14|XIV)", re.I)),
    ((constants.RLCS_REWARD, ), re.compile(r"rlcs[_\- ]?reward", re.I)),
    ((constants.SELECT_FAVORITES_ITEM, ), re.compile(r"select[_\- ]?favorites[_\- ]?item(:?[_\- ]?series)?", re.I)),
    ((constants.SELECT_FAVORITES_2, ), re.compile(r"select[_\- ]?favorites(:?[_\- ]?series)?[_\- ]?2", re.I)),
    ((constants.SEASON_1, ), re.compile(r"season[_\- ]?[1I]", re.I)),
    ((constants.SEASON_2, ), re.compile(r"season[_\- ]?(:?2|II)", re.I)),
    ((constants.SECRET_SANTA, ), re.compile(r"secret[_\- ]?santa(:?[_\- ]?series)?", re.I)),
    ((constants.SPRING_FEVER, ), re.compile(r"spring[_\- ]?fever(:?[_\- ]?series)?", re.I)),
    ((constants.TOTALLY_AWESOME, ), re.compile(r"totally[_\- ]?awesome(:?[_\- ]?series)?", re.I)),
    ((constants.TRIUMPH, ), re.compile(r"triumph(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.TURBO, ), re.compile(r"turbo(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.VELOCITY, ), re.compile(r"velocity(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.VICTORY, ), re.compile(r"victory(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.VINDICATOR, ), re.compile(r"vindicator(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.ZEPHYR, ), re.compile(r"zephyr(:?[_\- ]?(:?series|crate))?", re.I)),
    ((constants.WWE_PROMO_CODE, ), re.compile(r"wwe[_\- ]?promo[_\- ]?code", re.I)))
SLOT_REGEX_TABLE = (
    ((constants.ANTENNA, ), re.compile(r"antennas?", re.I)),
    ((constants.AVATAR_BORDER, constants.BORDER), re.compile(r"(:?avatar[_\- ])?borders?", re.I)),
    ((constants.PLAYER_BANNER, constants.BANNER), re.compile(r"(:?player[_\- ])?banners?", re.I)),
    ((constants.ROCKET_BOOST, constants.BOOST), re.compile(r"(:?rocket[_\- ])?boosts?", re.I)),
    ((constants.BODY, constants.CAR), re.compile(r"cars?|bod(y|ies)", re.I)),
    ((constants.ANIMATED_DECAL, constants.DECAL), re.compile(r"(:?animated[_\- ])?decals?", re.I)),
    ((constants.ENGINE_AUDIO, constants.AUDIO), re.compile(r"(:?engine[_\- ])?audios?", re.I)),
    ((constants.GIFT_PACK, ), re.compile(r"gift[_\- ]?packs?", re.I)),
    ((constants.GOAL_EXPLOSION, constants.EXPLOSION), re.compile(r"(:?goal[_\- ])?explosions?", re.I)),
    ((constants.PAINT_FINISH, ), re.compile(r"paint[_\- ]?finish(es)?", re.I)),
    ((constants.PLAYER_ANTHEM, constants.ANTHEM, ), re.compile(r"(:?player[_\- ])?anthems?", re.I)),
    ((constants.PLAYER_TITLE, constants.TITLE, ), re.compile(r"(:?player[_\- ])?titles?", re.I)),
    ((constants.TOPPER, constants.HAT), re.compile(r"toppers?|hats?", re.I)),
    ((constants.TRAIL, ), re.compile(r"trails?", re.I)),
    ((constants.WHEEL, ), re.compile(r"wheels?", re.I)))


class RocketLeagueException(Exception):
    pass


class InvalidCredits(RocketLeagueException):
    pass


class NoMatch(RocketLeagueException):
    pass


class InvalidQuantity(RocketLeagueException):
    pass


class ItemNotFound(RocketLeagueException):
    pass


def validate_credits(credits_: int):
    if credits_ % 10 or credits_ < 0:
        raise InvalidCredits()


def price_from_text(text: str) -> typing.Tuple[int, int]:
    if "k" in text:
        text = text.replace(" k", "")
        price = text.split(" - ")
        return int(float(price[0]) * 1000), int(float(price[1]) * 1000)
    else:
        price = text.split(" - ")
        return int(price[0]), int(price[1])


class Name:
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def compare_names_with_regex(name_1: str, name_2: str,
                                 method: typing.Callable[[str, str, re.RegexFlag], re.Match]) -> bool:
        name_1 = unidecode.unidecode(name_1)
        name_2 = unidecode.unidecode(name_2)
        regex = re.sub(r"[_\- ]", r"[_\- ]?", name_1)
        return bool(method(regex, name_2, re.I))

    @staticmethod
    def compare_names(name_1: str, name_2: str) -> bool:
        return Name.compare_names_with_regex(name_1, name_2, re.fullmatch)

    @staticmethod
    def contains_name(name_1: str, name_2: str) -> bool:
        return Name.compare_names_with_regex(name_1, name_2, re.match)

    def compare(self, other: Name) -> bool:
        return self.compare_names(self.name, other.name)


class NameWithComplement(Name):
    def __init__(self, name: str, complement: str):
        super().__init__(name)
        self.complement = complement

    def compare(self, other: Name) -> bool:
        return isinstance(other, self.__class__) and self.compare_names(self.name, other.name) and \
            self.compare_names(self.complement, self.complement)


class DecalName(NameWithComplement):
    pass


class NameWithKind(NameWithComplement):
    pass


def identify_name(name: str) -> typing.Union[Name, DecalName, NameWithKind]:
    kind_search = re.search(r": (\w+)", name, re.I)
    if kind_search:
        return NameWithKind(name.replace(kind_search.group(0), ""), kind_search.group(1))
    car_search = re.search(r" \(([\w\s]+)\)| \[([\w\s]+)]", name, re.I)
    if car_search:
        car = car_search.group(1)
        if car is None:
            car = car_search.group(2)
        return DecalName(name.replace(car_search.group(0), ""), car)
    return Name(name)


def compare_names(name_1: str, name_2: str) -> bool:
    name_1 = identify_name(name_1)
    name_2 = identify_name(name_2)
    return name_1.compare(name_2)


class RegexBasedModule:
    def __init__(self, regex_table):
        self.regex_table = regex_table

    @functools.lru_cache
    def compare(self, attribute_1: str, attribute_2: str) -> bool:
        attribute_1 = self.get_repr(attribute_1, -1)
        return attribute_1 is not None and attribute_1 == self.get_repr(attribute_2, -1)

    @functools.lru_cache
    def get_repr(self, attribute: str, index: int = 0) -> typing.Optional[str]:
        for alias, pattern in self.regex_table:
            if pattern.fullmatch(attribute):
                return alias[index]

    @functools.lru_cache
    def is_exactly(self, key: str, attribute: str) -> bool:
        for alias, pattern in self.regex_table:
            if key in alias:
                return bool(pattern.fullmatch(attribute))
        return False

    def from_text(self, text: str) -> typing.Optional[str]:
        for _, pattern in self.regex_table:
            search = pattern.search(text)
            if search:
                return search.group(0)

    def has(self, attributes: typing.Iterable[str], attribute: str) -> bool:
        return any(self.compare(attribute, attribute_) for attribute_ in attributes)

    def get_repr_from_iterable(self, attributes: typing.Iterable[str], attribute: str) -> typing.Optional[str]:
        for attribute_ in attributes:
            if self.compare(attribute, attribute_):
                return attribute_

    def match(self, attributes: typing.Iterable[str], attribute: str):
        if not self.has(attributes, attribute):
            raise NoMatch()

    def is_valid(self, attribute: str):
        return bool(self.get_repr(attribute))


color_utils = RegexBasedModule(COLOR_REGEX_TABLE)
rarity_utils = RegexBasedModule(RARITY_REGEX_TABLE)
certified_utils = RegexBasedModule(CERTIFIED_REGEX_TABLE)
slot_utils = RegexBasedModule(SLOT_REGEX_TABLE)
platform_utils = RegexBasedModule(PLATFORM_REGEX_TABLE)
serie_utils = RegexBasedModule(SERIE_REGEX_TABLE)


class DataIdentityItem:
    __slots__ = "name", "slots", "rarities"

    def __init__(self, name: str, slots: typing.Iterable[str], rarities: typing.Iterable[str]):
        self.name = name
        self.slots = slots
        self.rarities = rarities

    def match(self, identity_item: IdentityItem):
        slot_utils.match(self.slots, identity_item.slot)
        rarity_utils.match(self.rarities, identity_item.rarity)


class IdentityItem:
    __slots__ = "name", "rarity", "slot"

    def __init__(self, name: str, rarity: str, slot: str):
        self.rarity = rarity
        self.slot = slot
        self.name = name

    def compare_identity(self, other: IdentityItem) -> bool:
        return compare_names(self.name, other.name) and rarity_utils.compare(self.rarity, other.rarity) and \
            slot_utils.compare(self.slot, other.slot)


Prices = typing.Tuple[typing.Tuple[int, int], int]
PriceTableArgument = typing.Dict[str, typing.Dict[str, Prices]]


class PriceTable:
    def __init__(self, price_table: PriceTableArgument):
        self.price_table = price_table

    def get_prices(self, platform: str, color: str) -> Prices:
        return self.price_table[self.get_compact_platform(platform)][self.get_compact_color(color)]

    @staticmethod
    def get_compact_platform(platform: str) -> typing.Optional[str]:
        return platform_utils.get_repr_from_iterable(constants.COMPACTED_PLATFORMS, platform)

    @staticmethod
    def get_compact_color(color: str) -> typing.Optional[str]:
        return color_utils.get_repr_from_iterable(constants.COMPACTED_COLORS, color)


class ItemWithPriceTable(IdentityItem, PriceTable):
    __slots__ = "name", "rarity", "slot", "price_table"

    def __init__(self, name: str, rarity: str, slot: str, price_table: PriceTableArgument):
        super().__init__(name, rarity, slot)
        PriceTable.__init__(self, price_table)


class DataItem(IdentityItem):
    __slots__ = "name", "slot", "rarity", "colors", "certificates", "platforms", "series"

    def __init__(self, name: str, slot: str, rarity: str,
                 colors: typing.Optional[typing.Iterable[str]] = None,
                 certificates: typing.Optional[typing.Iterable[str]] = None,
                 platforms: typing.Optional[typing.Iterable[str]] = None,
                 series: typing.Optional[typing.Iterable[str]] = None):
        self.series = series
        self.certificates = certificates
        self.platforms = platforms
        self.colors = colors
        super().__init__(name, rarity, slot)

    def match(self, item: typing.Union[ReprItem, BaseItem]):
        if isinstance(item, BaseItem):
            if self.platforms is not None:
                platform_utils.match(self.platforms, item.platform)
            if self.series is not None:
                serie_utils.match(self.series, item.serie)
            if self.certificates is not None:
                certified_utils.match(self.certificates, item.certified)
        if isinstance(item, ReprItem) and self.colors is not None:
            color_utils.match(self.colors, item.color)

    def can_match(self, item: typing.Union[ReprItem, BaseItem]) -> bool:
        try:
            self.match(item)
        except NoMatch:
            return False
        else:
            return True


class DataItemWithPriceTable(DataItem, PriceTable):
    __slots__ = "name", "slot", "rarity", "colors", "certificates", "platforms", "series", "price_table"

    def __init__(self, name: str, slot: str, rarity: str, price_table: PriceTableArgument,
                 colors: typing.Optional[typing.Iterable[str]] = None,
                 certificates: typing.Optional[typing.Iterable[str]] = None,
                 platforms: typing.Optional[typing.Iterable[str]] = None,
                 series: typing.Optional[typing.Iterable[str]] = None):
        super().__init__(name, slot, rarity, colors, certificates, platforms, series)
        PriceTable.__init__(self, price_table)

    def to_item_with_price(self, quantity: int, blueprint: bool, platform: str, serie: str, trade_lock: bool,
                           acquired: datetime.datetime, favorite: bool = False, archived: bool = False,
                           color: str = constants.DEFAULT, certified: str = constants.NONE) -> ItemWithPrice:
        prices = self.get_prices(platform, color)
        item_with_price = ItemWithPrice(self.name, self.slot, self.rarity, quantity, blueprint, platform, prices[0],
                                        prices[1], serie, trade_lock, acquired, favorite, archived, color, certified)
        self.match(item_with_price)
        return item_with_price


class HasPrice:
    def __init__(self, price: typing.Tuple[int, int], crafting_cost: int):
        self.price = price
        self.crafting_cost = crafting_cost

    @property
    def price(self) -> typing.Tuple[int, int]:
        return self._price

    @price.setter
    def price(self, price: typing.Tuple[int, int]):
        min_price, max_price = price
        validate_credits(min_price)
        validate_credits(max_price)
        self._price = price

    @property
    def crafting_cost(self) -> int:
        return self._crafting_cost

    @crafting_cost.setter
    def crafting_cost(self, crafting_cost: int):
        validate_credits(crafting_cost)
        self._crafting_cost = crafting_cost

    def get_price_formatted(self, round_: bool = True) -> str:
        if round_ and self.price[0] > 1000 and self.price[1] > 1000:
            return f"{round(self.price[0] / 1000, 2)} - {round(self.price[1] / 1000, 2)} k"
        return f"{self.price[0]} - {self.price[1]}"


class ReprItem:
    def __init__(self, name: str, slot: str, blueprint: bool, color: str = constants.DEFAULT):
        self.name = name
        self.slot = slot
        self.blueprint = blueprint
        self.color = color

    def compare_repr(self, other: ReprItem) -> bool:
        return self.blueprint == other.blueprint and compare_names(self.name, other.name) and \
            slot_utils.compare(self.slot, other.slot) and color_utils.compare(self.color, other.color)


class BaseItem(IdentityItem, ReprItem):
    __slots__ = "name", "slot", "rarity", "blueprint", "color", "serie", "certified", "platform"

    def __init__(self, name: str, slot: str, rarity: str, blueprint: bool, serie: str, platform: str,
                 certified: str = constants.NONE, color: str = constants.DEFAULT):
        IdentityItem.__init__(self, name, rarity, slot)
        ReprItem.__init__(self, name, slot, blueprint, color)
        self.serie = serie
        self.certified = certified
        self.platform = platform

    def compare_base_item(self, other: BaseItem) -> bool:
        return compare_names(self.name, other.name) and slot_utils.compare(self.slot, other.slot) and \
            rarity_utils.compare(self.rarity, other.rarity) and self.blueprint == other.blueprint and \
            color_utils.compare(self.color, other.color) and serie_utils.compare(self.serie, other.serie) and \
            certified_utils.compare(self.certified, other.certified) and \
            platform_utils.compare(self.platform, other.platform)

    def is_non_crate(self):
        return serie_utils.is_exactly(constants.NON_CRATE, self.serie)


class BaseItemWithPrice(BaseItem, HasPrice):
    __slots__ = "name", "slot", "rarity", "blueprint", "price", "crafting_cost", "color"

    def __init__(self, name: str, slot: str, rarity: str, blueprint: bool, price: tuple[int, int], crafting_cost: int,
                 color: str = None):
        super().__init__(name, slot, rarity, blueprint, color)
        HasPrice.__init__(self, price, crafting_cost)


class Item(BaseItem):
    __slots__ = "name", "slot", "rarity", "_quantity", "blueprint", "serie", "trade_lock", "platform", "favorite", \
        "archived", "color", "certified"

    def __init__(self, name: str, slot: str, rarity: str, quantity: int, blueprint: bool, serie: str, trade_lock: bool,
                 platform: str, acquired: datetime.datetime, favorite: bool = False, archived: bool = False,
                 color: str = constants.DEFAULT, certified: str = constants.NONE):
        self.archived = archived
        self.quantity = quantity
        self.trade_lock = trade_lock
        self.favorite = favorite
        self.acquired = acquired
        super().__init__(name, slot, rarity, blueprint, serie, platform, certified, color)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        if quantity < 0:
            raise InvalidQuantity()
        self._quantity = quantity


class ItemWithPrice(Item, HasPrice):
    def __init__(self, name: str, slot: str, rarity: str, quantity: int, blueprint: bool, platform: str,
                 price: typing.Tuple[int, int], crafting_cost: int, serie: str, trade_lock: bool,
                 acquired: datetime.datetime, favorite: bool = False, archived: bool = False,
                 color: str = constants.DEFAULT, certified: str = constants.NONE):
        super().__init__(name, slot, rarity, quantity, blueprint, serie, trade_lock, platform, acquired, favorite,
                         archived, color, certified)
        HasPrice.__init__(self, price, crafting_cost)


class Account:
    def __init__(self, name: str, platform: str):
        self.name = name
        self.platform = platform


def get_price(price_table: typing.Iterable[DataItemWithPriceTable], item: IdentityItem, platform: str,
              color: str = constants.DEFAULT) -> typing.Optional[tuple[int, int], int]:
    for base_item_with_price in price_table:
        if base_item_with_price.compare_identity(item):
            return base_item_with_price.get_prices(platform, color)


class Propose:
    __slots__ = "account", "_credits", "items"

    def __init__(self, credits_: int, items: typing.Tuple[Item, ...], account: Account):
        self.account = account
        self.credits = credits_
        self.items = items

    @property
    def credits(self) -> int:
        return self._credits

    @credits.setter
    def credits(self, credits_: int):
        validate_credits(credits_)
        self._credits = credits_

    def get_total_price(self):
        items_with_price = filter(lambda item: isinstance(item, ItemWithPrice), self.items)
        min_price = sum(map(lambda item: item.price[0], items_with_price))
        max_price = sum(map(lambda item: item.price[1], items_with_price))
        return min_price + self.credits, max_price + self.credits


class Trade:
    __slots__ = "proposes", "date"

    def __init__(self, proposes: typing.Tuple[Propose, Propose], date: datetime.datetime):
        self.proposes = proposes
        self.date = date

    def get_kind(self) -> typing.Optional[typing.Literal["item_for_item", "item_for_credit"]]:
        if len(self.proposes[0].items) > 0 and len(self.proposes[1].items) > 0:
            return constants.ITEM_FOR_ITEM
        elif self.proposes[0].credits and not self.proposes[1].credits:
            return constants.ITEM_FOR_CREDIT
        elif self.proposes[1].credits and not self.proposes[0].credits:
            return constants.ITEM_FOR_CREDIT
        else:
            return None

    def get_best_propose(self) -> typing.Literal[0, 1]:
        average_1 = numpy.mean(self.proposes[0].get_total_price())
        average_2 = numpy.mean(self.proposes[1].get_total_price())
        if average_1 > average_2:
            return 1
        else:
            return 0


class ItemDatabase:
    def __init__(self, database: str):
        self.connection = sqlite3.connect(database, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
        name TINYTEXT NOT NULL,
        slot TINYTEXT NOT NULL,
        rarity TINYTEXT NOT NULL,
        quantity MEDIUMINT NOT NULL,
        blueprint BOOL NOT NULL,
        serie TINYTEXT NOT NULL,
        trade_lock BOOL NOT NULL,
        platform TINYTEXT NOT NULL,
        acquired timestamp NOT NULL,
        favorite BOOL NOT NULL DEFAULT false,
        archived BOOL NOT NULL DEFAULT false,
        color TINYTEXT NOT NULL DEFAULT "Default",
        certified TINYTEXT NOT NULL DEFAULT "None",
        id INTEGER PRIMARY KEY AUTOINCREMENT
        )""")
        self.connection.commit()

    def add_item(self, item: Item) -> int:
        self.cursor.execute("""
        INSERT INTO inventory (name, slot, rarity, quantity, blueprint, serie, trade_lock, platform, acquired, favorite, 
        archived, color, certified) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (item.name, item.slot, item.rarity, item.quantity, item.blueprint, item.serie, item.trade_lock,
              item.platform, item.acquired, item.favorite, item.archived, item.color, item.certified))
        self.connection.commit()
        return self.cursor.lastrowid

    def delete_item(self, id_: int):
        self.cursor.execute("DELETE FROM inventory WHERE id = ?;", (id_,))
        self.connection.commit()

    def get_items(self) -> dict[int, Item]:
        self.cursor.execute("SELECT * FROM inventory;")
        return {values[-1]: values[:-1] for values in self.cursor.fetchall()}
