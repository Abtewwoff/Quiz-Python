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
                print("faut que le nombre soit entre", mini, "et", maxi)
        except ValueError:
            print("faut Entrez un nombre valide")

def valider_texte(message):
    while True:
        saisie = input(message).strip()
        if saisie != "":
            return saisie
        print("Ceci ne peut pas être vide")
