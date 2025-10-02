def save_game(geld, RP, rebirth_upgrades, drills):
    with open("save.txt", "w") as bestand:
        bestand.write(str(geld) + "\n")
        bestand.write(str(RP) + "\n")
        for key in rebirth_upgrades:
            bestand.write(str(rebirth_upgrades[key][0]) + "\n")
        for drill in drills:
            bestand.write(str(drill[4]) + "\n")
            bestand.write(str(drill[5]) + "\n")
    print("Game opgeslagen!\n")

def load_game(rebirth_upgrades, drills):
    try:
        with open("save.txt", "r") as bestand:
            regels = bestand.readlines()
        geld = float(regels[0])
        RP = int(regels[1])
        idx = 2
        for key in rebirth_upgrades:
            rebirth_upgrades[key][0] = int(regels[idx]); idx += 1
        for drill in drills:
            drill[4] = int(regels[idx]); idx += 1
            drill[5] = float(regels[idx]); idx += 1
        print("Game geladen!\n")
        return geld, RP, rebirth_upgrades, drills
    except:
        print("Geen save bestand gevonden.\n")
        return 0.0, 0, rebirth_upgrades, drills
