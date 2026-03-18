import random
from utils import effacer, valider_numero, valider_texte
from logica_jogo import lire_json, sauvegarder_score, filtrer_questions, afficher_classement

def jouer():
    questions = lire_json("perguntas.json")
    if len(questions) == 0:
        return

    effacer()
    print("\n--- MATCH ---")
    nom = valider_texte("Votre nom : ")

    print("\nChoisissez une categorie :")
    print("1 - Geographie")
    print("2 - Histoire")
    print("3 - Science")
    print("4 - Litterature")
    print("5 - General")
    print("6 - Toutes")
    choix_cat = valider_numero("Votre choix : ", 1, 6)
    if choix_cat == 1: cat = "Geografia"
    elif choix_cat == 2: cat = "História"
    elif choix_cat == 3: cat = "Ciência"
    elif choix_cat == 4: cat = "Literatura"
    elif choix_cat == 5: cat = "Geral"
    else: cat = "Toutes"

    print("\nChoisissez une difficulte :")
    print("1 - Facile")
    print("2 - Moyenne")
    print("3 - Difficile")
    print("4 - Toutes")
    choix_diff = valider_numero("Votre choix : ", 1, 4)
    if choix_diff == 1: diff = "facil"
    elif choix_diff == 2: diff = "médio"
    elif choix_diff == 3: diff = "difícil"
    else: diff = "Toutes"

    questions_jeu = filtrer_questions(questions, cat, diff)
    if len(questions_jeu) == 0:
        print("Aucune question rencontree pour cette selection.")
        return

    random.shuffle(questions_jeu)
    questions_jeu = questions_jeu[:5]

    points = 0
    for q in questions_jeu:
        effacer()
        print("\nQuestion :")
        print(q["pergunta"])
        print("")
        print("1 -", q["opcoes"][0])
        print("2 -", q["opcoes"][1])
        print("3 -", q["opcoes"][2])
        print("4 -", q["opcoes"][3])
        print("")

        rep = valider_numero("Votre reponse (1-4) : ", 1, 4)
        index_rep = rep - 1

        if index_rep == q["resposta"]:
            print("\nCorrect !")
            points = points + 1
        else:
            print("\nFaux.")
            bon_index = q["resposta"]
            print("La reponse etait :", q["opcoes"][bon_index])

        if "explicacao" in q:
            print("Explication :", q["explicacao"])

        input("\nEntree pour continuer...")

    effacer()
    print("\nPartie terminee !")
    print("Score :", points, "/", len(questions_jeu))

    sauvegarder_score("pontuacoes.json", nom, points, len(questions_jeu), diff)

def main():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Lancer une partie")
        print("2 - Voir le classement")
        print("3 - Sortir")
        print("----------------------")

        choix = valider_numero("Votre choix : ", 1, 3)

        if choix == 1:
            jouer()
        elif choix == 2:
            afficher_classement("pontuacoes.json")
            input("Entree pour revenir au menu...")
        elif choix == 3:
            print("Fin du jeu.")
            break

if __name__ == "__main__":
    main()
