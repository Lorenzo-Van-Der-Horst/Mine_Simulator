#Mine Simulator
#by: Lorenzo van der Horst en Nick Pauel
#Date: 2025-09-30
#Version: 1.0

# --- Beginwaarden ---
geld = 0.0
basis_per_klik = 1.0
RP = 0

# Drills: naam, startprijs, productie per klik, prijsfactor, aantal, huidige prijs
drills = [
    ["Iron Drill", 10, 1, 1.5, 0, 10],
    ["Copper Drill", 50, 5, 1.55, 0, 50],
    ["Silver Drill", 120, 12, 1.6, 0, 120],
    ["Gold Drill", 300, 30, 1.65, 0, 300],
    ["Platinum Drill", 700, 70, 1.7, 0, 700],
]

# Rebirth-upgrades: [level, RP kost]
rebirth_upgrades = {
    "Mining Efficiency": [0, 1],   # +10% geld per klik per level
    "Upgrade Discount": [0, 1],    # -10% upgrade kosten per level
    "Team Boost": [0, 2],          # +1 Iron Drill start per level
    "Auto Start Bonus": [0, 3]     # +500 goud bij start per level
}

# --- RP-effecten ---
rebirth_effects = {
    "Mining Efficiency": "+10% geld per klik per level",
    "Upgrade Discount": "-10% upgrade kosten per level",
    "Team Boost": "+1 Iron Drill start per level",
    "Auto Start Bonus": "+500 goud bij start per level"
}

# Basis RP-formule
RP_basis = 10000
RP_factor = 2

# --- Functies ---

def geld_per_klik():
    totaal = basis_per_klik
    for drill in drills:
        totaal += drill[2] * drill[4]
    totaal *= 1 + 0.1 * rebirth_upgrades["Mining Efficiency"][0]
    return totaal

def drill_prijs(drill):
    prijs = drill[5]  # huidige prijs
    korting = 0.1 * rebirth_upgrades["Upgrade Discount"][0]
    return prijs * (1 - korting)

def geld_voor_volgende_RP():
    return RP_basis * (RP_factor ** RP)

def save_game():
    bestand = open("save.txt", "w")
    bestand.write(str(geld) + "\n")
    bestand.write(str(RP) + "\n")
    for key in rebirth_upgrades:
        bestand.write(str(rebirth_upgrades[key][0]) + "\n")
    for drill in drills:
        bestand.write(str(drill[4]) + "\n")  # aantal
        bestand.write(str(drill[5]) + "\n")  # huidige prijs
    bestand.close()
    print("Game opgeslagen!\n")

def load_game():
    global geld, RP
    try:
        bestand = open("save.txt", "r")
        regels = bestand.readlines()
        bestand.close()
        geld = float(regels[0])
        RP = int(regels[1])
        idx = 2
        for key in rebirth_upgrades:
            rebirth_upgrades[key][0] = int(regels[idx])
            idx += 1
        for drill in drills:
            drill[4] = int(regels[idx])
            idx += 1
            drill[5] = float(regels[idx])
            idx += 1
        print("Game geladen!\n")
    except:
        print("Geen save bestand gevonden.\n")

def uitgeven_RP():
    global RP, geld, drills
    while True:
        print(f"\nJe hebt {RP} RP om uit te geven!")
        print("Upgrades:")
        for i, key in enumerate(rebirth_upgrades):
            lvl, kost = rebirth_upgrades[key]
            effect = rebirth_effects[key]
            print(f"{i+1}) {key} | Level: {lvl} | Kost: {kost} RP | Effect: {effect}")
        print("0) Terug naar spel")
        
        keuze = input("Kies een upgrade om RP te spenderen (0-4): ")
        if keuze == "0":
            break
        elif keuze in ["1","2","3","4"]:
            i = int(keuze)-1
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

# --- Startspel ---
geld += 500 * rebirth_upgrades["Auto Start Bonus"][0]
drills[0][4] += rebirth_upgrades["Team Boost"][0]

print("Welkom bij Mine Simulator met Rebirth-upgrades!")
print("Enter = geld verdienen, 1-5 = drills kopen, r=rebirth, u=RP upgraden, s=save, l=load, q=stop\n")

while True:
    # weergave van geld en geld per klik
    if geld == int(geld):
        g = int(geld)
    else:
        g = round(geld, 2)
    
    if geld_per_klik() == int(geld_per_klik()):
        gpc = int(geld_per_klik())
    else:
        gpc = round(geld_per_klik(), 2)
    
    print(f"Geld: {g}  |  Geld per klik: {gpc}  |  RP: {RP}")
    print("Drills:")
    for i, drill in enumerate(drills):
        prijs = drill_prijs(drill)
        # Drills blijven gehele getallen tonen
        prijs_display = int(prijs)
        aantal_display = drill[4]
        print(f"{i+1}) {drill[0]:<15} Aantal: {aantal_display}  Kost: {prijs_display}  +{drill[2]}/klik")
    print(f"Volgende RP kost: {int(geld_voor_volgende_RP())}\n")
    
    actie = input("Enter=klik, 1-5=drill, r=rebirth, u=RP upgraden, s=save, l=load, q=stop: ").lower()
    
    if actie == "":
        verdiend = geld_per_klik()
        geld += verdiend
        print(f"Je verdiende {round(verdiend,2)} goud!\n")
    
    elif actie in ["1","2","3","4","5"]:
        i = int(actie) - 1
        prijs = drill_prijs(drills[i])
        if geld >= prijs:
            geld -= prijs
            drills[i][4] += 1
            drills[i][5] *= drills[i][3]
            print(f"Je kocht een {drills[i][0]}!\n")
        else:
            print("Niet genoeg geld!\n")
    
    elif actie == "r":
        if geld >= geld_voor_volgende_RP():
            RP += 1
            geld = 0.0
            for drill in drills:
                drill[4] = 0
                drill[5] = drill[1]  # reset huidige prijs naar startprijs
            # Pas Auto Start Bonus en Team Boost toe
            geld += 500 * rebirth_upgrades["Auto Start Bonus"][0]
            drills[0][4] += rebirth_upgrades["Team Boost"][0]
            print(f"Rebirth voltooid! RP={RP}\n")
        else:
            print("Niet genoeg geld om te rebirthen!\n")
    
    elif actie == "u":
        uitgeven_RP()
    
    elif actie == "s":
        save_game()
    
    elif actie == "l":
        load_game()
    
    elif actie == "q":
        print("Game afgesloten!")
        break
    
    else:
        print("Ongeldige keuze!\n")

