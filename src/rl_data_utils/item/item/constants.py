from typing import Literal

ARCHIVED = 'archived'
BLUEPRINT = 'blueprint'
CERTIFIED = 'certified'
COLOR = 'color'
CRAFTING_COST = 'crafting_cost'
NAME = 'name'
PAINTABLE = 'paintable'
PLATFORM = 'platform'
PRICE = 'price'
QUANTITY = 'quantity'
RARITY = 'rarity'
SERIE = 'serie'
SLOT = 'slot'
TRADABLE = 'tradable'

FULL = [ARCHIVED, BLUEPRINT, CERTIFIED, COLOR, CRAFTING_COST, NAME, PAINTABLE, PLATFORM, PRICE, QUANTITY, RARITY,
        SERIE, SLOT, TRADABLE]
INDENTIFIER = [NAME, RARITY, SLOT, BLUEPRINT, PLATFORM]

AttributeName = Literal['archived', 'blueprint', 'certified', 'color', 'crafting_cost', 'name', 'paintable',
                        'platform', 'price', 'quantity', 'rarity', 'serie', 'slot', 'tradable']
