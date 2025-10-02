from drills import drills, drill_prijs
from rebirth import rebirth_upgrades, rebirth_effects, geld_voor_volgende_RP, uitgeven_RP
from save_load import save_game, load_game
from money import geld_per_klik
from special_ores import rare_ores

# --- Beginwaarden ---
geld = 0.0
RP = 0

# Startspel bonussen (Auto Start Bonus + Team Boost)
geld += 500 * rebirth_upgrades["Auto Start Bonus"][0]
drills[0][4] += rebirth_upgrades["Team Boost"][0]

print("Welkom bij Mine Simulator met Rebirth-upgrades!")
print("Enter = geld verdienen, 1-5 = drills kopen, r=rebirth, u=RP upgraden, s=save, l=load, q=stop\n")

# --- Game loop ---
while True:
    if geld == int(geld):
        g = int(geld)
    else:
        g = round(geld, 2)
    if geld_per_klik(drills, rebirth_upgrades) == int(geld_per_klik(drills, rebirth_upgrades)):
        gpc = int(geld_per_klik(drills, rebirth_upgrades))
    else:
        gpc = round(geld_per_klik(drills, rebirth_upgrades), 2)

    # status weergeven
    print(f"Geld: {g}  |  Geld per klik: {gpc}  |  RP: {RP}")
    print("Drills:")
    for i, drill in enumerate(drills):
        prijs = drill_prijs(drill, rebirth_upgrades["Upgrade Discount"][0])
        prijs_display = int(prijs)
        aantal_display = drill[4]
        print(f"{i+1}) {drill[0]:<15} Aantal: {aantal_display}  Kost: {prijs_display}  +{drill[2]}/klik")
    print(f"Volgende RP kost: {int(geld_voor_volgende_RP(RP))}\n")

    # user input
    actie = input("Enter=klik, 1-10=drill, r=rebirth, u=RP upgraden, s=save, l=load, q=stop: ").lower()

    # acties
    if actie == "":
        verdiend = geld_per_klik(drills, rebirth_upgrades)
        geld += verdiend
        print(f"Je verdiende {round(verdiend,2)} goud!\n")

        import random
        roll = random.randint(1, 1000)
        for ore in rare_ores:
            if roll in ore[2]:
                print(f"Je vond {ore[0]}! Waarde: {ore[1]} goud.\n")
                geld += ore[1]
            
                break
            

    elif actie in ["1","2","3","4","5","6","7","8","9","10"]:
        i = int(actie) - 1
        prijs = drill_prijs(drills[i], rebirth_upgrades["Upgrade Discount"][0])
        if geld >= prijs:
            geld -= prijs
            drills[i][4] += 1
            drills[i][5] *= drills[i][3]
            print(f"Je kocht een {drills[i][0]}!\n")
        else:
            print("Niet genoeg geld!\n")

    elif actie == "r":
        if geld >= geld_voor_volgende_RP(RP):
            RP += 1
            geld = 0.0
            for drill in drills:
                drill[4] = 0
                drill[5] = drill[1]  # reset naar startprijs
            # Rebirth bonussen toepassen
            geld += 500 * rebirth_upgrades["Auto Start Bonus"][0]
            drills[0][4] += rebirth_upgrades["Team Boost"][0]
            # Ore Luck level
            ore_luck_level = rebirth_upgrades["ore_luck"][0]
            extra_kans = int(ore_luck_level * 5)  # elk level = +0.5% kans

            print(f"Rebirth voltooid! RP={RP}\n")
        else:
            print("Niet genoeg geld om te rebirthen!\n")

    elif actie == "u":
        RP, geld, drills = uitgeven_RP(RP, geld, drills)
        
    elif actie == "s":
        save_game(geld, RP, rebirth_upgrades, drills)

    elif actie == "l":
        geld, RP, rebirth_upgrades, drills = load_game(rebirth_upgrades, drills)

    elif actie == "q":
        print("Game afgesloten!")
        break

    else:
        print("Ongeldige keuze!\n")
