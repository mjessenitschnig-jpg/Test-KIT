import tkinter as tk
import random

# Konstanten für das Spiel
SPIEL_BREITE = 600
SPIEL_HOEHE = 400
GESCHWINDIGKEIT = 100  # Je niedriger, desto schneller das Spiel (in Millisekunden)
TEIL_GROESSE = 20      # Größe eines Schlangenglieds / des Futters
SCHLANGEN_FARBE = "#2ecc71"  # Grün
FUTTER_FARBE = "#e74c3c"     # Rot
HINTERGRUND_FARBE = "#2c3e50" # Dunkelblau

class SnakeSpiel:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Snake")
        self.root.resizable(False, False)

        # Punktestand
        self.score = 0
        self.score_label = tk.Label(root, text=f"Punkte: {self.score}", font=("Helvetica", 14, "bold"))
        self.score_label.pack()

        # Spielfeld (Spielfläche)
        self.canvas = tk.Canvas(root, bg=HINTERGRUND_FARBE, height=SPIEL_HOEHE, width=SPIEL_BREITE)
        self.canvas.pack()

        # Steuerung binden
        self.root.bind("<Left>", lambda event: self.richtung_wechseln("left"))
        self.root.bind("<Right>", lambda event: self.richtung_wechseln("right"))
        self.root.bind("<Up>", lambda event: self.richtung_wechseln("up"))
        self.root.bind("<Down>", lambda event: self.richtung_wechseln("down"))

        # Spiel zurücksetzen und starten
        self.spiel_zuruecksetzen()

    def spiel_zuruecksetzen(self):
        self.score = 0
        self.score_label.config(text=f"Punkte: {self.score}")
        self.richtung = "right"
        self.spiel_laeuft = True

        # Startposition der Schlange (3 Glieder)
        self.schlange = [
            [100, 100],
            [80, 100],
            [60, 100]
        ]
        
        self.futter = None
        self.futter_platzieren()
        self.aktualisieren()

    def futter_platzieren(self):
        # Zufällige Position auf dem Raster berechnen
        while True:
            x = random.randint(0, int((SPIEL_BREITE / TEIL_GROESSE) - 1)) * TEIL_GROESSE
            y = random.randint(0, int((SPIEL_HOEHE / TEIL_GROESSE) - 1)) * TEIL_GROESSE
            # Sicherstellen, dass das Futter nicht in der Schlange landet
            if [x, y] not in self.schlange:
                self.futter = [x, y]
                break

    def richtung_wechseln(self, neue_richtung):
        # Verhindert, dass die Schlange direkt in sich selbst hineinsteuert
        gegenteile = {"left": "right", "right": "left", "up": "down", "down": "up"}
        if neue_direction := neue_richtung:
            if neue_direction != gegenteile.get(self.richtung):
                self.richtung = neue_direction

    def kollisionen_pruefen(self):
        kopf_x, kopf_y = self.schlange[0]

        # Wand-Kollision
        if kopf_x < 0 or kopf_x >= SPIEL_BREITE or kopf_y < 0 or kopf_y >= SPIEL_HOEHE:
            return True

        # Selbst-Kollision (Kopf trifft Körper)
        if [kopf_x, kopf_y] in self.schlange[1:]:
            return True

        return False

    def spiel_ende(self):
        self.spiel_laeuft = False
        self.canvas.create_text(
            SPIEL_BREITE/2, SPIEL_HOEHE/2,
            text="GAME OVER\nDrücke LEERTASTE für Neustart",
            fill="white", font=("Helvetica", 20, "bold"), justify="center"
        )
        self.root.bind("<space>", lambda event: self.neustart())

    def neustart(self):
        self.canvas.delete("all")
        self.root.unbind("<space>")
        self.spiel_zuruecksetzen()

    def aktualisieren(self):
        if not self.spiel_laeuft:
            return

        # Berechne neue Kopfposition basierend auf der Richtung
        kopf_x, kopf_y = self.schlange[0]
        if self.richtung == "up":
            kopf_y -= TEIL_GROESSE
        elif self.richtung == "down":
            kopf_y += TEIL_GROESSE
        elif self.richtung == "left":
            kopf_x -= TEIL_GROESSE
        elif self.richtung == "right":
            kopf_x += TEIL_GROESSE

        # Neuen Kopf hinzufügen
        neuer_kopf = [kopf_x, kopf_y]
        self.schlange.insert(0, neuer_kopf)

        # Prüfen, ob Futter gefressen wurde
        if kopf_x == self.futter[0] and kopf_y == self.futter[1]:
            self.score += 1
            self.score_label.config(text=f"Punkte: {self.score}")
            self.futter_platzieren()
        else:
            # Wenn kein Futter gefressen wurde, das letzte Glied entfernen
            self.schlange.pop()

        # Prüfen, ob das Spiel vorbei ist
        if self.kollisionen_pruefen():
            self.spiel_ende()
            return

        # Zeichnen
        self.canvas.delete("all")
        
        # Futter zeichnen
        self.canvas.create_oval(
            self.futter[0], self.futter[1],
            self.futter[0] + TEIL_GROESSE, self.futter[1] + TEIL_GROESSE,
            fill=FUTTER_FARBE, outline=""
        )

        # Schlange zeichnen
        for glied in self.schlange:
            self.canvas.create_rectangle(
                glied[0], glied[1],
                glied[0] + TEIL_GROESSE, glied[1] + TEIL_GROESSE,
                fill=SCHLANGEN_FARBE, outline=HINTERGRUND_FARBE
            )

        # Nächsten Schritt timen
        self.root.after(GESCHWINDIGKEIT, self.aktualisieren)

# Hauptprogramm starten
if __name__ == "__main__":
    root = tk.Tk()
    spiel = SnakeSpiel(root)
    root.mainloop()