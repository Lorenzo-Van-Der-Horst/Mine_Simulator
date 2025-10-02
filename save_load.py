def save_game(money, RP, rebirth_upgrades, drills):
    with open("save.txt", "w") as file:
        file.write(str(money) + "\n")
        file.write(str(RP) + "\n")
        for key in rebirth_upgrades:
            file.write(str(rebirth_upgrades[key][0]) + "\n")
        for drill in drills:
            file.write(str(drill[4]) + "\n")
            file.write(str(drill[5]) + "\n")
    print("Game saved!\n")


def load_game(rebirth_upgrades, drills):
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
        money = float(lines[0])
        RP = int(lines[1])
        idx = 2
        for key in rebirth_upgrades:
            rebirth_upgrades[key][0] = int(lines[idx]); idx += 1
        for drill in drills:
            drill[4] = int(lines[idx]); idx += 1
            drill[5] = float(lines[idx]); idx += 1
        print("Game loaded!\n")
        return money, RP, rebirth_upgrades, drills
    except:
        print("No save file found.\n")
        return 0.0, 0, rebirth_upgrades, drills
