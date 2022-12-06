from __future__ import annotations

import datetime
import functools
import sqlite3
import typing
import re
import unidecode

# Certificates
AVIATOR = "Aviator"
ACROBAT = "Acrobat"
GOALKEEPER = "Goalkeeper"
GUARDIAN = "Guardian"
JUGGLER = "Juggler"
NONE = "None"
PARAGON = "Paragon"
PLAYMAKER = "Playmaker"
SCORER = "Scorer"
SHOW_OFF = "Show-off"
SNIPER = "Sniper"
STRIKER = "Striker"
SWEEPER = "Sweeper"
TACTICIAN = "Tactician"
TURTLE = "Turtle"
VICTOR = "Victor"
# Colors
BLACK = "Black"
BURNT_SIENNA = "Burnt Sienna"
SIENNA = "Sienna"
BS = "BS"
COBALT = "Cobalt"
BLUE = "Blue"
CRIMSON = "Crimson"
RED = "Red"
CARMESIM = "Carmesim"
DEFAULT = "Default"
NORMAL = "Normal"
REGULAR = "Regular"
FOREST_GREEN = "Forest Green"
GREEN = "Green"
FG = "FG"
GREY = "Grey"
LIME = "Lime"
ORANGE = "Orange"
PINK = "Pink"
PURPLE = "Purple"
SAFFRON = "Saffron"
YELLOW = "Yellow"
SKY_BLUE = "Sky Blue"
SB = "SB"
TITANIUM_WHITE = "Titanium White"
WHITE = "White"
TW = "TW"
GOLD = "Gold"
# Platforms
PC = "Pc"
COMPUTER = "Computer"
STEAM = "Steam"
EPIC_GAMES = "Epic Games"
EPIC = "Epic"
PS4 = "Ps4"
PLAY_4 = "Play 4"
PLAYSTATION_4 = "Playstation 4"
SWITCH = "Switch"
XBOX = "Xbox"
# Rarities
BLACK_MARKET = "Black market"
BM = "BM"
COMMON = "Common"
EXOTIC = "Exotic"
IMPORT = "Import"
IMPORTED = "Imported"
LEGACY = "Legacy"
LIMITED = "Limited"
PREMIUM = "Premium"
RARE = "Rare"
UNCOMMON = "Uncommon"
VERY_RARE = "Very rare"
VR = "VR"
# Series
ACCELERATOR = "Accelerator"
ACCOLADE_1 = "Accolade 1"
ACCOLADE_2 = "Accolade 2"
AURIGA = "Auriga"
BEACH_BLAST = "Beach Blast"
BONUS_GIFT = "Bonus Gift"
CHAMPIONS_1 = "Champions 1"
CHAMPIONS_2 = "Champions 2"
CHAMPIONS_3 = "Champions 3"
CHAMPIONS_4 = "Champions 4"
DORADO = "Dorado"
ELEVATION = "Elevation"
FEROCITY = "Ferocity"
FORNAX = "Fornax"
GOLDEN_EGG_2022 = "Golden Egg 2022"
GOLDEN_EGG_2020 = "Golden Egg 2020"
GOLDEN_EGG_2019 = "Golden Egg 2019"
GOLDEN_EGG_2018 = "Golden Egg 2018"
GOLDEN_GIFT_2021 = "Golden Gift 2021"
GOLDEN_GIFT_2020 = "Golden Gift 2020"
GOLDEN_GIFT_2019 = "Golden Gift 2019"
GOLDEN_GIFT_2018 = "Golden Gift 2018"
GOLDEN_GIFT_BASKET_2022 = "Golden Gift Basket 2022"
GOLDEN_LANTERN_2021 = "Golden Lantern 2021"
GOLDEN_LANTERN_2020 = "Golden Lantern 2020"
GOLDEN_LANTERN_2019 = "Golden Lantern 2019"
GOLDEN_MOON = "Golden Moon"
GOLDEN_PUMPKIN_2022 = "Golden Pumpkin 2022"
GOLDEN_PUMPKIN_2020 = "Golden Pumpkin 2020"
GOLDEN_PUMPKIN_2019 = "Golden Pumpkin 2019"
GOLDEN_PUMPKIN_2018 = "Golden Pumpkin 2018"
HAUNTED_HALLOWS = "Haunted Hallows"
IGNITION = "Ignition"
IMPACT = "Impact"
MOMENTUM = "Momentum"
NITRO = "Nitro"
NON_CRATE = "Non Crate"
OVERDRIVE = "Overdrive"
POST_GAME = "Post Game"
PLAYERS_CHOICE = "Player\'s Choice"
RLCS_REWARD = "RLCS Reward"
REVIVAL = "Revival"
ROCKETPASS_1 = "Rocketpass 1"
ROCKETPASS_2 = "Rocketpass 2"
ROCKETPASS_3 = "Rocketpass 3"
ROCKETPASS_4 = "Rocketpass 4"
ROCKETPASS_5 = "Rocketpass 5"
ROCKETPASS_6 = "Rocketpass 6"
ROCKETPASS_7 = "Rocketpass 7"
ROCKETPASS_8 = "Rocketpass 8"
ROCKETPASS_9 = "Rocketpass 9"
ROCKETPASS_10 = "Rocketpass 10"
ROCKETPASS_11 = "Rocketpass 11"
ROCKETPASS_12 = "Rocketpass 12"
ROCKETPASS_13 = "Rocketpass 13"
ROCKETPASS_14 = "Rocketpass 14"
SELECT_FAVORITES_ITEM = "Select Favorites Item"
SELECT_FAVORITES_2 = "Select Favorites 2"
SEASON_1 = "Season 1"
SEASON_2 = "Season 2"
SECRET_SANTA = "Secret Santa"
SPRING_FEVER = "Spring Fever"
TOTALLY_AWESOME = "Totally Awesome"
TRIUMPH = "Triumph"
TURBO = "Turbo"
VELOCITY = "Velocity"
VICTORY = "Victory"
VINDICATOR = "Vindicator"
ZEPHYR = "Zephyr"
WWE_PROMO_CODE = "WWE Promo Code"
# Slots
ANTENNA = "Antenna"
AVATAR_BORDER = "Avatar Border"
BORDER = "Border"
CAR = "Car"
BODY = "Body"
BLUEPRINTS = "Blueprints"
DECAL = "Decal"
ANIMATED_DECAL = "Animated Decal"
ENGINE_AUDIO = "Engine Audio"
GOAL_EXPLOSION = "Goal Explosion"
GIFT_PACK = "Gift Pack"
PAINT_FINISH = "Paint Finish"
ANTHEM = "Anthem"
PLAYER_ANTHEM = "Player Anthem"
BANNER = "Banner"
PLAYER_BANNER = "Player Banner"
BOOST = "Boost"
ROCKET_BOOST = "Rocket Boost"
TOPPER = "Topper"
HAT = "Hat"
TRAIL = "Trail"
WHEEL = "Wheel"
TITLE = "Title"
PLAYER_TITLE = "Player Title"

