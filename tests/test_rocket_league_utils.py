import pytest
import datetime

from rocket_league_utils import certified_utils, color_utils, platform_utils, rarity_utils, serie_utils, slot_utils
import rocket_league_utils as rl_utils


def test_compare_identity():
    item_1 = rl_utils.Item(archived=True, name="Dingo", slot="Car", color="Titanium White", rarity="Import",
                           certified="Striker", quantity=1, blueprint=False, trade_lock=False, serie="non crate",
                           platform="pc", acquired=datetime.datetime.now())
    item_2 = rl_utils.Item(archived=False, name="Dingo", slot="Car", color="Grey", rarity="Import",
                           certified="Goalkeeper", quantity=5, blueprint=False, trade_lock=False, serie="non crate",
                           platform="pc", acquired=datetime.datetime.now())
    assert item_1.compare_identity(item_2)


inventory_colors = ["Crimson", "Sky Blue", "Pink", "Orange", "Cobalt", "Burnt Sienna", "Titanium White", "Grey",
                    "Saffron", "Lime", "Forest Green", "Black", "Purple"]

insider_colors = ["Default", "Black", "Titanium White", "Grey", "Crimson", "Pink", "Cobalt", "Sky Blue",
                  "Burnt Sienna", "Saffron", "Lime", "Forest Green", "Orange", "Purple"]

insider_rarities = ["Limited", "Uncommon", "Rare", "Very Rare", "Import", "Exotic", "Black Market"]

inventory_rarities = ["Import", "Limited", "Uncommon", "Black market", "Rare", "Very rare", "Exotic"]

inventory_series = ["Accelerator", "Accolade 1", "Accolade II", "Auriga", "Champions 1", "Champions 2", "Champions 3",
                    "Champions 4", "Elevation", "Ferocity", "Golden Egg '18", "Golden Egg '19",
                    "Golden Lantern '19", "Golden Pumpkin '20", "Ignition", "Impact", "Momentum", "Nitro", "Overdrive",
                    "Player's Choice", "Postgame", "RLCS reward", "Season 1", "Secret Santa", "Totally Awesome",
                    "Triumph", "Turbo", "Velocity", "Victory", "Vindicator", "WWE promo code", "Zephyr"]

inventory_slots = ["Engine Audio", "Player Banner", "Body", "Topper", "Goal Explosion", "Wheels",
                   "Player Anthem", "Animated Decal", "Paint Finish", "Decal", "Avatar Border",
                   "Antenna", "Rocket Boost", "Trail"]

insider_slots = ["Wheels", "Cars", "Boosts", "Toppers", "Decals", "Antennas", "Goal Explosions", "Trails",
                 "Paint Finishes", "Banners", "Engine Audios", "Avatar Borders"]


@pytest.mark.parametrize("certified_1,certified_2", [
    ["aviator", "Aviator"], ["acrobat", "Acrobat"], ["victor", "Victor"], ["striker", "Striker"],
    ["sniper", "Sniper"], ["scorer", "Scorer"], ["playmaker", "Playmaker"], ["guardian", "Guardian"],
    ["paragon", "Paragon"], ["sweeper", "Sweeper"], ["turtle", "Turtle"], ["tactician", "Tactician"],
    ["show-off", "Show-off"], ["juggler", "Juggler"], ["goalkeeper", "Goalkeeper"]])
def test_compare_certified(certified_1, certified_2):
    assert certified_utils.compare(certified_1, certified_2)


@pytest.mark.parametrize("certified", ["acrobat"])
def test_is_acrobat(certified):
    assert certified_utils.is_exactly(rl_utils.ACROBAT, certified)


@pytest.mark.parametrize("certified", ["aviator"])
def test_is_aviator(certified):
    assert certified_utils.is_exactly(rl_utils.AVIATOR, certified)


@pytest.mark.parametrize("certified", ["goalkeeper"])
def test_is_goalkeeper(certified):
    assert certified_utils.is_exactly(rl_utils.GOALKEEPER, certified)


@pytest.mark.parametrize("certified", ["guardian"])
def test_is_guardian(certified):
    assert certified_utils.is_exactly(rl_utils.GUARDIAN, certified)


@pytest.mark.parametrize("certified", ["juggler"])
def test_is_juggler(certified):
    assert certified_utils.is_exactly(rl_utils.JUGGLER, certified)


@pytest.mark.parametrize("certified", ["paragon"])
def test_is_paragon(certified):
    assert certified_utils.is_exactly(rl_utils.PARAGON, certified)


@pytest.mark.parametrize("certified", ["playmaker"])
def test_is_playmaker(certified):
    assert certified_utils.is_exactly(rl_utils.PLAYMAKER, certified)


@pytest.mark.parametrize("certified", ["scorer"])
def test_is_scorer(certified):
    assert certified_utils.is_exactly(rl_utils.SCORER, certified)


@pytest.mark.parametrize("certified", ["show_off"])
def test_is_show_off(certified):
    assert certified_utils.is_exactly(rl_utils.SHOW_OFF, certified)


@pytest.mark.parametrize("certified", ["sniper"])
def test_is_sniper(certified):
    assert certified_utils.is_exactly(rl_utils.SNIPER, certified)


@pytest.mark.parametrize("certified_string", ["acrobat"])
def test_contains_acrobat(certified_string):
    assert certified_utils.from_text(certified_string)


