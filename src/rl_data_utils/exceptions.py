class RocketLeagueException(Exception):
    pass


class InvalidAttribute(RocketLeagueException):
    pass


class UnrecognizableAttribute(InvalidAttribute):
    pass


class NameHaveNotCarName(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"Item {name} don't have car name.")


class TradeSizeError(RocketLeagueException):
    def __init__(self) -> None:
        super(TradeSizeError, self).__init__("A trade can't has more than 24 items.")


class InvalidCreditsQuantity(InvalidAttribute):
    def __init__(self) -> None:
        super().__init__("A credit need to be a quantity divisible for 10.")


class NegativeItemAttribute(InvalidAttribute):
    def __init__(self) -> None:
        super().__init__("It can't be lower than zero.")


class InvalidTrade(RocketLeagueException):
    pass
