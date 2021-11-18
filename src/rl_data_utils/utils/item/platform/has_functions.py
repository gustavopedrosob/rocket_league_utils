from rl_data_utils.utils.item.platform.is_functions import is_pc, is_ps4, is_xbox, is_switch


def has_pc(platforms: list[str]) -> bool:
    return any([is_pc(platform) for platform in platforms])


def has_ps4(platforms: list[str]) -> bool:
    return any([is_ps4(platform) for platform in platforms])


def has_xbox(platforms: list[str]) -> bool:
    return any([is_xbox(platform) for platform in platforms])


def has_switch(platforms: list[str]) -> bool:
    return any([is_switch(platform) for platform in platforms])