@pytest.mark.parametrize("certified_string", ["aviator"])
def test_contains_aviator(certified_string):
    assert certified_utils.from_text(certified_string)


@pytest.mark.parametrize("certified_string", ["goalkeeper"])
def test_contains_goalkeeper(certified_string):
    assert certified_utils.from_text(certified_string)


@pytest.mark.parametrize("certified_string", ["guardian"])
def test_contains_guardian(certified_string):
    assert certified_utils.from_text(certified_string)


@pytest.mark.parametrize("certified_string", ["juggler"])
def test_contains_juggler(certified_string):
    assert certified_utils.from_text(certified_string)


@pytest.mark.parametrize("certified_string", ["paragon"])
def test_contains_paragon(certified_string):
    assert certified_utils.from_text(certified_string)


@pytest.mark.parametrize("certified_string", ["playmaker"])
def test_contains_playmaker(certified_string):
    assert certified_utils.from_text(certified_string)


@pytest.mark.parametrize("certified_string", ["scorer"])
def test_contains_scorer(certified_string):
    assert certified_utils.from_text(certified_string)


@pytest.mark.parametrize("certified_string", ["show_off"])
def test_contains_show_off(certified_string):
    assert certified_utils.from_text(certified_string)


@pytest.mark.parametrize("certified_string", ["sniper"])
def test_contains_sniper(certified_string):
    assert certified_utils.from_text(certified_string)


@pytest.mark.parametrize("certified_string,certified_expected", [["sTRIKEr", rl_utils.STRIKER]])
def test_get_respective(certified_string, certified_expected):
    assert certified_utils.get_repr(certified_string) == certified_expected


@pytest.mark.parametrize("certified_string", ["acrobat"])
def test_get_exactly_respective_acrobat(certified_string):
    assert certified_utils.get_repr(certified_utils.from_text(certified_string)) == rl_utils.ACROBAT


@pytest.mark.parametrize("certified_string", ["aviator"])
def test_get_exactly_respective_aviator(certified_string):
    assert certified_utils.get_repr(certified_utils.from_text(certified_string)) == rl_utils.AVIATOR


@pytest.mark.parametrize("certified_string", ["goalkeeper"])
def test_get_exactly_respective_goalkeeper(certified_string):
    assert certified_utils.get_repr(certified_utils.from_text(certified_string)) == rl_utils.GOALKEEPER


@pytest.mark.parametrize("certified_string", ["guardian"])
def test_get_exactly_respective_guardian(certified_string):
    assert certified_utils.get_repr(certified_utils.from_text(certified_string)) == rl_utils.GUARDIAN


@pytest.mark.parametrize("certified_string", ["juggler"])
def test_get_exactly_respective_juggler(certified_string):
    assert certified_utils.get_repr(certified_utils.from_text(certified_string)) == rl_utils.JUGGLER


@pytest.mark.parametrize("certified_string", ["paragon"])
def test_get_exactly_respective_paragon(certified_string):
    assert certified_utils.get_repr(certified_utils.from_text(certified_string)) == rl_utils.PARAGON


@pytest.mark.parametrize("certified_string", ["playmaker"])
def test_get_exactly_respective_playmaker(certified_string):
    assert certified_utils.get_repr(certified_utils.from_text(certified_string)) == rl_utils.PLAYMAKER


@pytest.mark.parametrize("certified_string", ["scorer"])
def test_get_exactly_respective_scorer(certified_string):
    assert certified_utils.get_repr(certified_utils.from_text(certified_string)) == rl_utils.SCORER


@pytest.mark.parametrize("certified_string", ["show_off"])
def test_get_exactly_respective_show_off(certified_string):
    assert certified_utils.get_repr(certified_utils.from_text(certified_string)) == rl_utils.SHOW_OFF


@pytest.mark.parametrize("certified_string", ["sniper"])
def test_get_exactly_respective_sniper(certified_string):
    assert certified_utils.get_repr(certified_utils.from_text(certified_string)) == rl_utils.SNIPER


@pytest.mark.parametrize("color_1,color_2", [
    ["default", "Default"], ["black", "Black"], ["titanium white", "Titanium White"], ["grey", "Grey"],
    ["crimson", "Crimson"], ["pink", "Pink"], ["cobalt", "Cobalt"], ["sky blue", "Sky Blue"],
    ["burnt sienna", "Burnt Sienna"], ["saffron", "Saffron"], ["lime", "Lime"],
    ["forest green", "Forest Green"], ["orange", "Orange"], ["purple", "Purple"]])
def test_compare_color(color_1, color_2):
    assert color_utils.compare(color_1, color_2)


@pytest.mark.parametrize("color", ["black"])
def test_is_black(color):
    assert color_utils.is_exactly(rl_utils.BLACK, color)


@pytest.mark.parametrize("color", ["burnt sienna", "bs", "sienna"])
def test_is_burnt_sienna(color):
    assert color_utils.is_exactly(rl_utils.BURNT_SIENNA, color)


@pytest.mark.parametrize("color", ["cobalt", "blue"])
def test_is_cobalt(color):
    assert color_utils.is_exactly(rl_utils.COBALT, color)


@pytest.mark.parametrize("color", ["crimson", "red", "carmesim"])
def test_is_crimson(color):
    assert color_utils.is_exactly(rl_utils.CRIMSON, color)


@pytest.mark.parametrize("color", ["default", "regular", "none"])
def test_is_default(color):
    assert color_utils.is_exactly(rl_utils.DEFAULT, color)


