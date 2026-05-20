import random
import sys

# Spieler-Statistiken
player = {
    "name": "Held",
    "hp": 100,
    "max_hp": 100,
    "attack": 15,
    "gold": 0,
    "potions = 1 # Anzahl der Heiltränke, die der Spieler besitzt"
    "MAX_POTIONS = 3 # Maximale Anzahl der Heiltränke, die der Spieler tragen kann"

    "position": [0, 0]  # [X, Y] Koordinaten im Dungeon
}

# Monster-Typen mit ihren möglichen Werten
MONSTER_TYPES = [
    {"name": "Große Ratte", "hp_range": (15, 25), "attack_range": (5, 10), "gold_range": (5, 15)},
    {"name": "Goblin", "hp_range": (25, 40), "attack_range": (8, 15), "gold_range": (15, 30)}
    {"name": "Skelett", "hp_range": (30, 50), "attack_range": (10, 20), "gold_range": (20, 40)},
    {"name": "Ork", "hp_range": (40, 60), "attack_range": (12, 25), "gold_range": (30, 50)},
    {"name": "Dämonenhund", "hp_range": (50, 80), "attack_range": (15, 30), "gold_range": (40, 70)},
    {"name": "Drachenjunges", "hp_range": (80, 120), "attack_range": (20, 40), "gold_range": (50, 100)}
]

def print_status():
    """Zeigt die aktuellen Werte des Spielers an."""
    print("\n" + "="*30)
    print(f"Spieler: {player['name']} | HP: {player['hp']}/{player['max_hp']} | Gold: {player['gold']}")
    print(f"Position im Dungeon: X={player['position'][0]}, Y={player['position'][1]}")
    print("="*30)

def drink_potion():
    global player_hp, potions
    
    if potions <= 0:
        print("❌ Du hast keine Heiltränke mehr!")
        return

    if player_hp >= player_max_hp:
        print("❤️ Deine Lebenspunkte sind schon voll!")
        return

    # Heilungs-Logik
    potions -= 1
    heal_amount = 30  # Heilt z.B. 30 HP
    player_hp = min(player_max_hp, player_hp + heal_amount)
    
    print(f"🧪 Du trinkst einen Heiltrank und regenerierst {heal_amount} HP.")
    print(f"❤️ Aktuelle HP: {player_hp}/{player_max_hp} | Tränke übrig: {potions}/{MAX_POTIONS}\n")

def check_loot():
    global potions
    
    # 35% Chance, einen Trank zu finden (0.35)
    if random.random() < 0.35:
        print("✨ Der Gegner hat etwas fallen gelassen...")
        
        if potions < MAX_POTIONS:
            potions += 1
            print(f"🧪 Du hast einen Heiltrank gefunden! (Tränke: {potions}/{MAX_POTIONS})")
        else:
            print("🎒 Du findest einen Trank, aber deine Taschen sind voll! (Maximum von 5 erreicht)")
    else:
        print("💀 Der Gegner hatte leider nichts Brauchbares dabei.")

def combat_round():
    # ... dein bisheriger Kampfcode ...
    
    print("Was willst du tun?")
    print("1. Angreifen")
    print(f"2. Heiltrank nehmen (Vorrat: {potions}/{MAX_POTIONS})")
    
    wahl = input("> ")
    
    if wahl == "1":
        # ... angriffs-logik ...
        pass
    elif wahl == "2":
        drink_potion()
        
    # Wenn der Gegner besiegt ist:
    # enemy_hp <= 0:
    #     print("Du hast gewonnen!")
    #     check_loot()  <-- Hier wird nach dem Kampf gewürfelt!
    
