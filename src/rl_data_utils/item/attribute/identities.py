import re
from re import Pattern
from typing import Tuple, Set, Callable

from rl_data_utils.exceptions import UnrecognizableAttribute
from rl_data_utils.item.attribute.constants import BLACK, BURNT_SIENNA, BS, COBALT, BLUE, CRIMSON, RED, CARMESIM, \
    DEFAULT, REGULAR, NONE, NORMAL, FOREST_GREEN, GREEN, FG, GREY, LIME, ORANGE, PINK, PURPLE, SAFFRON, YELLOW, \
    SKY_BLUE, SB, TITANIUM_WHITE, WHITE, TW, ACROBAT, AVIATOR, GOALKEEPER, GUARDIAN, JUGGLER, PARAGON, PLAYMAKER, \
    SCORER, SHOW_OFF, SNIPER, STRIKER, SWEEPER, TACTICIAN, TURTLE, VICTOR, PC, COMPUTER, STEAM, EPIC_GAMES, XBOX, PS4, \
    PLAY_4, PLAYSTATION_4, SWITCH, ANTENNA, AVATAR_BORDER, BORDER, PLAYER_BANNER, BANNER, BLUEPRINTS, ROCKET_BOOST, \
    BOOST, BODY, CAR, DECAL, ANIMATED_DECAL, ENGINE_AUDIO, GIFT_PACK, GOAL_EXPLOSION, PAINT_FINISH, PLAYER_ANTHEM, \
    ANTHEM, PLAYER_TITLE, TITLE, TRAIL, WHEEL, BLACK_MARKET, BM, COMMON, EXOTIC, IMPORT, IMPORTED, LEGACY, LIMITED, \
    PREMIUM, RARE, UNCOMMON, VERY_RARE, VR, ACCELERATOR, ACCOLADE_1, ACCOLADE_2, AURIGA, BEACH_BLAST, BONUS_GIFT, \
    CHAMPIONS_1, CHAMPIONS_2, CHAMPIONS_3, CHAMPIONS_4, ELEVATION, FEROCITY, GOLDEN_EGG_2020, GOLDEN_EGG_2019, \
    GOLDEN_EGG_2018, GOLDEN_GIFT_2020, GOLDEN_GIFT_2019, GOLDEN_GIFT_2018, GOLDEN_LANTERN_2021, GOLDEN_LANTERN_2020, \
    GOLDEN_LANTERN_2019, GOLDEN_PUMPKIN_2020, GOLDEN_PUMPKIN_2019, GOLDEN_PUMPKIN_2018, HAUNTED_HALLOWS, IGNITION, \
    IMPACT, MOMENTUM, NITRO, NON_CRATE, OVERDRIVE, PLAYERS_CHOICE, RLCS_REWARD, SECRET_SANTA, SEASON_1, SPRING_FEVER, \
    TOTALLY_AWESOME, TRIUMPH, TURBO, VELOCITY, VICTORY, VINDICATOR, ZEPHYR, WWE_PROMO_CODE, POST_GAME, SIENNA, EPIC, \
    TOPPER, HAT


class StringIdentity:
    def __init__(self, id_: int, alias: str, regex: Pattern):
        self.id_ = id_
        self.alias = alias
        self.regex = regex


class Identity:
    def __init__(self, id_: int, string_identities: Set[StringIdentity]):
        self.id_ = id_
        self.string_identities = string_identities

    def get_string_identity_id(self, id_: int) -> StringIdentity:
        return self.get_string_identity(lambda si: si.id_ == id_)

    def get_string_identity_by_alias(self, alias: str) -> StringIdentity:
        return self.get_string_identity(lambda si: si.alias == alias)

    def get_string_identity(self, condition: Callable[[StringIdentity], bool]) -> StringIdentity:
        for string_identity in self.string_identities:
            if condition(string_identity):
                return string_identity
        raise UnrecognizableAttribute("No string identity was found.")


