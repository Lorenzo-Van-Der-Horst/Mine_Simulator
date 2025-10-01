#Mine Simulator
#by: Lorenzo van der Horst en Nick Pauel
#Date: 2025-09-30
#Version: 1.0

# --- Startwaarden ---
money = 500
rebirth_points = 0 # placeholder
production = 1  # placeholder

# --- Main menu loop ---
while True:
    menu_choice = input(f"""
==============================
         Mine Simulator
==============================

Goud: {money}
RP: {rebirth_points} 
Totaal productie/sec: {production} 

--- Acties ---
[A] Verdien goud handmatig (+10 goud)
[B] Koop drills
[C] Rebirth / Claim RP
[D] Toon Rebirth-upgrades
[E] Verlaat spel

Kies een optie: """)
    
    if menu_choice.lower() == "a":
        money += 10
        print(f"Je hebt 10 geld verdiend! Je hebt nu {money} geld.")
