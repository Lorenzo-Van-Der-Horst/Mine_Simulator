# Rebirth-upgrades: [level, RP kost]
rebirth_upgrades = {
    "Mining Efficiency": [0, 1],   # +10% geld per klik per level
    "Upgrade Discount": [0, 1],    # -10% upgrade kosten per level
    "Team Boost": [0, 2],          # +1 Iron Drill start per level
    "Auto Start Bonus": [0, 3],    # +500 goud bij start per level
    "ore_luck": [0, 5]      # +0.5% kans op zeldzame ertsen per level
}

# Beschrijving van effecten
rebirth_effects = {
    "Mining Efficiency": "+10% geld per klik per level",
    "Upgrade Discount": "-10% upgrade kosten per level",
    "Team Boost": "+1 Iron Drill start per level",
    "Auto Start Bonus": "+500 goud bij start per level",
    "ore_luck": "+0.5% kans op zeldzame ertsen per level"
}

# Basis RP-formule
RP_basis = 10000
RP_factor = 2


def geld_voor_volgende_RP(RP):
    """Bereken hoeveel geld nodig is voor de volgende RP."""
    return RP_basis * (RP_factor ** RP)


def uitgeven_RP(RP, geld, drills):
    """Laat speler RP uitgeven aan upgrades."""
    while True:
        print(f"\nJe hebt {RP} RP om uit te geven!")
        print("Upgrades:")
        for i, key in enumerate(rebirth_upgrades):
            lvl, kost = rebirth_upgrades[key]
            effect = rebirth_effects[key]
            print(f"{i+1}) {key} | Level: {lvl} | Kost: {kost} RP | Effect: {effect}")
        print("0) Terug naar spel")

        keuze = input("Kies een upgrade om RP te spenderen (0-5): ")
        if keuze == "0":
            break
        elif keuze in ["1","2","3","4","5"]:
            i = int(keuze) - 1
            key = list(rebirth_upgrades.keys())[i]
            lvl, kost = rebirth_upgrades[key]
            if RP >= kost:
                RP -= kost
                rebirth_upgrades[key][0] += 1
                print(f"{key} verhoogd naar level {rebirth_upgrades[key][0]}! ({rebirth_effects[key]})\n")
                if key == "Auto Start Bonus":
                    geld += 500
                if key == "Team Boost":
                    drills[0][4] += 1
            else:
                print("Niet genoeg RP!\n")
        else:
            print("Ongeldige keuze!\n")
    return RP, geld, drills
