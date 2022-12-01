# from json import load
#
# import rl_utils as rl_utils
#
#
# def get_price_database(platform="pc"):
#     with open("sample-items-rl-insider.json", "r") as file:
#         json = load(file)
#
#     database = []
#
#     for item in json:
#         for color, price in item["prices"][platform].items():
#             data_item = rl_utils.BaseItemWithPrice(
#                 name=item["name"],
#                 blueprint=bool(price["b"]),
#                 crafting_cost=price["b"],
#                 price=price["k"],
#                 slot=item["slot"]
#             )
#             database.append(data_item)
#     return database
#
#
# price_database = get_price_database()
#
#
# def test_getting_price():
#     repr_item = rl_utils.ReprItem(name="Zomba", blueprint=False, slot="Wheels")
#     rl_utils.get_price(price_database, repr_item)