class Identities:
    def __init__(self, identities: Set[Identity]):
        self.identities = identities

    def get_identity(self, id_: int) -> Identity:
        for identity in self.identities:
            if identity.id_ == id_:
                return identity
        raise UnrecognizableAttribute("No identity was found.")

    def identify(self, string: str) -> Tuple[Identity, StringIdentity]:
        return self.find(lambda identity, string_identity: string_identity.regex.fullmatch(string))

    def identify_in_text(self, text: str) -> Tuple[Identity, StringIdentity]:
        return self.find(lambda identity, string_identity: string_identity.regex.match(text))

    def identify_exactly_in_text(self, text: str, alias: str):
        identity, _ = self.identify_by_alias(alias)
        string_identity = identity.get_string_identity(lambda si: si.regex.match(text))
        return identity, string_identity

    def identify_by_alias(self, alias: str) -> Tuple[Identity, StringIdentity]:
        return self.find(lambda i, si: si.alias == alias)

    def find(self, condition: Callable[[Identity, StringIdentity], bool]) -> Tuple[Identity, StringIdentity]:
        for identity in self.identities:
            for string_identity in identity.string_identities:
                if condition(identity, string_identity):
                    return identity, string_identity
        raise UnrecognizableAttribute("No identity and string identity was found.")


DEFAULT_IDENTITY = Identity(
    id_=0,
    string_identities=(
        StringIdentity(0, DEFAULT, re.compile(r"default", re.I)),
        StringIdentity(1, REGULAR, re.compile(r"regular", re.I)),
        StringIdentity(2, NONE, re.compile("none", re.I)),
        StringIdentity(3, NORMAL, re.compile("normal"))
    )
)


COLORS = Identities(
    (
        DEFAULT_IDENTITY,
        Identity(
            id_=1,
            string_identities=(
                StringIdentity(0, BLACK, re.compile(r"black", re.I)),
            )
        ),
        Identity(
            id_=2,
            string_identities=(
                StringIdentity(0, BURNT_SIENNA, re.compile(r"burnt[_\- ]?sienna", re.I)),
                StringIdentity(1, SIENNA, re.compile(r"sienna", re.I)),
                StringIdentity(2, BS, re.compile(r"bs", re.I))
            )
        ),
        Identity(
            id_=3,
            string_identities=(
                StringIdentity(0, COBALT, re.compile(r"cobalt", re.I)),
                StringIdentity(1, BLUE, re.compile(r"blue"))
            )
        ),
        Identity(
            id_=4,
            string_identities=(
                StringIdentity(0, CRIMSON, re.compile(r"crimson", re.I)),
                StringIdentity(1, RED, re.compile(r"red", re.I)),
                StringIdentity(2, CARMESIM, re.compile(r"carmesim", re.I))
            )
        ),
        Identity(
            id_=5,
            string_identities=(
                StringIdentity(0, FOREST_GREEN, re.compile(r"forest[_\- ]?green", re.I)),
                StringIdentity(1, GREEN, re.compile(r"green", re.I)),
                StringIdentity(2, FG, re.compile(r"fg", re.I))
            )
        ),
        Identity(
            id_=6,
            string_identities=(
                StringIdentity(0, GREY, re.compile(r"grey", re.I)),
            )
        ),
        Identity(
            id_=7,
            string_identities=(
                StringIdentity(0, LIME, re.compile(r"lime", re.I)),
            )
        ),
        Identity(
            id_=8,
            string_identities=(
                StringIdentity(0, ORANGE, re.compile(r"orange", re.I)),
            )
        ),
        Identity(
            id_=9,
            string_identities=(
                StringIdentity(0, PINK, re.compile(r"pink", re.I)),
            )
        ),
        Identity(
            id_=10,
            string_identities=(
                StringIdentity(0, PURPLE, re.compile(r"purple", re.I)),
            )
        ),
        Identity(
            id_=11,
            string_identities=(
                StringIdentity(0, SAFFRON, re.compile(r"saffron", re.I)),
                StringIdentity(1, YELLOW, re.compile(r"yellow", re.I))
            )
        ),
        Identity(
            id_=12,
            string_identities=(
                StringIdentity(0, SKY_BLUE, re.compile(r"sky[_\- ]?blue", re.I)),
                StringIdentity(1, SB, re.compile(r"sb"))
            )
        ),
        Identity(
            id_=13,
            string_identities=(
                StringIdentity(0, TITANIUM_WHITE, re.compile(r"titanium[_\- ]?white", re.I)),
                StringIdentity(1, WHITE, re.compile(r"white", re.I)),
                StringIdentity(2, TW, re.compile(r"tw", re.I))
            )
        )
    )
)

