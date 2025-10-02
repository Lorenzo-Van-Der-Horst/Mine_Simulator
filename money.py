def geld_per_klik(drills, rebirth_upgrades):
    totaal = 1.0  # basis per klik
    for drill in drills:
        totaal += drill[2] * drill[4]
    totaal *= 1 + 0.1 * rebirth_upgrades["Mining Efficiency"][0]
    return totaal
