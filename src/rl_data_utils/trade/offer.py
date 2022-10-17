from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject


class Offer(RocketLeagueObject):
    def __init__(self, credits_=None, items=None, author=None):
        self.credits = credits_
        self.items = items
        self.author = author

    def is_only_items(self):
        return not self.credits and self.items

    def is_only_credits(self):
        return self.credits and not self.items

    def is_items_and_credits(self):
        return self.credits and self.items