@pytest.mark.parametrize("color", ["forest green", "green", "fg"])
def test_is_forest_green(color):
    assert color_utils.is_exactly(rl_utils.FOREST_GREEN, color)


@pytest.mark.parametrize("color", ["grey"])
def test_is_grey(color):
    assert color_utils.is_exactly(rl_utils.GREY, color)


@pytest.mark.parametrize("color", ["lime"])
def test_is_lime(color):
    assert color_utils.is_exactly(rl_utils.LIME, color)


@pytest.mark.parametrize("color", ["orange"])
def test_is_orange(color):
    assert color_utils.is_exactly(rl_utils.ORANGE, color)


@pytest.mark.parametrize("color", ["pink"])
def test_is_pink(color):
    assert color_utils.is_exactly(rl_utils.PINK, color)


@pytest.mark.parametrize("color", ["purple"])
def test_is_purple(color):
    assert color_utils.is_exactly(rl_utils.PURPLE, color)


@pytest.mark.parametrize("color", ["saffron", "yellow"])
def test_is_saffron(color):
    assert color_utils.is_exactly(rl_utils.SAFFRON, color)


@pytest.mark.parametrize("color", ["sky blue", "sb"])
def test_is_sky_blue(color):
    assert color_utils.is_exactly(rl_utils.SKY_BLUE, color)


@pytest.mark.parametrize("color", ["titanium white", "tw"])
def test_is_titanium_white(color):
    assert color_utils.is_exactly(rl_utils.TITANIUM_WHITE, color)


def test_has_black():
    assert color_utils.has(rl_utils.COLORS, rl_utils.BLACK)


def test_has_burnt_sienna():
    assert color_utils.has(rl_utils.COLORS, rl_utils.BURNT_SIENNA)


def test_has_cobalt():
    assert color_utils.has(rl_utils.COLORS, rl_utils.COBALT)


def test_has_crimson():
    assert color_utils.has(rl_utils.COLORS, rl_utils.CRIMSON)


def test_has_default():
    assert color_utils.has(rl_utils.COLORS, rl_utils.DEFAULT)


def test_has_forest_green():
    assert color_utils.has(rl_utils.COLORS, rl_utils.FOREST_GREEN)


def test_has_grey():
    assert color_utils.has(rl_utils.COLORS, rl_utils.GREY)


def test_has_lime():
    assert color_utils.has(rl_utils.COLORS, rl_utils.LIME)


def test_has_orange():
    assert color_utils.has(rl_utils.COLORS, rl_utils.ORANGE)


def test_has_pink():
    assert color_utils.has(rl_utils.COLORS, rl_utils.PINK)


def test_has_purple():
    assert color_utils.has(rl_utils.COLORS, rl_utils.PURPLE)


def test_has_saffron():
    assert color_utils.has(rl_utils.COLORS, rl_utils.SAFFRON)


def test_has_sky_blue():
    assert color_utils.has(rl_utils.COLORS, rl_utils.SKY_BLUE)


def test_has_titanium_white():
    assert color_utils.has(rl_utils.COLORS, rl_utils.TITANIUM_WHITE)


