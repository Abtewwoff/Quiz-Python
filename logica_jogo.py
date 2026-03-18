import json
import random

def lire_json(fichier):
    try:
        f = open(fichier, "r", encoding="utf-8")
        donnees = json.load(f)
        f.close()
        return donnees
    except FileNotFoundError:
        print("Fichier introuvable")
        return []

def sauvegarder_score(fichier, nom, points, total, diff, cat):
    scores = lire_json(fichier)
    nouveau = {
        "nom": nom,
        "points": points,
        "total": total,
        "diff": diff,
        "cat": cat
    }
    scores.append(nouveau)
    f = open(fichier, "w", encoding="utf-8")
    json.dump(scores, f, indent=4)
    f.close()

def filtrer_questions(questions, cat, diff):
    liste = []
    for q in questions:
        if cat != "Toutes" and q["categoria"] != cat:
            continue

        if diff != "Toutes" and q["dificuldade"] != diff:
            continue
        liste.append(q)
    return liste

def trier_score(element):
    return element["points"]

def afficher_classement(fichier):
    scores = lire_json(fichier)
    if len(scores) == 0:
        print("Aucun record")
        return
    scores.sort(key=trier_score, reverse=True)
    print("\n--- CLASSEMENT TOP 10 ---")
    i = 1
    for s in scores[:10]:
        print(i, "-", s["nom"], ":", s["points"], "/", s["total"], "(", s["diff"], "-", s.get("cat", "Toutes"), ")")
        i = i + 1
    print("-------------------------\n")
