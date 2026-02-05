# PLANIFICACAO.md — Créé par Enzo et Domingos

### 1. Modèle de Données

Nous utiliserons des listes de dictionnaires pour gérer les informations en mémoire. Cette structure permet d'accéder facilement aux données et de les convertir au format JSON.

**Exemple 1 : Structure d'une question**

```python
pergunta_exemplo = {
    "id": 1,
    "pergunta": "Quelle est la capitale du Portugal ?",
    "opcoes": ["Porto", "Lisbonne", "Coimbra", "Braga"],
    "resposta": 1, 
    "categoria": "Géographie",
    "dificuldade": "facile",
    "explicacao": "Lisbonne est la capitale et la plus grande ville du Portugal."
}

```

**Exemple 2 : Structure du score de classement**

```python
score_exemplo = {
    "nome": "Enzo",
    "pontos": 8,
    "total_perguntas": 10,
    "data": "2024-05-20"
}

```

#

### 2. Entrées / Traitement / Sorties

| Phase | Description |
| --- | --- |
| **Entrées** | Options du menu, nom du joueur, réponses (indices 1-4), fichier `perguntas.json`. |
| **Traitement** | Validation des types, calcul du score, filtrage par difficulté, tri du Top 10 pour la récupération des scores. |
| **Sorties** | Menus formatés, feedback des réponses, résumé final, écriture dans le fichier `pontuacoes.json`. |

#

### 3. Liste des Fonctions et Responsabilités

| Fonction | Description | Responsabilité |
| --- | --- | --- |
| `carregar_json` | Lit les fichiers JSON et gère les erreurs de fichier inexistant. | Étudiant A |
| `guardar_score` | Ajoute et enregistre les nouveaux résultats dans l'historique. | Étudiant A |
| `validar_input` | Garantit que l'utilisateur saisit un nombre valide dans l'intervalle. | Étudiant B |
| `exibir_pergunta` | Gère l'affichage de la question et vérifie si la réponse correspond à l'indice correct. | Étudiant B |
| `gerar_quiz` | Filtre les questions par difficulté choisie et les mélange. | Étudiant C |
| `mostrar_ranking` | Lit le fichier des scores et affiche les 10 meilleurs résultats. | Étudiant C |

#

### 4. Flux du Programme

* **Lancer le programme** et charger les données du fichier `perguntas.json`.
* **Afficher le menu principal** avec les options : Jouer, Classement et Quitter.
* **Lire le choix de l'utilisateur :** si la saisie est invalide répéter la demande jusqu'à obtenir un numéro valide.
* **Si le choix est "Jouer" :** 1. Demander le nom et la difficulté.
2. Charger les questions correspondantes.
3. Lancer la **boucle de jeu** : afficher l'énoncé, valider que la réponse est entre 1 et 4, mettre à jour le score et afficher l'explication.
4. À la fin, afficher le **résumé des points**, sauvegarder le score et proposer de rejouer ou de revenir au menu.
* **Si le choix est "Voir le classement" :** Lire le fichier `pontuacoes.json` et afficher le Top 10 des meilleurs scores, puis revenir au menu.
* **Si le choix est "Quitter" :** Afficher un message de fin et fermer et mettre fin au code lancer

#

### 5. Structure des Fichiers

* **`main.py`** : Fichier principal du jeux. Qui contient la boucle principale et le menu.
* **`logica_jogo.py`** : Fichier qui contient les fonctions spécifiques au quiz (les questions, la vérification des réponses, affichage des réponses).
* **`utils.py`** : Fichier qui contient les fonctions utils (validation des saisies dans le terminal etc).
* **`perguntas.json`** : Fichier qui contient les questions.
* **`pontuacoes.json`** : Fichier qui contient l'historique des classements.

#

### 6. Plan de Tests (Manuel)

1. **Erreur de saisie :** si on entre exepme **"abc"** dans le menu au lieu d'un nombre. (**Attendu : Erreur et répétition de la demande**).
2. **Hors limite :** Saisir "5" alors qu'il n'y a que 4 options. (**Attendu : Message d'option invalide**), Fait via le fichier `utils.py`.
3. **Fichier inexistant :** Renommer `perguntas.json` et lancer le jeu. (**Attendu : Message d'erreur "Fichier non trouvé"**), Fait via le fichier `utils.py`.
4. **Saisie vide :** Appuyer sur `Entrée` sans rien écrire. (**Attendu : Pas de crash, répétition de la demande**).
5. **Difficulté :** Choisir "facile" et vérifier qu'aucune question "difficile" n'apparaît.
6. **Classement (Ranking) :** Vérifier que le nom et le score s'affichent correctement après la fin d'une partie via un print basique
7. **Répétition :** Jouer 2 fois de suite sans fermer le programme et vérifier que les points se réinitialisent correctement.
8. **Quitter :** Quitter le programme et vérifier que le fichier `pontuacoes.json` est bien sauvegardé les scores.
9. **Erreur de fichier :** Renommer `pontuacoes.json` et lancer le jeu. (**Attendu : Message d'erreur "Fichier non trouvé"**), Fait via le fichier `utils.py` etc sur d'autre fichiers comme : `perguntas.json`, etc.

link pour aider a faire se fichier .md (Documentation en FR) : [Clique ici](https://datascientist.fr/blog/guide-ultime-creer-fichiers-readme-md-efficaces-markdown)