@pytest.mark.parametrize("color", ["black"])
def test_contains_black(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["burnt sienna", "bs", "sienna"])
def test_contains_burnt_sienna(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["cobalt", "blue"])
def test_contains_cobalt(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["crimson", "red", "carmesim"])
def test_contains_crimson(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["default", "regular"])
def test_contains_default(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["forest green", "green", "fg"])
def test_contains_forest_green(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["grey"])
def test_contains_grey(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["lime"])
def test_contains_lime(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["orange"])
def test_contains_orange(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["pink"])
def test_contains_pink(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["purple"])
def test_contains_purple(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["saffron", "yellow"])
def test_contains_saffron(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["sky blue", "sb"])
def test_contains_sky_blue(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", ["titanium white", "tw"])
def test_contains_titanium_white(color):
    assert color_utils.from_text(color)


@pytest.mark.parametrize("color", [*inventory_colors, *insider_colors])
def test_has_color(color):
    assert color_utils.has(rl_utils.COLORS, color)


@pytest.mark.parametrize("color", [*inventory_colors, *insider_colors])
def test_get_respective_color(color):
    result = color_utils.get_repr(color)
    print(result)


def test_compare_name():
    assert rl_utils.compare_names("Wall Breaker II", "Wall Breaker II")


@pytest.mark.parametrize("decal_name, car_name", (("Dragon [Dominus]", "Dominus"), ("Dragon (Octane)", "Octane")))
def test_get_car(decal_name: str, car_name: str):
    assert rl_utils.identify_name(decal_name).complement == car_name


def test_get_kind():
    assert rl_utils.identify_name("Bravado: Infinite").complement == "Infinite"


@pytest.mark.parametrize("platform_1,platform_2",
                         [["pc", "Pc"], ["ps4", "Ps4"], ["xbox", "Xbox"], ["switch", "Switch"]])
def test_compare_platform(platform_1, platform_2):
    assert platform_utils.compare(platform_1, platform_2)


@pytest.mark.parametrize("platform", ["pc", "computer", "steam", "epic games", "epic"])
def test_is_pc(platform):
    assert platform_utils.is_exactly(rl_utils.PC, platform)


@pytest.mark.parametrize("platform", ["ps4", "ps 4", "play 4", "playstation 4"])
def test_is_ps4(platform):
    assert platform_utils.is_exactly(rl_utils.PS4, platform)


@pytest.mark.parametrize("platform", ["xbox"])
def test_is_xbox(platform):
    assert platform_utils.is_exactly(rl_utils.XBOX, platform)


@pytest.mark.parametrize("platform", ["switch"])
def test_is_switch(platform):
    assert platform_utils.is_exactly(rl_utils.SWITCH, platform)


@pytest.mark.parametrize("platform", ["pc"])
def test_contains_pc(platform):
    assert platform_utils.from_text(platform)


@pytest.mark.parametrize("platform", ["ps4", "ps 4", "play 4", "playstation 4"])
def test_contains_ps4(platform):
    assert platform_utils.from_text(platform)


@pytest.mark.parametrize("platform", ["xbox"])
def test_contains_xbox(platform):
    assert platform_utils.from_text(platform)


@pytest.mark.parametrize("platform", ["switch"])
def test_contains_switch(platform):
    assert platform_utils.from_text(platform)


def test_raises_credits_lower_than_zero():
    with pytest.raises(rl_utils.InvalidCredits):
        rl_utils.validate_credits(-1)


def test_raises_invalid_credits_quantity():
    with pytest.raises(rl_utils.InvalidCredits):
        rl_utils.validate_credits(5)


@pytest.mark.parametrize("platforms_", [rl_utils.PLATFORMS])
def test_has_pc(platforms_):
    assert platform_utils.has(platforms_, rl_utils.PC)


@pytest.mark.parametrize("platforms_", [rl_utils.PLATFORMS])
def test_has_ps4(platforms_):
    assert platform_utils.has(platforms_, rl_utils.PS4)


@pytest.mark.parametrize("platforms_", [rl_utils.PLATFORMS])
def test_has_xbox(platforms_):
    assert platform_utils.has(platforms_, rl_utils.XBOX)


@pytest.mark.parametrize("platforms_", [rl_utils.PLATFORMS])
def test_has_switch(platforms_):
    assert platform_utils.has(platforms_, rl_utils.SWITCH)


@pytest.mark.parametrize("rarity_1,rarity_2", [
    ["black market", "Black market"], ["common", "Common"], ["exotic", "Exotic"], ["import", "Import"],
    ["limited", "Limited"], ["premium", "Premium"], ["rare", "Rare"], ["uncommon", "Uncommon"],
    ["very rare", "Very rare"], ["legacy", "Legacy"]])
def test_compare_rarity(rarity_1, rarity_2):
    assert rarity_utils.compare(rarity_1, rarity_2)


@pytest.mark.parametrize("rarity", ["bm", "black market"])
def test_is_black_market(rarity):
    assert rarity_utils.is_exactly(rl_utils.BLACK_MARKET, rarity)


@pytest.mark.parametrize("rarity", ["common"])
def test_is_common(rarity):
    assert rarity_utils.is_exactly(rl_utils.COMMON, rarity)


@pytest.mark.parametrize("rarity", ["exotic"])
def test_is_exotic(rarity):
    assert rarity_utils.is_exactly(rl_utils.EXOTIC, rarity)


@pytest.mark.parametrize("rarity", ["import"])
def test_is_import(rarity):
    assert rarity_utils.is_exactly(rl_utils.IMPORT, rarity)


@pytest.mark.parametrize("rarity", ["legacy"])
def test_is_legacy(rarity):
    assert rarity_utils.is_exactly(rl_utils.LEGACY, rarity)


@pytest.mark.parametrize("rarity", ["limited"])
def test_is_limited(rarity):
    assert rarity_utils.is_exactly(rl_utils.LIMITED, rarity)


@pytest.mark.parametrize("rarity", ["premium"])
def test_is_premium(rarity):
    assert rarity_utils.is_exactly(rl_utils.PREMIUM, rarity)


@pytest.mark.parametrize("rarity", ["rare"])
def test_is_rare(rarity):
    assert rarity_utils.is_exactly(rl_utils.RARE, rarity)


@pytest.mark.parametrize("rarity", ["uncommon"])
def test_is_uncommon(rarity):
    assert rarity_utils.is_exactly(rl_utils.UNCOMMON, rarity)


@pytest.mark.parametrize("rarity", ["very rare", "vr"])
def test_is_very_rare(rarity):
    assert rarity_utils.is_exactly(rl_utils.VERY_RARE, rarity)


@pytest.mark.parametrize("rarity", ["bm", "black market"])
def test_contains_black_market(rarity):
    assert rarity_utils.from_text(rarity)


@pytest.mark.parametrize("rarity", ["common"])
def test_contains_common(rarity):
    assert rarity_utils.from_text(rarity)


@pytest.mark.parametrize("rarity", ["exotic"])
def test_contains_exotic(rarity):
    assert rarity_utils.from_text(rarity)


@pytest.mark.parametrize("rarity", ["import", "imported"])
def test_contains_import(rarity):
    assert rarity_utils.from_text(rarity)


@pytest.mark.parametrize("rarity", ["legacy"])
def test_contains_legacy(rarity):
    assert rarity_utils.from_text(rarity)


@pytest.mark.parametrize("rarity", ["limited"])
def test_contains_limited(rarity):
    assert rarity_utils.from_text(rarity)


@pytest.mark.parametrize("rarity", ["premium"])
def test_contains_premium(rarity):
    assert rarity_utils.from_text(rarity)


@pytest.mark.parametrize("rarity", ["rare"])
def test_contains_rare(rarity):
    assert rarity_utils.from_text(rarity)


@pytest.mark.parametrize("rarity", ["uncommon"])
def test_contains_uncommon(rarity):
    assert rarity_utils.from_text(rarity)


@pytest.mark.parametrize("rarity", ["very rare", "vr"])
def test_contains_very_rare(rarity):
    assert rarity_utils.from_text(rarity)


@pytest.mark.parametrize("rarity", [*inventory_rarities, *insider_rarities])
def test_has_rarity(rarity):
    assert rarity_utils.has(rl_utils.RARITIES, rarity)


@pytest.mark.parametrize("rarities_", [rl_utils.RARITIES])
def test_has_black_market(rarities_):
    assert rarity_utils.has(rarities_, rl_utils.BLACK_MARKET)


@pytest.mark.parametrize("rarities_", [rl_utils.RARITIES])
def test_has_common(rarities_):
    assert rarity_utils.has(rarities_, rl_utils.COMMON)


@pytest.mark.parametrize("rarities_", [rl_utils.RARITIES])
def test_has_exotic(rarities_):
    assert rarity_utils.has(rarities_, rl_utils.EXOTIC)


@pytest.mark.parametrize("rarities_", [rl_utils.RARITIES])
def test_has_import(rarities_):
    assert rarity_utils.has(rarities_, rl_utils.IMPORT)


@pytest.mark.parametrize("rarities_", [rl_utils.RARITIES])
def test_has_legacy(rarities_):
    assert rarity_utils.has(rarities_, rl_utils.LEGACY)


@pytest.mark.parametrize("rarities_", [rl_utils.RARITIES])
def test_has_limited(rarities_):
    assert rarity_utils.has(rarities_, rl_utils.LIMITED)


@pytest.mark.parametrize("rarities_", [rl_utils.RARITIES])
def test_has_premium(rarities_):
    assert rarity_utils.has(rarities_, rl_utils.PREMIUM)


@pytest.mark.parametrize("rarities_", [rl_utils.RARITIES])
def test_has_rare(rarities_):
    assert rarity_utils.has(rarities_, rl_utils.RARE)


@pytest.mark.parametrize("rarities_", [rl_utils.RARITIES])
def test_has_uncommon(rarities_):
    assert rarity_utils.has(rarities_, rl_utils.UNCOMMON)


@pytest.mark.parametrize("rarities_", [rl_utils.RARITIES])
def test_has_very_rare(rarities_):
    assert rarity_utils.has(rarities_, rl_utils.VERY_RARE)


@pytest.mark.parametrize("serie", ["Accelerator"])
def test_is_accelerator_series(serie):
    assert serie_utils.is_exactly(rl_utils.ACCELERATOR, serie)


@pytest.mark.parametrize("serie", ["Accolade 1"])
def test_is_accolade_1_series(serie):
    assert serie_utils.is_exactly(rl_utils.ACCOLADE_1, serie)


@pytest.mark.parametrize("serie", ["Accolade 2"])
def test_is_accolade_2_series(serie):
    assert serie_utils.is_exactly(rl_utils.ACCOLADE_2, serie)


@pytest.mark.parametrize("serie", ["Auriga"])
def test_is_auriga_series(serie):
    assert serie_utils.is_exactly(rl_utils.AURIGA, serie)


@pytest.mark.parametrize("serie", ["Beach Blast"])
def test_is_beach_blast_series(serie):
    assert serie_utils.is_exactly(rl_utils.BEACH_BLAST, serie)


@pytest.mark.parametrize("serie", ["Bonus Gift"])
def test_is_bonus_gift(serie):
    assert serie_utils.is_exactly(rl_utils.BONUS_GIFT, serie)


@pytest.mark.parametrize("serie", ["Champions 1"])
def test_is_champions_1_series(serie):
    assert serie_utils.is_exactly(rl_utils.CHAMPIONS_1, serie)


@pytest.mark.parametrize("serie", ["Champions 2"])
def test_is_champions_2_series(serie):
    assert serie_utils.is_exactly(rl_utils.CHAMPIONS_2, serie)


@pytest.mark.parametrize("serie", ["Champions 3"])
def test_is_champions_3_series(serie):
    assert serie_utils.is_exactly(rl_utils.CHAMPIONS_3, serie)


@pytest.mark.parametrize("serie", ["Champions 4"])
def test_is_champions_4_series(serie):
    assert serie_utils.is_exactly(rl_utils.CHAMPIONS_4, serie)


@pytest.mark.parametrize("serie", ["Dorado", "Dorado Series"])
def test_is_dorado_series(serie):
    assert serie_utils.is_exactly(rl_utils.DORADO, serie)


@pytest.mark.parametrize("serie", ["Elevation"])
def test_is_elevation_series(serie):
    assert serie_utils.is_exactly(rl_utils.ELEVATION, serie)


@pytest.mark.parametrize("serie", ["Ferocity"])
def test_is_ferocity_series(serie):
    assert serie_utils.is_exactly(rl_utils.FEROCITY, serie)


@pytest.mark.parametrize("serie", ["Fornax", "Fornax Series"])
def test_is_fornax_series(serie):
    assert serie_utils.is_exactly(rl_utils.FORNAX, serie)


@pytest.mark.parametrize("serie", ["Golden Egg '18"])
def test_is_golden_egg_2018(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_EGG_2018, serie)


@pytest.mark.parametrize("serie", ["Golden Egg '19"])
def test_is_golden_egg_2019(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_EGG_2019, serie)


@pytest.mark.parametrize("serie", ["Golden Egg '20"])
def test_is_golden_egg_2020(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_EGG_2020, serie)


@pytest.mark.parametrize("serie", ["Golden Egg '22"])
def test_is_golden_egg_2022(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_EGG_2022, serie)


@pytest.mark.parametrize("serie", ["Golden Gift '18"])
def test_is_golden_gift_2018(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_GIFT_2018, serie)


@pytest.mark.parametrize("serie", ["Golden Gift '19"])
def test_is_golden_gift_2019(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_GIFT_2019, serie)


@pytest.mark.parametrize("serie", ["Golden Gift '20"])
def test_is_golden_gift_2020(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_GIFT_2020, serie)


@pytest.mark.parametrize("serie", ["Golden Gift '21"])
def test_is_golden_gift_2021(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_GIFT_2021, serie)


@pytest.mark.parametrize("serie", ["Golden Gift Basket '22"])
def test_is_golden_gift_basket_2022(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_GIFT_BASKET_2022, serie)


@pytest.mark.parametrize("serie", ["Golden Lantern '19"])
def test_is_golden_lantern_2019(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_LANTERN_2019, serie)


@pytest.mark.parametrize("serie", ["Golden Lantern '20"])
def test_is_golden_lantern_2020(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_LANTERN_2020, serie)


@pytest.mark.parametrize("serie", ["Golden Lantern '21"])
def test_is_golden_lantern_2021(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_LANTERN_2021, serie)


@pytest.mark.parametrize("serie", ["Golden Moon"])
def test_is_golden_moon(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_MOON, serie)


@pytest.mark.parametrize("serie", ["Golden Pumpkin '18"])
def test_is_golden_pumpkin_2018(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_PUMPKIN_2018, serie)


@pytest.mark.parametrize("serie", ["Golden Pumpkin '19"])
def test_is_golden_pumpkin_2019(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_PUMPKIN_2019, serie)


@pytest.mark.parametrize("serie", ["Golden Pumpkin '20"])
def test_is_golden_pumpkin_2020(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_PUMPKIN_2020, serie)


@pytest.mark.parametrize("serie", ["Golden Pumpkin '22"])
def test_is_golden_pumpkin_2022(serie):
    assert serie_utils.is_exactly(rl_utils.GOLDEN_PUMPKIN_2022, serie)


@pytest.mark.parametrize("serie", ["Haunted Hallows"])
def test_is_haunted_hallows_series(serie):
    assert serie_utils.is_exactly(rl_utils.HAUNTED_HALLOWS, serie)


@pytest.mark.parametrize("serie", ["Ignition"])
def test_is_ignition_series(serie):
    assert serie_utils.is_exactly(rl_utils.IGNITION, serie)


@pytest.mark.parametrize("serie", ["Impact"])
def test_is_impact_series(serie):
    assert serie_utils.is_exactly(rl_utils.IMPACT, serie)


@pytest.mark.parametrize("serie", ["Momentum"])
def test_is_momentum_series(serie):
    assert serie_utils.is_exactly(rl_utils.MOMENTUM, serie)


@pytest.mark.parametrize("serie", ["Nitro"])
def test_is_nitro_series(serie):
    assert serie_utils.is_exactly(rl_utils.NITRO, serie)


@pytest.mark.parametrize("serie", ["Non Crate"])
def test_is_non_crate(serie):
    assert serie_utils.is_exactly(rl_utils.NON_CRATE, serie)


@pytest.mark.parametrize("serie", ["Overdrive"])
def test_is_overdrive_series(serie):
    assert serie_utils.is_exactly(rl_utils.OVERDRIVE, serie)


@pytest.mark.parametrize("serie", ["Player's Choice"])
def test_is_players_choice_series(serie):
    assert serie_utils.is_exactly(rl_utils.PLAYERS_CHOICE, serie)


@pytest.mark.parametrize("serie", ["RLCS Reward"])
def test_is_rlcs_reward_series(serie):
    assert serie_utils.is_exactly(rl_utils.RLCS_REWARD, serie)


@pytest.mark.parametrize("serie", ["Revival", "Revival Series"])
def test_is_revival_series(serie):
    assert serie_utils.is_exactly(rl_utils.REVIVAL, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 1"])
def test_is_rocketpass_1(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_1, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 2"])
def test_is_rocketpass_2(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_2, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 3"])
def test_is_rocketpass_3(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_3, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 4"])
def test_is_rocketpass_4(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_4, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 5"])
def test_is_rocketpass_5(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_5, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 6"])
def test_is_rocketpass_6(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_6, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 7"])
def test_is_rocketpass_7(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_7, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 8"])
def test_is_rocketpass_8(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_8, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 9"])
def test_is_rocketpass_9(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_9, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 10"])
def test_is_rocketpass_10(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_10, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 11"])
def test_is_rocketpass_11(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_11, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 12"])
def test_is_rocketpass_12(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_12, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 13"])
def test_is_rocketpass_13(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_13, serie)


@pytest.mark.parametrize("serie", ["Rocketpass 14"])
def test_is_rocketpass_14(serie):
    assert serie_utils.is_exactly(rl_utils.ROCKETPASS_14, serie)


@pytest.mark.parametrize("serie", ["Select Favorites Item", "Select Favorites Item Series"])
def test_is_select_favorites_item(serie):
    assert serie_utils.is_exactly(rl_utils.SELECT_FAVORITES_ITEM, serie)


@pytest.mark.parametrize("serie", ["Select Favorites 2", "Select Favorites Series 2"])
def test_is_select_favorites_2(serie):
    assert serie_utils.is_exactly(rl_utils.SELECT_FAVORITES_2, serie)


@pytest.mark.parametrize("serie", ["Season 1"])
def test_is_season_1(serie):
    assert serie_utils.is_exactly(rl_utils.SEASON_1, serie)


@pytest.mark.parametrize("serie", ["Season 2"])
def test_is_season_2(serie):
    assert serie_utils.is_exactly(rl_utils.SEASON_2, serie)


@pytest.mark.parametrize("serie", ["Secret Santa"])
def test_is_secret_santa_series(serie):
    assert serie_utils.is_exactly(rl_utils.SECRET_SANTA, serie)


@pytest.mark.parametrize("serie", ["Spring Fever"])
def test_is_spring_fever_series(serie):
    assert serie_utils.is_exactly(rl_utils.SPRING_FEVER, serie)


@pytest.mark.parametrize("serie", ["Totally Awesome"])
def test_is_totally_awesome_series(serie):
    assert serie_utils.is_exactly(rl_utils.TOTALLY_AWESOME, serie)


@pytest.mark.parametrize("serie", ["Triumph"])
def test_is_triumph_series(serie):
    assert serie_utils.is_exactly(rl_utils.TRIUMPH, serie)


@pytest.mark.parametrize("serie", ["Turbo"])
def test_is_turbo_series(serie):
    assert serie_utils.is_exactly(rl_utils.TURBO, serie)


@pytest.mark.parametrize("serie", ["Velocity"])
def test_is_velocity_series(serie):
    assert serie_utils.is_exactly(rl_utils.VELOCITY, serie)


@pytest.mark.parametrize("serie", ["Victory"])
def test_is_victory_series(serie):
    assert serie_utils.is_exactly(rl_utils.VICTORY, serie)


@pytest.mark.parametrize("serie", ["Vindicator"])
def test_is_vindicator_series(serie):
    assert serie_utils.is_exactly(rl_utils.VINDICATOR, serie)


@pytest.mark.parametrize("serie", ["Zephyr"])
def test_is_zephyr_series(serie):
    assert serie_utils.is_exactly(rl_utils.ZEPHYR, serie)


@pytest.mark.parametrize("serie", ["WWE Promo Code"])
def test_is_wwe_promo_code(serie):
    assert serie_utils.is_exactly(rl_utils.WWE_PROMO_CODE, serie)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_accelerator_series(series_):
    assert serie_utils.has(series_, rl_utils.ACCELERATOR)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_accolade_1_series(series_):
    assert serie_utils.has(series_, rl_utils.ACCOLADE_1)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_accolade_2_series(series_):
    assert serie_utils.has(series_, rl_utils.ACCOLADE_2)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_auriga_series(series_):
    assert serie_utils.has(series_, rl_utils.AURIGA)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_beach_blast_series(series_):
    assert serie_utils.has(series_, rl_utils.BEACH_BLAST)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_bonus_gift(series_):
    assert serie_utils.has(series_, rl_utils.BONUS_GIFT)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_champions_1_series(series_):
    assert serie_utils.has(series_, rl_utils.CHAMPIONS_1)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_champions_2_series(series_):
    assert serie_utils.has(series_, rl_utils.CHAMPIONS_2)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_champions_3_series(series_):
    assert serie_utils.has(series_, rl_utils.CHAMPIONS_3)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_champions_4_series(series_):
    assert serie_utils.has(series_, rl_utils.CHAMPIONS_4)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_elevation_series(series_):
    assert serie_utils.has(series_, rl_utils.ELEVATION)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_ferocity_series(series_):
    assert serie_utils.has(series_, rl_utils.FEROCITY)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_egg_2018(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_EGG_2018)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_egg_2019(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_EGG_2019)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_egg_2020(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_EGG_2020)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_gift_2018(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_GIFT_2018)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_gift_2019(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_GIFT_2019)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_gift_2020(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_GIFT_2020)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_lantern_2019(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_LANTERN_2019)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_lantern_2020(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_LANTERN_2020)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_lantern_2021(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_LANTERN_2021)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_pumpkin_2018(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_PUMPKIN_2018)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_pumpkin_2019(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_PUMPKIN_2019)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_golden_pumpkin_2020(series_):
    assert serie_utils.has(series_, rl_utils.GOLDEN_PUMPKIN_2020)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_haunted_hallows_series(series_):
    assert serie_utils.has(series_, rl_utils.HAUNTED_HALLOWS)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_ignition_series(series_):
    assert serie_utils.has(series_, rl_utils.IGNITION)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_impact_series(series_):
    assert serie_utils.has(series_, rl_utils.IMPACT)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_momentum_series(series_):
    assert serie_utils.has(series_, rl_utils.MOMENTUM)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_nitro_series(series_):
    assert serie_utils.has(series_, rl_utils.NITRO)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_non_crate(series_):
    assert serie_utils.has(series_, rl_utils.NON_CRATE)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_overdrive_series(series_):
    assert serie_utils.has(series_, rl_utils.OVERDRIVE)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_players_choice_series(series_):
    assert serie_utils.has(series_, rl_utils.PLAYERS_CHOICE)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_rlcs_reward(series_):
    assert serie_utils.has(series_, rl_utils.RLCS_REWARD)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_season_1(series_):
    assert serie_utils.has(series_, rl_utils.SEASON_1)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_secret_santa_series(series_):
    assert serie_utils.has(series_, rl_utils.SECRET_SANTA)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_spring_fever_series(series_):
    assert serie_utils.has(series_, rl_utils.SPRING_FEVER)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_totally_awesome_series(series_):
    assert serie_utils.has(series_, rl_utils.TOTALLY_AWESOME)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_triumph_series(series_):
    assert serie_utils.has(series_, rl_utils.TRIUMPH)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_turbo_series(series_):
    assert serie_utils.has(series_, rl_utils.TURBO)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_velocity_series(series_):
    assert serie_utils.has(series_, rl_utils.VELOCITY)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_victory_series(series_):
    assert serie_utils.has(series_, rl_utils.VICTORY)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_vindicator_series(series_):
    assert serie_utils.has(series_, rl_utils.VINDICATOR)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_zephyr_series(series_):
    assert serie_utils.has(series_, rl_utils.ZEPHYR)


@pytest.mark.parametrize("series_", [rl_utils.SERIES])
def test_has_wwe_promo_code(series_):
    assert serie_utils.has(series_, rl_utils.WWE_PROMO_CODE)


@pytest.mark.parametrize("serie", [*inventory_series])
def test_has_serie(serie):
    assert serie_utils.has(rl_utils.SERIES, serie)


@pytest.mark.parametrize("slot_1,slot_2", [
    ["antennas", "Antennas"], ["avatar borders", "Avatar Borders"], ["body", "Body"],
    ["decals", "Decals"], ["engine audio", "Engine Audio"], ["goal explosions", "Goal Explosions"],
    ["paint finishes", "Paint Finishes"], ["player anthems", "Player Anthems"],
    ["player banners", "Player Banners"], ["rocket boosts", "Rocket Boosts"], ["toppers", "Toppers"],
    ["trails", "Trails"], ["wheels", "Wheels"]])
def test_compare_slot(slot_1, slot_2):
    assert slot_utils.compare(slot_1, slot_2)


@pytest.mark.parametrize("slot", ["Anthem"])
def test_is_anthem(slot):
    assert slot_utils.is_exactly(rl_utils.ANTHEM, slot)


@pytest.mark.parametrize("slot", ["Antenna"])
def test_is_antenna(slot):
    assert slot_utils.is_exactly(rl_utils.ANTENNA, slot)


@pytest.mark.parametrize("slot", ["Avatar Border"])
def test_is_avatar_border(slot):
    assert slot_utils.is_exactly(rl_utils.BORDER, slot)


@pytest.mark.parametrize("slot", ["Banner"])
def test_is_banner(slot):
    assert slot_utils.is_exactly(rl_utils.BANNER, slot)


@pytest.mark.parametrize("slot", ["Boost"])
def test_is_boost(slot):
    assert slot_utils.is_exactly(rl_utils.BOOST, slot)


@pytest.mark.parametrize("slot", ["Car"])
def test_is_car(slot):
    assert slot_utils.is_exactly(rl_utils.CAR, slot)


@pytest.mark.parametrize("slot", ["Decal"])
def test_is_decal(slot):
    assert slot_utils.is_exactly(rl_utils.DECAL, slot)


@pytest.mark.parametrize("slot", ["Engine Audio"])
def test_is_engine_audio(slot):
    assert slot_utils.is_exactly(rl_utils.ENGINE_AUDIO, slot)


@pytest.mark.parametrize("slot", ["Goal Explosion"])
def test_is_goal_explosion(slot):
    assert slot_utils.is_exactly(rl_utils.GOAL_EXPLOSION, slot)


@pytest.mark.parametrize("slot", ["Paint Finish"])
def test_is_paint_finish(slot):
    assert slot_utils.is_exactly(rl_utils.PAINT_FINISH, slot)


@pytest.mark.parametrize("slot", ["Topper"])
def test_is_topper(slot):
    assert slot_utils.is_exactly(rl_utils.TOPPER, slot)


@pytest.mark.parametrize("slot", ["Trail"])
def test_is_trail(slot):
    assert slot_utils.is_exactly(rl_utils.TRAIL, slot)


@pytest.mark.parametrize("slot", ["Wheels"])
def test_is_wheel(slot):
    assert slot_utils.is_exactly(rl_utils.WHEEL, slot)


@pytest.mark.parametrize("slot", ["Antenna"])
def test_contains_antenna(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Avatar Border"])
def test_contains_border(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Banner"])
def test_contains_banner(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Boost"])
def test_contains_boost(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Car"])
def test_contains_car(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Decal"])
def test_contains_decal(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Engine Audio"])
def test_contains_engine_audio(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Gift Pack"])
def test_contains_gift_pack(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Goal Explosion"])
def test_contains_goal_explosion(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Paint Finish"])
def test_contains_paint_finish(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Anthem"])
def test_contains_anthem(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Topper"])
def test_contains_topper(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Trail"])
def test_contains_trail(slot):
    assert slot_utils.from_text(slot)


@pytest.mark.parametrize("slot", ["Wheels"])
def test_contains_wheel(slot):
    assert slot_utils.from_text(slot)
