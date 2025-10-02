# special_ores.py
# Each ore has: [Name, Value, Chance range from 1–1000]

rare_ores = [
    ["Copper Ore", 1, range(1, 401)],          # 40% chance
    ["Silver Ore", 5, range(401, 701)],        # 30% chance
    ["Gold Ore", 20, range(701, 851)],         # 15% chance
    ["Platinum Ore", 100, range(851, 951)],    # 10% chance
    ["Diamond Ore", 500, range(951, 981)],     # 3% chance
    ["Mythril Ore", 2000, range(981, 991)],    # 1% chance
    ["Adamantite Ore", 10000, range(991, 996)], # 0.5% chance
    ["Orichalcum Ore", 50000, range(996, 999)], # 0.3% chance
    ["Titanium Ore", 200000, range(999, 1000)], # 0.1% chance
    ["Uranium Ore", 1000000, range(1000, 1001)] # 0.1% chance
]