def battle():
    """Generiert einen Kampf mit einem zufälligen Monster."""
    # Zufälliges Monster auswählen und Werte auswürfeln
    monster_template = random.choice(MONSTER_TYPES)
    monster_name = monster_template["name"]
    monster_hp = random.randint(*monster_template["hp_range"])
    monster_max_attack = monster_template["attack_range"][1]
    
    print(f"\nPlötzlich springt ein {monster_name} aus dem Schatten! (HP: {monster_hp})")
    
    while monster_hp > 0 and player["hp"] > 0:
        print(f"\nDein HP: {player['hp']} | {monster_name} HP: {monster_hp}")
        action = input("Was tust du? (a = Angreifen, f = Fliehen): ").lower().strip()
        
        if action == 'a':
            # Spieler greift an (Zufälliger Schaden bis zum Maximalschaden)
            player_damage = random.randint(5, player["attack"])
            monster_hp -= player_damage
            print(f"Du triffst den {monster_name} für {player_damage} Schaden!")
            
            if monster_hp <= 0:
                break
                
            # Monster schlägt zurück
            monster_damage = random.randint(3, monster_max_attack)
            player["hp"] -= monster_damage
            print(f"Der {monster_name} greift dich an und macht {monster_damage} Schaden!")
            
        elif action == 'f':
            # Fluchtchance 50%
            if random.random() < 0.5:
                print("Flucht erfolgreich! Du rennst panisch zurück.")
                return
            else:
                print("Flucht fehlgeschlagen! Das Monster erwischt dich im Laufen.")
                monster_damage = random.randint(3, monster_max_attack)
                player["hp"] -= monster_damage
                print(f"Der {monster_name} trifft dich für {monster_damage} Schaden!")
        else:
            print("Ungültige Aktion! Du zögerst und das Monster nutzt die Chance.")
            monster_damage = random.randint(3, monster_max_attack)
            player["hp"] -= monster_damage
            print(f"Der {monster_name} trifft dich für {monster_damage} Schaden!")

    if player["hp"] <= 0:
        print("\nDu bist im Dungeon gefallen... GAME OVER.")
        sys.exit()
    else:
        # Siegbelohnung
        gold_drop = random.randint(*monster_template["gold_range"])
        player["gold"] += gold_drop
        print(f"\nSiegreich! Du hast den {monster_name} besiegt und {gold_drop} Gold gefunden.")
        
        # Kleine Chance auf Heilung nach dem Kampf
        if random.random() < 0.3:
            heal = random.randint(10, 20)
            player["hp"] = min(player["max_hp"], player["hp"] + heal)
            print(f"Du findest einen kleinen Heiltrank in den Überresten und heilst {heal} HP.")

def move():
    """Regelt die Bewegung des Spielers."""
    print_status()
    richtung = input("In welche Richtung willst du gehen? (N = Norden, S = Süden, O = Osten, W = Westen, Q = Beenden): ").lower().strip()
    
    if richtung == 'q':
        print("Du verlässt den Dungeon mit deiner Beute. Danke fürs Spielen!")
        sys.exit()
        
    if richtung == 'n':
        player["position"][1] += 1
        print("Du gehst nach Norden.")
    elif richtung == 's':
        player["position"][1] -= 1
        print("Du gehst nach Süden.")
    elif richtung == 'o':
        player["position"][0] += 1
        print("Du gehst nach Osten.")
    elif richtung == 'w':
        player["position"][0] -= 1
        print("Du gehst nach Westen.")
    else:
        print("Diese Richtung kenne ich nicht. Du läufst gegen eine Wand.")
        return

    # Zufallsevent nach der Bewegung (z.B. 40% Chance auf ein Monster)
    event_chance = random.random()
    if event_chance < 0.4:
        battle()
    elif event_chance < 0.5:
        # Ein kleines friedliches Event
        fund = random.randint(2, 8)
        player["gold"] += fund
        print(f"Du findest ein paar alte Münzen auf dem Boden! (+{fund} Gold)")
    else:
        print("Der Gang ist still. Hier ist im Moment nichts zu sehen.")

# Hauptschleife des Spiels
print("Willkommen im unendlichen Dungeon!")
player["name"] = input("Wie lautet der Name deines Helden? ") or "Held"

while True:
    move()

    