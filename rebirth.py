# Rebirth upgrades: [level, RP cost]
rebirth_upgrades = {
    "Mining Efficiency": [0, 1],   # +10% money per click per level
    "Upgrade Discount": [0, 1],    # -10% upgrade cost per level
    "Start with drill": [0, 2],          # +1 Iron Drill at start per level
    "Auto Start Bonus": [0, 3],    # +500 gold at start per level
    "Ore Luck": [0, 5]             # +0.5% chance for rare ores per level
}

# Description of effects
rebirth_effects = {
    "Mining Efficiency": "+10% money per click per level",
    "Upgrade Discount": "-10% upgrade cost per level",
    "Start with drill": "+1 Iron Drill at start per level",
    "Auto Start Bonus": "+500 gold at start per level",
    "Ore Luck": "+0.5% chance for rare ores per level"
}

# Base RP formula
RP_base = 10000
RP_factor = 2


def money_for_next_RP(RP):
    """Calculate how much money is required for the next RP."""
    return RP_base * (RP_factor ** RP)


def spend_RP(RP, money, drills):
    """Let the player spend RP on upgrades."""
    while True:
        print(f"\nYou have {RP} RP to spend!")
        print("Upgrades:")
        for i, key in enumerate(rebirth_upgrades):
            lvl, cost = rebirth_upgrades[key]
            effect = rebirth_effects[key]
            print(f"{i+1}) {key} | Level: {lvl} | Cost: {cost} RP | Effect: {effect}")
        print("0) Back to game")

        choice = input("Choose an upgrade to spend RP on (0-5): ")
        if choice == "0":
            break
        elif choice in ["1", "2", "3", "4", "5"]:
            i = int(choice) - 1
            key = list(rebirth_upgrades.keys())[i]
            lvl, cost = rebirth_upgrades[key]
            if RP >= cost:
                RP -= cost
                rebirth_upgrades[key][0] += 1
                print(f"{key} increased to level {rebirth_upgrades[key][0]}! ({rebirth_effects[key]})\n")
                if key == "Auto Start Bonus":
                    money += 500
                if key == "Start with drill":
                    drills[0][4] += 1
            else:
                print("Not enough RP!\n")
        else:
            print("Invalid choice!\n")
    return RP, money, drills