CERTIFIEDS = Identities(
    (
        DEFAULT_IDENTITY,
        Identity(
            id_=1,
            string_identities=(
                StringIdentity(0, ACROBAT, re.compile(r"acrobat", re.I)),
            )
        ),
        Identity(
            id_=2,
            string_identities=(
                StringIdentity(0, AVIATOR, re.compile(r"aviator", re.I)),
            )
        ),
        Identity(
            id_=3,
            string_identities=(
                StringIdentity(0, GOALKEEPER, re.compile(r"goalkeeper", re.I)),
            )
        ),
        Identity(
            id_=4,
            string_identities=(
                StringIdentity(0, GUARDIAN, re.compile(r"guardian", re.I)),
            )
        ),
        Identity(
            id_=5,
            string_identities=(
                StringIdentity(0, JUGGLER, re.compile(r"juggler", re.I)),
            )
        ),
        Identity(
            id_=6,
            string_identities=(
                StringIdentity(0, PARAGON, re.compile(r"paragon", re.I)),
            )
        ),
        Identity(
            id_=7,
            string_identities=(
                StringIdentity(0, PLAYMAKER, re.compile(r"playmaker", re.I)),
            )
        ),
        Identity(
            id_=8,
            string_identities=(
                StringIdentity(0, SCORER, re.compile(r"scorer", re.I)),
            )
        ),
        Identity(
            id_=9,
            string_identities=(
                StringIdentity(0, SHOW_OFF, re.compile(r"show[_\- ]?off", re.I)),
            )
        ),
        Identity(
            id_=10,
            string_identities=(
                StringIdentity(0, SNIPER, re.compile(r"sniper", re.I)),
            )
        ),
        Identity(
            id_=11,
            string_identities=(
                StringIdentity(0, STRIKER, re.compile(r"striker", re.I)),
            )
        ),
        Identity(
            id_=12,
            string_identities=(
                StringIdentity(0, SWEEPER, re.compile(r"sweeper", re.I)),
            )
        ),
        Identity(
            id_=13,
            string_identities=(
                StringIdentity(0, TACTICIAN, re.compile(r"tactician", re.I)),
            )
        ),
        Identity(
            id_=14,
            string_identities=(
                StringIdentity(0, TURTLE, re.compile(r"turtle", re.I)),
            )
        ),
        Identity(
            id_=15,
            string_identities=(
                StringIdentity(0, VICTOR, re.compile(r"victor", re.I)),
            )
        ),
    )
)

PLATFORMS = Identities(
    (
        Identity(
            id_=0,
            string_identities=(
                StringIdentity(0, PC, re.compile(r"pc", re.I)),
                StringIdentity(1, COMPUTER, re.compile(r"computer", re.I)),
                StringIdentity(2, STEAM, re.compile(r"steam", re.I)),
                StringIdentity(3, EPIC_GAMES, re.compile(r"epic[_\- ]?games")),
                StringIdentity(4, EPIC, re.compile(r"epic"))
            )
        ),
        Identity(
            id_=1,
            string_identities=(
                StringIdentity(0, XBOX, re.compile(r"xbox", re.I)),
            )
        ),
        Identity(
            id_=2,
            string_identities=(
                StringIdentity(0, PS4, re.compile(r"ps[_\- ]?4", re.I)),
                StringIdentity(1, PLAY_4, re.compile(r"play[_\- ]?4", re.I)),
                StringIdentity(2, PLAYSTATION_4, re.compile(r"playstation[_\- ]?4", re.I))
            )
        ),
        Identity(
            id_=3,
            string_identities=(
                StringIdentity(0, SWITCH, re.compile(r"switch", re.I)),
            )
        ),
    )
)