CERTIFICATES = (AVIATOR, ACROBAT, GOALKEEPER, GUARDIAN, JUGGLER, NONE, PARAGON, PLAYMAKER, SCORER,
                SHOW_OFF, SNIPER, STRIKER, SWEEPER, TACTICIAN, TURTLE, VICTOR)
COLORS = (BLACK, BURNT_SIENNA, COBALT, CRIMSON, DEFAULT, FOREST_GREEN, GREY, LIME, ORANGE, PINK,
          PURPLE, SAFFRON, SKY_BLUE, TITANIUM_WHITE, GOLD)
PLATFORMS = (PC, PS4, SWITCH, XBOX)
RARITIES = (BLACK_MARKET, COMMON, EXOTIC, IMPORT, LIMITED, PREMIUM, RARE, UNCOMMON, VERY_RARE, LEGACY)
SERIES = (
    ACCELERATOR, ACCOLADE_1, ACCOLADE_2, AURIGA, BEACH_BLAST, BONUS_GIFT, CHAMPIONS_1, CHAMPIONS_2, CHAMPIONS_3,
    CHAMPIONS_4, DORADO, ELEVATION, FEROCITY, FORNAX, GOLDEN_EGG_2018, GOLDEN_EGG_2019, GOLDEN_EGG_2020,
    GOLDEN_EGG_2022, GOLDEN_GIFT_2018, GOLDEN_GIFT_2019, GOLDEN_GIFT_2020, GOLDEN_GIFT_2021, GOLDEN_GIFT_BASKET_2022,
    GOLDEN_LANTERN_2019, GOLDEN_LANTERN_2020, GOLDEN_LANTERN_2021, GOLDEN_MOON, GOLDEN_PUMPKIN_2018,
    GOLDEN_PUMPKIN_2019, GOLDEN_PUMPKIN_2020, GOLDEN_PUMPKIN_2022, HAUNTED_HALLOWS, IGNITION, IMPACT, MOMENTUM, NITRO,
    NON_CRATE, OVERDRIVE, PLAYERS_CHOICE, RLCS_REWARD, REVIVAL, ROCKETPASS_1, ROCKETPASS_2, ROCKETPASS_3, ROCKETPASS_4,
    ROCKETPASS_5, ROCKETPASS_6, ROCKETPASS_7, ROCKETPASS_8, ROCKETPASS_9, ROCKETPASS_10, ROCKETPASS_11, ROCKETPASS_12,
    ROCKETPASS_13, ROCKETPASS_14, SELECT_FAVORITES_ITEM, SELECT_FAVORITES_2, SEASON_1, SEASON_2, SECRET_SANTA,
    SPRING_FEVER, TOTALLY_AWESOME, TRIUMPH, TURBO, VELOCITY, VICTORY, VINDICATOR, ZEPHYR, WWE_PROMO_CODE)
