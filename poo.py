class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece

    def faire_du_bruit(self):
        if self.espece == "chien":
            print("Wouf!")
        elif self.espece == "chat":
            print("Miaou!")
        else:
            print("...")

mon_chien = Animal("Médor", "chien")
mon_chat = Animal("Biquette", "chat")

mon_chien.faire_du_bruit()  # Affiche "Wouf!"
mon_chat.faire_du_bruit()   # Affiche "Miaou!"