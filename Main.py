from drills import drills, drill_price
from rebirth import rebirth_upgrades, rebirth_effects, money_for_next_RP, spend_RP
from save_load import save_game, load_game
from money import money_per_click
from special_ores import rare_ores

# --- Starting values ---
money = 0.0
RP = 0

# Starting bonuses (Auto Start Bonus + Start with drill)
money += 500 * rebirth_upgrades["Auto Start Bonus"][0]
drills[0][4] += rebirth_upgrades["Start with drill"][0]

print("Welcome to Mine Simulator with Rebirth upgrades!")
print("Enter = earn money, 1-10 = buy drills, r=rebirth, u=spend RP, s=save, l=load, q=quit\n")

# --- Game loop ---
while True:
    # Round money display
    if money == int(money):
        g = int(money)
    else:
        g = round(money, 2)

    # Round money per click display
    if money_per_click(drills, rebirth_upgrades) == int(money_per_click(drills, rebirth_upgrades)):
        gpc = int(money_per_click(drills, rebirth_upgrades))
    else:
        gpc = round(money_per_click(drills, rebirth_upgrades), 2)

    # Show status
    print(f"💵 Money: {g}  |  ⛏️  Money per click: {gpc}  |  💶 RP: {RP}")
    print("🔧Drills:")
    for i, drill in enumerate(drills):
        price = drill_price(drill, rebirth_upgrades["Upgrade Discount"][0])
        price_display = int(price)
        amount_display = drill[4]
        print(f"{i+1}) {drill[0]:<15} Amount: {amount_display}  Cost: {price_display}  +{drill[2]}/click")
    print(f"Next RP requires: {int(money_for_next_RP(RP))}\n")

    # Player input
    action = input("Enter=click, 1-10=drill, r=rebirth, u=spend RP, s=save, l=load, q=quit: ").lower()

    # Actions
    if action == "":
        earned = money_per_click(drills, rebirth_upgrades)
        money += earned
        print(f"You earned {round(earned,2)} gold!\n")

        import random
        roll = random.randint(1, 1000)
        for ore in rare_ores:
            if roll in ore[2]:
                print(f"You found {ore[0]}! Value: {ore[1]} gold.\n")
                money += ore[1]
                break

    elif action in ["1","2","3","4","5","6","7","8","9","10"]:
        i = int(action) - 1
        price = drill_price(drills[i], rebirth_upgrades["Upgrade Discount"][0])
        if money >= price:
            money -= price
            drills[i][4] += 1
            drills[i][5] *= drills[i][3]
            print(f"You bought a {drills[i][0]}!\n")
        else:
            print("Not enough money!\n")

    elif action == "r":
        if money >= money_for_next_RP(RP):
            RP += 1
            money = 0.0
            for drill in drills:
                drill[4] = 0
                drill[5] = drill[1]  # reset to base price
            # Apply rebirth bonuses
            money += 500 * rebirth_upgrades["Auto Start Bonus"][0]
            drills[0][4] += rebirth_upgrades["Start with drill"][0]
            # Ore Luck level
            ore_luck_level = rebirth_upgrades["Ore Luck"][0]
            extra_chance = int(ore_luck_level * 5)  # each level = +0.5% chance

            print(f"Rebirth complete! RP={RP}\n")
        else:
            print("Not enough money to rebirth!\n")

    elif action == "u":
        RP, money, drills = spend_RP(RP, money, drills)
        
    elif action == "s":
        save_game(money, RP, rebirth_upgrades, drills)

    elif action == "l":
        money, RP, rebirth_upgrades, drills = load_game(rebirth_upgrades, drills)

    elif action == "q":
        print("Game closed!")
        break

    else:
        print("Invalid choice!\n")