SLOTS = Identities(
    (
        Identity(
            id_=0,
            string_identities=(
                StringIdentity(0, ANTENNA, re.compile(r"antennas?", re.I)),
            )
        ),
        Identity(
            id_=1,
            string_identities=(
                StringIdentity(0, AVATAR_BORDER, re.compile(r"avatar[_\- ]?borders?", re.I)),
                StringIdentity(1, BORDER, re.compile(r"borders?", re.I))
            )
        ),
        Identity(
            id_=2,
            string_identities=(
                StringIdentity(0, PLAYER_BANNER, re.compile(r"player[_\- ]?banners?", re.I)),
                StringIdentity(1, BANNER, re.compile(r"banners?", re.I))
            )
        ),
        Identity(
            id_=3,
            string_identities=(
                StringIdentity(0, BLUEPRINTS, re.compile(r"blueprints?", re.I)),
            )
        ),
        Identity(
            id_=4,
            string_identities=(
                StringIdentity(0, ROCKET_BOOST, re.compile(r"rocket[_\- ]boosts?", re.I)),
                StringIdentity(1, BOOST, re.compile(r"boosts?", re.I))
            )
        ),
        Identity(
            id_=5,
            string_identities=(
                StringIdentity(0, BODY, re.compile(r"bod(y|ies)", re.I)),
                StringIdentity(1, CAR, re.compile(r"cars?", re.I))
            )
        ),
        Identity(
            id_=6,
            string_identities=(
                StringIdentity(0, DECAL, re.compile(r"decals?", re.I)),
                StringIdentity(1, ANIMATED_DECAL, re.compile(r"animated?[_\- ]?decals?", re.I))
            )
        ),
        Identity(
            id_=7,
            string_identities=(
                StringIdentity(0, ENGINE_AUDIO, re.compile(r"engine[_\- ]?audio", re.I)),
            )
        ),
        Identity(
            id_=8,
            string_identities=(
                StringIdentity(0, GIFT_PACK, re.compile(r"gift[_\- ]?packs?", re.I)),
            )
        ),
        Identity(
            id_=9,
            string_identities=(
                StringIdentity(0, GOAL_EXPLOSION, re.compile(r"goal[_\- ]?explosions?", re.I)),
            )
        ),
        Identity(
            id_=10,
            string_identities=(
                StringIdentity(0, PAINT_FINISH, re.compile(r"paint[_\- ]?finish(es)?", re.I)),
            )
        ),
        Identity(
            id_=11,
            string_identities=(
                StringIdentity(0, PLAYER_ANTHEM, re.compile(r"player[_\- ]?anthems?", re.I)),
                StringIdentity(1, ANTHEM, re.compile(r"anthems?", re.I))
            )
        ),
        Identity(
            id_=12,
            string_identities=(
                StringIdentity(0, TOPPER, re.compile(r"toppers?", re.I)),
                StringIdentity(1, HAT, re.compile(r"hats?", re.I))
            )
        ),
        Identity(
            id_=13,
            string_identities=(
                StringIdentity(0, PLAYER_TITLE, re.compile(r"player[_\- ]?title", re.I)),
                StringIdentity(1, TITLE, re.compile(r"title", re.I))
            )
        ),
        Identity(
            id_=14,
            string_identities=(
                StringIdentity(0, TRAIL, re.compile(r"trails?", re.I)),
            )
        ),
        Identity(
            id_=15,
            string_identities=(
                StringIdentity(0, WHEEL, re.compile(r"wheels?", re.I)),
            )
        )
    )
)

RARITIES = Identities(
    (
        Identity(
            id_=0,
            string_identities=(
                StringIdentity(0, BLACK_MARKET, re.compile(r"black[_\- ]?market", re.I)),
                StringIdentity(1, BM, re.compile(r"bm", re.I))
            )
        ),
        Identity(
            id_=1,
            string_identities=(
                StringIdentity(0, COMMON, re.compile(r"common", re.I)),
            )
        ),
        Identity(
            id_=2,
            string_identities=(
                StringIdentity(0, EXOTIC, re.compile(r"exotic", re.I)),
            )
        ),
        Identity(
            id_=3,
            string_identities=(
                StringIdentity(0, IMPORT, re.compile(r"import", re.I)),
                StringIdentity(1, IMPORTED, re.compile(r"imported", re.I))
            )
        ),
        Identity(
            id_=4,
            string_identities=(
                StringIdentity(0, LEGACY, re.compile(r"legacy", re.I)),
            )
        ),
        Identity(
            id_=5,
            string_identities=(
                StringIdentity(0, LIMITED, re.compile(r"limited", re.I)),
            )
        ),
        Identity(
            id_=6,
            string_identities=(
                StringIdentity(0, PREMIUM, re.compile(r"premium", re.I)),
            )
        ),
        Identity(
            id_=7,
            string_identities=(
                StringIdentity(0, RARE, re.compile(r"rare", re.I)),
            )
        ),
        Identity(
            id_=8,
            string_identities=(
                StringIdentity(0, UNCOMMON, re.compile(r"uncommon", re.I)),
            )
        ),
        Identity(
            id_=9,
            string_identities=(
                StringIdentity(0, VERY_RARE, re.compile(r"very[_\- ]?rare", re.I)),
                StringIdentity(1, VR, re.compile(r"vr", re.I))
            )
        ),
    )
)


