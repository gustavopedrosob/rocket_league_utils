from rocket_league_utils.certificates.isandcompare import CertificatesIsAndCompare
from rocket_league_utils.certificates.is_functions import *


def compare_certificates(certify_1: str, certify_2: str) -> bool:
    return CertificatesIsAndCompare.compare_(certify_1, certify_2)


def is_certify(string: str) -> bool:
    return CertificatesIsAndCompare.is_(string)


def get_respective_certified(certified: str) -> str:
    if is_aviator(certified):
        return AVIATOR
    elif is_acrobat(certified):
        return ACROBAT
    elif is_victor(certified):
        return VICTOR
    elif is_striker(certified):
        return STRIKER
    elif is_sniper(certified):
        return SNIPER
    elif is_scorer(certified):
        return SCORER
    elif is_playmaker(certified):
        return PLAYMAKER
    elif is_guardian(certified):
        return GUARDIAN
    elif is_paragon(certified):
        return PARAGON
    elif is_sweeper(certified):
        return SWEEPER
    elif is_turtle(certified):
        return TURTLE
    elif is_tactician(certified):
        return TACTICIAN
    elif is_show_off(certified):
        return SHOW_OFF
    elif is_juggler(certified):
        return JUGGLER
    elif is_goalkeeper(certified):
        return GOALKEEPER


class Certified:
    def __init__(self, certified: str):
        self.certified = certified

    def is_aviator(self) -> bool:
        return is_aviator(self.certified)

    def is_acrobat(self) -> bool:
        return is_acrobat(self.certified)

    def is_victor(self) -> bool:
        return is_victor(self.certified)

    def is_striker(self) -> bool:
        return is_striker(self.certified)

    def is_sniper(self) -> bool:
        return is_sniper(self.certified)

    def is_scorer(self) -> bool:
        return is_scorer(self.certified)

    def is_playmaker(self) -> bool:
        return is_playmaker(self.certified)

    def is_guardian(self) -> bool:
        return is_guardian(self.certified)

    def is_paragon(self) -> bool:
        return is_paragon(self.certified)

    def is_sweeper(self) -> bool:
        return is_sweeper(self.certified)

    def is_turtle(self) -> bool:
        return is_turtle(self.certified)

    def is_tactician(self) -> bool:
        return is_tactician(self.certified)

    def is_show_off(self) -> bool:
        return is_show_off(self.certified)

    def is_juggler(self) -> bool:
        return is_juggler(self.certified)

    def is_goalkeeper(self) -> bool:
        return is_goalkeeper(self.certified)

    def compare_certificates(self, certified: str) -> bool:
        return compare_certificates(self.certified, certified)

    def get_respective_certified(self) -> str:
        return get_respective_certified(self.certified)