SLOTS = (ANTENNA, BORDER, CAR, DECAL, ENGINE_AUDIO, GOAL_EXPLOSION, PAINT_FINISH, ANTHEM, BANNER,
         BOOST, TOPPER, TRAIL, WHEEL)

COLOR_REGEX_TABLE = {
    BLACK: re.compile(r"black", re.I),
    BURNT_SIENNA: re.compile(r"burnt[_\- ]?sienna|bs|sienna", re.I),
    COBALT: re.compile(r"cobalt|blue", re.I),
    CRIMSON: re.compile(r"crimson|carmesim|red", re.I),
    DEFAULT: re.compile(r"default|regular|none", re.I),
    FOREST_GREEN: re.compile(r"forest[_\- ]green|fg|green", re.I),
    GREY: re.compile(r"grey", re.I),
    LIME: re.compile(r"lime", re.I),
    ORANGE: re.compile(r"orange", re.I),
    PINK: re.compile(r"pink", re.I),
    PURPLE: re.compile(r"purple", re.I),
    SAFFRON: re.compile(r"saffron|yellow", re.I),
    SKY_BLUE: re.compile(r"sky[_\- ]?blue|sb", re.I),
    TITANIUM_WHITE: re.compile(r"titanium[_\- ]white|white|tw", re.I),
    GOLD: re.compile(r"gold(:?en)?", re.I)}
CERTIFIED_REGEX_TABLE = {
    ACROBAT: re.compile(r"acrobat", re.I),
    AVIATOR: re.compile(r"aviator", re.I),
    GOALKEEPER: re.compile(r"goalkeeper", re.I),
    GUARDIAN: re.compile(r"guardian", re.I),
    JUGGLER: re.compile(r"juggler", re.I),
    NONE: re.compile(r"default|regular|none", re.I),
    PARAGON: re.compile(r"paragon", re.I),
    PLAYMAKER: re.compile(r"playmaker", re.I),
    SCORER: re.compile(r"scorer", re.I),
    SHOW_OFF: re.compile(r"show[_\- ]?off", re.I),
    SNIPER: re.compile(r"sniper", re.I),
    STRIKER: re.compile(r"striker", re.I),
    SWEEPER: re.compile(r"sweeper", re.I),
    TACTICIAN: re.compile(r"tactician", re.I),
    TURTLE: re.compile(r"turtle", re.I),
    VICTOR: re.compile(r"victor", re.I)}
PLATFORM_REGEX_TABLE = {
    PC: re.compile(r"pc|computer|epic([_\- ]games)?|steam", re.I),
    XBOX: re.compile(r"xbox", re.I),
    PS4: re.compile(r"(:?ps|play(:?station)?)[_\- ]?4?", re.I),
    SWITCH: re.compile(r"switch", re.I)}
RARITY_REGEX_TABLE = {
    BLACK_MARKET: re.compile(r"black[_\- ]?markets?|bms?", re.I),
    COMMON: re.compile(r"commons?", re.I),
    EXOTIC: re.compile(r"exotics?", re.I),
    IMPORT: re.compile(r"imports?", re.I),
    LEGACY: re.compile(r"legac(y|ies)", re.I),
    LIMITED: re.compile(r"limiteds?", re.I),
    PREMIUM: re.compile(r"premiums?", re.I),
    RARE: re.compile(r"rares?", re.I),
    UNCOMMON: re.compile(r"uncommons?", re.I),
    VERY_RARE: re.compile(r"very[_\- ]?rares?|vrs?", re.I)}
