import os

def effacer():
    os.system('cls' if os.name == 'nt' else 'clear')

def valider_numero(message, mini, maxi):
    while True:
        saisie = input(message)
        try:
            nombre = int(saisie)
            if nombre >= mini and nombre <= maxi:
                return nombre
            else:
                print("Erreur : nombre doit être entre", mini, "et", maxi)
        except ValueError:
            print("Erreur : Entrez un chiffre valide")

def valider_texte(message):
    while True:
        saisie = input(message).strip()
        if saisie != "":
            return saisie
        print("Erreur : ne peut pas être vide")
