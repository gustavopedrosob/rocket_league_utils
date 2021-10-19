from rocket_league_utils.__others import _regex_found


def is_car(type_: str) -> bool:
    return _regex_found("car|body|bodies", type_)


def is_decal(type_: str) -> bool:
    return "decal" in type_.lower()


def is_paint_finish(type_: str) -> bool:
    return "paint" in type_.lower()


def is_wheel(type_: str) -> bool:
    return "wheel" in type_.lower()


def is_boost(type_: str) -> bool:
    return "boost" in type_.lower()


def is_topper(type_: str) -> bool:
    return _regex_found(r"topper|hat", type_)


def is_antenna(type_: str) -> bool:
    return "antenna" in type_.lower()


def is_goal_explosion(type_: str) -> bool:
    return _regex_found(r"goal[_\- ]?explosion", type_)


def is_trail(type_: str) -> bool:
    return "trail" in type_.lower()


def is_engine_audio(type_: str) -> bool:
    return _regex_found(r"engine[_\- ]?audio", type_)


def is_banner(type_: str) -> bool:
    return "banner" in type_.lower()


def is_avatar_border(type_: str) -> bool:
    return _regex_found(r"avatar[_\- ]?border", type_)


def is_gift_pack(type_: str) -> bool:
    return _regex_found(r"gift[_\- ]?pack", type_)


def is_player_anthem(type_: str) -> bool:
    return _regex_found(r"player[_\- ]?anthem", type_)