SERIE_REGEX_TABLE = {
    ACCELERATOR: re.compile(r"accelerator(:?[_\- ]?series)?", re.I),
    ACCOLADE_1: re.compile(r"accolade[_\- ]?[1I](:?[_\- ]?series)?", re.I),
    ACCOLADE_2: re.compile(r"accolade[_\- ]?(2|II)(:?[_\- ]?series)?", re.I),
    AURIGA: re.compile(r"auriga(:?[_\- ]?series)?", re.I),
    BEACH_BLAST: re.compile(r"beach[_\- ]?blast(:?[_\- ]?series)?", re.I),
    BONUS_GIFT: re.compile(r"bonus[_\- ]?gift", re.I),
    CHAMPIONS_1: re.compile(r"champions[_\- ]?1(:?[_\- ]?series)?", re.I),
    CHAMPIONS_2: re.compile(r"champions[_\- ]?2(:?[_\- ]?series)?", re.I),
    CHAMPIONS_3: re.compile(r"champions[_\- ]?3(:?[_\- ]?series)?", re.I),
    CHAMPIONS_4: re.compile(r"champions[_\- ]?4(:?[_\- ]?series)?", re.I),
    DORADO: re.compile(r"dorado(:?[_\- ]?series)?", re.I),
    ELEVATION: re.compile(r"elevation(:?[_\- ]?series)?", re.I),
    FEROCITY: re.compile(r"ferocity(:?[_\- ]?series)?", re.I),
    FORNAX: re.compile(r"fornax(:?[_\- ]?series)?", re.I),
    GOLDEN_EGG_2022: re.compile(r"golden[_\- ]?egg[_\- ]?(:?'22|2022)", re.I),
    GOLDEN_EGG_2020: re.compile(r"golden[_\- ]?egg[_\- ]?(:?'20|2020)", re.I),
    GOLDEN_EGG_2019: re.compile(r"golden[_\- ]?egg[_\- ]?(:?'19|2019)", re.I),
    GOLDEN_EGG_2018: re.compile(r"golden[_\- ]?egg[_\- ]?(:?'18|2018)", re.I),
    GOLDEN_GIFT_2021: re.compile(r"golden[_\- ]?gift[_\- ]?(:?'21|2021)", re.I),
    GOLDEN_GIFT_2020: re.compile(r"golden[_\- ]?gift[_\- ]?(:?'20|2020)", re.I),
    GOLDEN_GIFT_2019: re.compile(r"golden[_\- ]?gift[_\- ]?(:?'19|2019)", re.I),
    GOLDEN_GIFT_2018: re.compile(r"golden[_\- ]?gift[_\- ]?(:?'18|2018)", re.I),
    GOLDEN_GIFT_BASKET_2022: re.compile(r"golden[_\- ]?gift[_\- ]?basket[_\- ]?(:?'22|2022)", re.I),
    GOLDEN_LANTERN_2021: re.compile(r"golden[_\- ]?lantern[_\- ]?(:?'21|2021)", re.I),
    GOLDEN_LANTERN_2020: re.compile(r"golden[_\- ]?lantern[_\- ]?(:?'20|2020)", re.I),
    GOLDEN_LANTERN_2019: re.compile(r"golden[_\- ]?lantern[_\- ]?(:?'19|2019)", re.I),
    GOLDEN_MOON: re.compile(r"golden[_\- ]?moon", re.I),
    GOLDEN_PUMPKIN_2022: re.compile(r"golden[_\- ]?pumpkin[_\- ]?(:?'22|2022)", re.I),
    GOLDEN_PUMPKIN_2020: re.compile(r"golden[_\- ]?pumpkin[_\- ]?(:?'20|2020)", re.I),
    GOLDEN_PUMPKIN_2019: re.compile(r"golden[_\- ]?pumpkin[_\- ]?(:?'19|2019)", re.I),
    GOLDEN_PUMPKIN_2018: re.compile(r"golden[_\- ]?pumpkin[_\- ]?(:?'18|2018)", re.I),
    HAUNTED_HALLOWS: re.compile(r"haunted[_\- ]?hallows(:?[_\- ]?series)?", re.I),
    IGNITION: re.compile(r"ignition(:?[_\- ]?series)?", re.I),
    IMPACT: re.compile(r"impact(:?[_\- ]?series)?", re.I),
    MOMENTUM: re.compile(r"momentum(:?[_\- ]?series)?", re.I),
    NITRO: re.compile(r"nitro(:?[_\- ]?series)?", re.I),
    NON_CRATE: re.compile(r"non[_\- ]?crate|post[_\- ]?game", re.I),
    OVERDRIVE: re.compile(r"overdrive(:?[_\- ]?series)?", re.I),
    PLAYERS_CHOICE: re.compile(r"player'?s?[_\- ]?choice(:?[_\- ]?series)?", re.I),
    REVIVAL: re.compile(r"revival([_\- ]?series)?", re.I),
    ROCKETPASS_1: re.compile(r"rocketpass[_\- ]?1", re.I),
    ROCKETPASS_2: re.compile(r"rocketpass[_\- ]?2", re.I),
    ROCKETPASS_3: re.compile(r"rocketpass[_\- ]?3", re.I),
    ROCKETPASS_4: re.compile(r"rocketpass[_\- ]?4", re.I),
    ROCKETPASS_5: re.compile(r"rocketpass[_\- ]?5", re.I),
    ROCKETPASS_6: re.compile(r"rocketpass[_\- ]?6", re.I),
    ROCKETPASS_7: re.compile(r"rocketpass[_\- ]?7", re.I),
    ROCKETPASS_8: re.compile(r"rocketpass[_\- ]?8", re.I),
    ROCKETPASS_9: re.compile(r"rocketpass[_\- ]?9", re.I),
    ROCKETPASS_10: re.compile(r"rocketpass[_\- ]?10", re.I),
    ROCKETPASS_11: re.compile(r"rocketpass[_\- ]?11", re.I),
    ROCKETPASS_12: re.compile(r"rocketpass[_\- ]?12", re.I),
    ROCKETPASS_13: re.compile(r"rocketpass[_\- ]?13", re.I),
    ROCKETPASS_14: re.compile(r"rocketpass[_\- ]?14", re.I),
    RLCS_REWARD: re.compile(r"rlcs[_\- ]?reward", re.I),
    SELECT_FAVORITES_ITEM: re.compile(r"select[_\- ]?favorites[_\- ]?item(:?[_\- ]?series)?", re.I),
    SELECT_FAVORITES_2: re.compile(r"select[_\- ]?favorites(:?[_\- ]?series)?[_\- ]?2", re.I),
    SEASON_1: re.compile(r"season[_\- ]?[1I]", re.I),
    SEASON_2: re.compile(r"season[_\- ]?(:?2|II)", re.I),
    SECRET_SANTA: re.compile(r"secret[_\- ]?santa(:?[_\- ]?series)?", re.I),
    SPRING_FEVER: re.compile(r"spring[_\- ]?fever(:?[_\- ]?series)?", re.I),
    TOTALLY_AWESOME: re.compile(r"totally[_\- ]?awesome(:?[_\- ]?series)?", re.I),
    TRIUMPH: re.compile(r"triumph(:?[_\- ]?series)?", re.I),
    TURBO: re.compile(r"turbo(:?[_\- ]?series)?", re.I),
    VELOCITY: re.compile(r"velocity(:?[_\- ]?series)?", re.I),
    VICTORY: re.compile(r"victory(:?[_\- ]?series)?", re.I),
    VINDICATOR: re.compile(r"vindicator(:?[_\- ]?series)?", re.I),
    ZEPHYR: re.compile(r"zephyr(:?[_\- ]?series)?", re.I),
    WWE_PROMO_CODE: re.compile(r"wwe[_\- ]?promo[_\- ]?code", re.I)}
