import pytest

from rl_data_utils.item.attribute.attribute import Certified
from rl_data_utils.item.attribute.constants import AVIATOR, ACROBAT, GOALKEEPER, GUARDIAN, JUGGLER, PARAGON, PLAYMAKER, \
    SCORER, SHOW_OFF, SNIPER
from rl_data_utils.item.attribute_data.constants import CERTIFICATES

inventory_certificates = ["Aviator", "Acrobat", "Victor", "Striker", "Sniper", "Scorer", "Playmaker", "Guardian",
                          "Paragon", "Sweeper", "Turtle", "Tactician", "Show-off", "Juggler", "Goalkeeper"]

pair_equals = [["aviator", "Aviator"], ["acrobat", "Acrobat"], ["victor", "Victor"], ["striker", "Striker"],
               ["sniper", "Sniper"], ["scorer", "Scorer"], ["playmaker", "Playmaker"], ["guardian", "Guardian"],
               ["paragon", "Paragon"], ["sweeper", "Sweeper"], ["turtle", "Turtle"], ["tactician", "Tactician"],
               ["show-off", "Show-off"], ["juggler", "Juggler"], ["goalkeeper", "Goalkeeper"]]


samples = [inventory_certificates, CERTIFICATES]


def test_from_random():
    print(Certified.create_random())


@pytest.mark.parametrize("certified_1,certified_2", pair_equals)
def test_compare_certified(certified_1, certified_2):
    assert Certified(certified_1).compare(Certified(certified_2))


@pytest.mark.parametrize("certified", ["acrobat"])
def test_is_acrobat(certified):
    assert Certified(certified).is_exactly(ACROBAT)


@pytest.mark.parametrize("certified", ["aviator"])
def test_is_aviator(certified):
    assert Certified(certified).is_exactly(AVIATOR)


@pytest.mark.parametrize("certified", ["goalkeeper"])
def test_is_goalkeeper(certified):
    assert Certified(certified).is_exactly(GOALKEEPER)


@pytest.mark.parametrize("certified", ["guardian"])
def test_is_guardian(certified):
    assert Certified(certified).is_exactly(GUARDIAN)


@pytest.mark.parametrize("certified", ["juggler"])
def test_is_juggler(certified):
    assert Certified(certified).is_exactly(JUGGLER)


@pytest.mark.parametrize("certified", ["paragon"])
def test_is_paragon(certified):
    assert Certified(certified).is_exactly(PARAGON)


@pytest.mark.parametrize("certified", ["playmaker"])
def test_is_playmaker(certified):
    assert Certified(certified).is_exactly(PLAYMAKER)


@pytest.mark.parametrize("certified", ["scorer"])
def test_is_scorer(certified):
    assert Certified(certified).is_exactly(SCORER)


@pytest.mark.parametrize("certified", ["show_off"])
def test_is_show_off(certified):
    assert Certified(certified).is_exactly(SHOW_OFF)


@pytest.mark.parametrize("certified", ["sniper"])
def test_is_sniper(certified):
    assert Certified(certified).is_exactly(SNIPER)