SERIES = Identities(
    (
        Identity(
            id_=0,
            string_identities=(
                StringIdentity(0, ACCELERATOR, re.compile(r"accelerator", re.I)),
            )
        ),
        Identity(
            id_=1,
            string_identities=(
                StringIdentity(0, ACCOLADE_1, re.compile(r"accolade[_\- ]?[1I]", re.I)),
            )
        ),
        Identity(
            id_=2,
            string_identities=(
                StringIdentity(0, ACCOLADE_2, re.compile(r"accolade[_\- ]?(?:2|II)", re.I)),
            )
        ),
        Identity(
            id_=3,
            string_identities=(
                StringIdentity(0, AURIGA, re.compile(r"auriga", re.I)),
            )
        ),
        Identity(
            id_=4,
            string_identities=(
                StringIdentity(0, BEACH_BLAST, re.compile(r"beach[_\- ]?blast", re.I)),
            )
        ),
        Identity(
            id_=5,
            string_identities=(
                StringIdentity(0, BONUS_GIFT, re.compile(r"bonus[_\- ]?gift", re.I)),
            )
        ),
        Identity(
            id_=6,
            string_identities=(
                StringIdentity(0, CHAMPIONS_1, re.compile(r"champions[_\- ]?1", re.I)),
            )
        ),
        Identity(
            id_=7,
            string_identities=(
                StringIdentity(0, CHAMPIONS_2, re.compile(r"champions[_\- ]?2", re.I)),
            )
        ),
        Identity(
            id_=8,
            string_identities=(
                StringIdentity(0, CHAMPIONS_3, re.compile(r"champions[_\- ]?3", re.I)),
            )
        ),
        Identity(
            id_=9,
            string_identities=(
                StringIdentity(0, CHAMPIONS_4, re.compile(r"champions[_\- ]?4", re.I)),
            )
        ),
        Identity(
            id_=10,
            string_identities=(
                StringIdentity(0, ELEVATION, re.compile(r"elevation", re.I)),
            )
        ),
        Identity(
            id_=11,
            string_identities=(
                StringIdentity(0, FEROCITY, re.compile(r"ferocity", re.I)),
            )
        ),
        Identity(
            id_=12,
            string_identities=(
                StringIdentity(0, GOLDEN_EGG_2020, re.compile(r"golden[_\- ]?egg[_\- ]?'?(?:20)?20", re.I)),
            )
        ),
        Identity(
            id_=13,
            string_identities=(
                StringIdentity(0, GOLDEN_EGG_2019, re.compile(r"golden[_\- ]?egg[_\- ]?'?(?:20)?19", re.I)),
            )
        ),
        Identity(
            id_=14,
            string_identities=(
                StringIdentity(0, GOLDEN_EGG_2018, re.compile(r"golden[_\- ]?egg[_\- ]?'?(?:20)?18", re.I)),
            )
        ),
        Identity(
            id_=15,
            string_identities=(
                StringIdentity(0, GOLDEN_GIFT_2020, re.compile(r"golden[_\- ]?gift[_\- ]?'?(?:20)?20", re.I)),
            )
        ),
        Identity(
            id_=16,
            string_identities=(
                StringIdentity(0, GOLDEN_GIFT_2019, re.compile(r"golden[_\- ]?gift[_\- ]?'?(?:20)?19", re.I)),
            )
        ),
        Identity(
            id_=17,
            string_identities=(
                StringIdentity(0, GOLDEN_GIFT_2018, re.compile(r"golden[_\- ]?gift[_\- ]?'?(?:20)?18", re.I)),
            )
        ),
        Identity(
            id_=18,
            string_identities=(
                StringIdentity(0, GOLDEN_LANTERN_2021, re.compile(r"golden[_\- ]?lantern[_\- ]?'?(?:20)?21", re.I)),
            )
        ),
        Identity(
            id_=19,
            string_identities=(
                StringIdentity(0, GOLDEN_LANTERN_2020, re.compile(r"golden[_\- ]?lantern[_\- ]?'?(?:20)?20", re.I)),
            )
        ),
        Identity(
            id_=20,
            string_identities=(
                StringIdentity(0, GOLDEN_LANTERN_2019, re.compile(r"golden[_\- ]?lantern[_\- ]?'?(?:20)?19", re.I)),
            )
        ),
        Identity(
            id_=21,
            string_identities=(
                StringIdentity(0, GOLDEN_PUMPKIN_2020, re.compile(r"golden[_\- ]?pumpkin[_\- ]?'?(?:20)?20", re.I)),
            )
        ),
        Identity(
            id_=22,
            string_identities=(
                StringIdentity(0, GOLDEN_PUMPKIN_2019, re.compile(r"golden[_\- ]?pumpkin[_\- ]?'?(?:20)?19", re.I)),
            )
        ),
        Identity(
            id_=23,
            string_identities=(
                StringIdentity(0, GOLDEN_PUMPKIN_2018, re.compile(r"golden[_\- ]?pumpkin[_\- ]?'?(?:20)?18", re.I)),
            )
        ),
        Identity(
            id_=24,
            string_identities=(
                StringIdentity(0, HAUNTED_HALLOWS, re.compile(r"haunted[_\- ]?hallows", re.I)),
            )
        ),
        Identity(
            id_=25,
            string_identities=(
                StringIdentity(0, IGNITION, re.compile(r"ignition", re.I)),
            )
        ),
        Identity(
            id_=26,
            string_identities=(
                StringIdentity(0, IMPACT, re.compile(r"impact", re.I)),
            )
        ),
        Identity(
            id_=27,
            string_identities=(
                StringIdentity(0, MOMENTUM, re.compile(r"momentum", re.I)),
            )
        ),
        Identity(
            id_=28,
            string_identities=(
                StringIdentity(0, NITRO, re.compile(r"nitro", re.I)),
            )
        ),
        Identity(
            id_=29,
            string_identities=(
                StringIdentity(0, NON_CRATE, re.compile(r"non[_\- ]?crate", re.I)),
                StringIdentity(1, POST_GAME, re.compile(r"post[_\- ]?game", re.I))
            )
        ),
        Identity(
            id_=30,
            string_identities=(
                StringIdentity(0, OVERDRIVE, re.compile(r"overdrive", re.I)),
            )
        ),
        Identity(
            id_=31,
            string_identities=(
                StringIdentity(0, PLAYERS_CHOICE, re.compile(r"player's[_\- ]?choice", re.I)),
            )
        ),
        Identity(
            id_=32,
            string_identities=(
                StringIdentity(0, RLCS_REWARD, re.compile(r"RLCS[_\- ]?reward", re.I)),
            )
        ),
        Identity(
            id_=33,
            string_identities=(
                StringIdentity(0, SEASON_1, re.compile(r"season[_\- ]?[1I]", re.I)),
            )
        ),
        Identity(
            id_=34,
            string_identities=(
                StringIdentity(0, SECRET_SANTA, re.compile(r"secret[_\- ]?santa", re.I)),
            )
        ),
        Identity(
            id_=35,
            string_identities=(
                StringIdentity(0, SPRING_FEVER, re.compile(r"spring[_\- ]?fever", re.I)),
            )
        ),
        Identity(
            id_=36,
            string_identities=(
                StringIdentity(0, TOTALLY_AWESOME, re.compile(r"totally[_\- ]?awesome", re.I)),
            )
        ),
        Identity(
            id_=37,
            string_identities=(
                StringIdentity(0, TRIUMPH, re.compile(r"triumph", re.I)),
            )
        ),
        Identity(
            id_=38,
            string_identities=(
                StringIdentity(0, TURBO, re.compile(r"turbo", re.I)),
            )
        ),
        Identity(
            id_=39,
            string_identities=(
                StringIdentity(0, VELOCITY, re.compile(r"velocity", re.I)),
            )
        ),
        Identity(
            id_=40,
            string_identities=(
                StringIdentity(0, VICTORY, re.compile(r"victory", re.I)),
            )
        ),
        Identity(
            id_=41,
            string_identities=(
                StringIdentity(0, VINDICATOR, re.compile(r"vindicator", re.I)),
            )
        ),
        Identity(
            id_=42,
            string_identities=(
                StringIdentity(0, ZEPHYR, re.compile(r"zephyr", re.I)),
            )
        ),
        Identity(
            id_=43,
            string_identities=(
                StringIdentity(0, WWE_PROMO_CODE, re.compile(r"WWE[_\- ]?promo[_\- ]?code", re.I)),
            )
        ),
    )
)