SLOT_REGEX_TABLE = {
    ANTENNA: re.compile(r"antennas?", re.I),
    BORDER: re.compile(r"avatar[_\- ]?borders?", re.I),
    BANNER: re.compile(r"(player)?[_\- ]?banners?", re.I),
    BOOST: re.compile(r"(rocket)?[_\- ]?boosts?", re.I),
    CAR: re.compile(r"cars?|bod(y|ies)", re.I),
    DECAL: re.compile(r"(animated[_\- ])?decals?", re.I),
    ENGINE_AUDIO: re.compile(r"engine[_\- ]?audios?", re.I),
    GIFT_PACK: re.compile(r"gift[_\- ]?packs?", re.I),
    GOAL_EXPLOSION: re.compile(r"goal[_\- ]?explosions?", re.I),
    PAINT_FINISH: re.compile(r"paint[_\- ]?finish(es)?", re.I),
    ANTHEM: re.compile(r"(player[_\- ])?anthems?", re.I),
    TITLE: re.compile(r"(player[_\- ])?titles?", re.I),
    TOPPER: re.compile(r"toppers?|hats?", re.I),
    TRAIL: re.compile(r"trails?", re.I),
    WHEEL: re.compile(r"wheels?", re.I)}


class RocketLeagueException(Exception):
    pass


