def money_per_click(drills, rebirth_upgrades):
    total = 1.0  # base per click
    for drill in drills:
        total += drill[2] * drill[4]  # power * amount owned
    total *= 1 + 0.1 * rebirth_upgrades["Mining Efficiency"][0]  # +10% per level
    return total
