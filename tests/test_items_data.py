from json import load
import rocket_league_utils as rl_utils

with open("sample-gameflip-data.json", "r") as file:
    json = load(file)

items_json = json["data"]

gameflip_data = []

for data in items_json:
    data_item = rl_utils.DataItem(
        platforms=rl_utils.PLATFORMS if data["platform"] == "all" else data["platform"],
        colors=[e["name"] for e in data.get("colors", [])],
        name=data["name"],
        rarity=data["rarity"],
        slot=data["slot"]
    )
    gameflip_data.append(data_item)