class InvalidCredits(RocketLeagueException):
    pass


class NoMatch(RocketLeagueException):
    pass


class InvalidQuantity(RocketLeagueException):
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
        kind_search = re.search(r": (\w+)", name, re.I)
        if kind_search:
            self.name = name.replace(kind_search.group(0), "")
            self.kind = kind_search.group(1)
            self.car = None
            return
        car_search = re.search(r" \(([\w\s]+)\)| \[([\w\s]+)]", name, re.I)
        if car_search:
            car = car_search.group(1)
            if car is None:
                car = car_search.group(2)
            self.name = name.replace(car_search.group(0), "")
            self.car = car
            self.kind = None
            return
        self.name = name
        self.car = None
        self.kind = None

    @staticmethod
    def compare_names(name_1: str, name_2: str) -> bool:
        string_1 = re.sub(r"\W", "", unidecode.unidecode(name_1.lower()))
        string_2 = re.sub(r"\W", "", unidecode.unidecode(name_2.lower()))
        return set(string_1) == set(string_2)

    def compare(self, other: Name) -> bool:
        if self.kind is not None:
            return self.compare_names(self.name, other.name) and self.compare_names(self.kind, other.kind)
        elif self.car is not None:
            return self.compare_names(self.name, other.name) and self.compare_names(self.car, other.car)
        else:
            return self.compare_names(self.name, other.name)


def compare_names(name_1: str, name_2: str) -> bool:
    name_1 = Name(name_1)
    name_2 = Name(name_2)
    return name_1.compare(name_2)


class RegexBasedModule:
    def __init__(self, regex_table: typing.Dict[str, typing.Pattern]):
        self.regex_table = regex_table

    @functools.lru_cache
    def compare(self, attribute_1: str, attribute_2: str) -> bool:
        for pattern in self.regex_table.values():
            if pattern.fullmatch(attribute_1) and pattern.fullmatch(attribute_2):
                return True
        return False

    @functools.lru_cache
    def get_repr(self, attribute: str) -> typing.Optional[str]:
        for attribute_, pattern in self.regex_table.items():
            if pattern.fullmatch(attribute_) and pattern.fullmatch(attribute):
                return attribute_

    @functools.lru_cache
    def is_exactly(self, key: str, attribute: str) -> bool:
        return bool(self.regex_table[key].fullmatch(attribute))

    def from_text(self, text: str) -> typing.Optional[str]:
        for pattern in self.regex_table.values():
            search = pattern.search(text)
            if search:
                return search.group(0)

    def has(self, attributes: typing.Iterable[str], attribute: str) -> bool:
        return any(self.compare(attribute, attribute_) for attribute_ in attributes)

    def get_respective_from_iterable(self, attributes: typing.Iterable[str], attribute: str) -> typing.Optional[str]:
        for attribute_ in attributes:
            if self.compare(attribute, attribute_):
                return attribute_

    def match(self, attributes: typing.Iterable[str], attribute: str):
        if not self.has(attributes, attribute):
            raise NoMatch()


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
    PLATFORMS = ("pc", "xbox", "switch", "ps4")
    COLORS = ("black", "bs", "blue", "red", "none", "fg", "grey", "lime", "orange", "pink", "purple",
              "yellow", "sb", "tw", "gold")

    def __init__(self, price_table: PriceTableArgument):
        self.price_table = price_table

    def get_prices(self, platform: str, color: str) -> Prices:
        return self.price_table[self.get_compact_platform(platform)][self.get_compact_color(color)]

    @classmethod
    def get_compact_platform(cls, platform: str) -> typing.Optional[str]:
        return platform_utils.get_respective_from_iterable(cls.PLATFORMS, platform)

    @classmethod
    def get_compact_color(cls, color: str) -> typing.Optional[str]:
        return color_utils.get_respective_from_iterable(cls.COLORS, color)


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

    def match(self, item: Item):
        if self.colors is not None:
            color_utils.match(self.colors, item.color)
        if self.platforms is not None:
            platform_utils.match(self.platforms, item.platform)
        if self.series is not None:
            serie_utils.match(self.series, item.serie)
        if self.certificates is not None:
            certified_utils.match(self.certificates, item.certified)

    def to_item(self, *args, **kwargs) -> Item:
        return Item(self.name, self.slot, self.rarity, *args, **kwargs)


