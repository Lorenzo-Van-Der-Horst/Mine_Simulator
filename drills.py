drills = [
    ["Iron Drill", 10, 1, 1.5, 0, 10],
    ["Copper Drill", 50, 5, 1.55, 0, 50],
    ["Silver Drill", 120, 12, 1.6, 0, 120],
    ["Gold Drill", 300, 30, 1.65, 0, 300],
    ["Platinum Drill", 700, 70, 1.7, 0, 700],
    ["Diamond Drill", 1500, 150, 1.75, 0, 1500],
    ["Obsidian Drill", 5000, 500, 1.8, 0, 5000],
    ["Mithril Drill", 12000, 1200, 1.85, 0, 12000],
    ["Adamantite Drill", 30000, 3000, 1.9, 0, 30000],
    ["Obsidian Drill", 42000, 5000, 1.9, 0, 42000]
]

def drill_prijs(drill, upgrade_discount):
    korting = 0.1 * upgrade_discount
    return drill[5] * (1 - korting)