class DataItemWithPriceTable(DataItem, PriceTable):
    __slots__ = "name", "slot", "rarity", "colors", "certificates", "platforms", "series", "price_table"

    def __init__(self, name: str, slot: str, rarity: str, price_table: PriceTableArgument,
                 colors: typing.Optional[typing.Iterable[str]] = None,
                 certificates: typing.Optional[typing.Iterable[str]] = None,
                 platforms: typing.Optional[typing.Iterable[str]] = None,
                 series: typing.Optional[typing.Iterable[str]] = None):
        super().__init__(name, rarity, slot, colors, certificates, platforms, series)
        PriceTable.__init__(self, price_table)

    def to_item_with_price(self, quantity: int, blueprint: bool, platform: str, serie: str, trade_lock: bool,
                           acquired: datetime.datetime, favorite: bool = False, archived: bool = False,
                           color: str = DEFAULT, certified: str = NONE) -> ItemWithPrice:

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
    def __init__(self, name: str, slot: str, blueprint: bool, color: str = DEFAULT):
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
                 certified: str = NONE, color: str = DEFAULT):
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
        return serie_utils.is_exactly(NON_CRATE, self.serie)


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
                 color: str = DEFAULT, certified: str = NONE):
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
                 acquired: datetime.datetime, favorite: bool = False, archived: bool = False, color: str = DEFAULT,
                 certified: str = NONE):
        super().__init__(name, slot, rarity, quantity, blueprint, serie, trade_lock, platform, acquired, favorite,
                         archived, color, certified)
        HasPrice.__init__(self, price, crafting_cost)


HEX_TABLE = {
    CRIMSON: "#ff4d4d",
    SKY_BLUE: "#69fff",
    PINK: "#ff8dce",
    ORANGE: "#da9a00",
    COBALT: "#8c9eff",
    BURNT_SIENNA: "#995e4d",
    TITANIUM_WHITE: "#fff",
    GREY: "#c4c4c4",
    SAFFRON: "#ff8",
    LIME: "#ccff4d",
    FOREST_GREEN: "#329536",
    BLACK: "#000",
    PURPLE: "#e974fd",
    GOLD: "#F4B900",
}

RGB_TABLE = {
    RARE: (116, 151, 235),
    VERY_RARE: (158, 124, 252),
    IMPORT: (227, 90, 82),
    EXOTIC: (236, 219, 108),
    BLACK_MARKET: (255, 0, 255),
    PREMIUM: (107, 241, 174),
    LIMITED: (247, 121, 57)
}


class Account:
    def __init__(self, name: str, platform: str):
        self.name = name
        self.platform = platform


def get_price(price_table: typing.Iterable[BaseItemWithPrice], base_item: BaseItem) -> typing.Optional[tuple[int, int]]:
    for base_item_with_price in price_table:
        if base_item_with_price.compare_base_item(base_item):
            return base_item_with_price.price


class Propose:
    __slots__ = "account", "_credits", "items"

    def __init__(self, credits_: int, items: typing.Sized[Item], account: Account):
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


ITEM_FOR_ITEM: typing.Literal["item_for_item"] = "item_for_item"
ITEM_FOR_CREDIT: typing.Literal["item_for_credit"] = "item_for_credit"


class Trade:
    __slots__ = "propose_1", "propose_2", "date"

    def __init__(self, propose_1: Propose, propose_2: Propose, date: datetime.datetime):
        self.propose_1 = propose_1
        self.propose_2 = propose_2
        self.date = date

    def get_kind(self) -> typing.Optional[typing.Literal["item_for_item", "item_for_credit"]]:
        if len(self.propose_1.items) > 0 and len(self.propose_2.items) > 0:
            return ITEM_FOR_ITEM
        elif self.propose_1.credits and not self.propose_2.credits:
            return ITEM_FOR_CREDIT
        elif self.propose_2.credits and not self.propose_1.credits:
            return ITEM_FOR_CREDIT
        else:
            return None


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
