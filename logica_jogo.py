import json
import random

def ler_json(ficheiro):
    try:
        f = open(ficheiro, "r", encoding="utf-8")
        dados = json.load(f)
        f.close()
        return dados
    except FileNotFoundError:
        print("Ficheiro não encontrado")
        return []

def salvar_pontuacao(ficheiro, nome, pontos, total, diff, cat):
    pontuacoes = ler_json(ficheiro)
    novo = {
        "nome": nome,
        "pontos": pontos,
        "total": total,
        "diff": diff,
        "cat": cat
    }
    pontuacoes.append(novo)
    f = open(ficheiro, "w", encoding="utf-8")
    json.dump(pontuacoes, f, indent=4)
    f.close()

def filtrar_perguntas(perguntas, cat, diff):
    lista = []
    for q in perguntas:
        if cat != "Todas" and q["categoria"] != cat:
            continue

        if diff != "Todas" and q["dificuldade"] != diff:
            continue
        lista.append(q)
    return lista

def ordenar_pontuacao(elemento):
    return elemento["pontos"]

def mostrar_classificacao(ficheiro):
    pontuacoes = ler_json(ficheiro)
    if len(pontuacoes) == 0:
        print("Nenhum recorde")
        return
    pontuacoes.sort(key=ordenar_pontuacao, reverse=True)
    print("\n--- CLASSIFICAÇÃO TOP 10 ---")
    i = 1
    for p in pontuacoes[:10]:
        print(i, "-", p["nome"], ":", p["pontos"], "/", p["total"], "(", p["diff"], "-", p.get("cat", "Todas"), ")")
        i = i + 1
    print("-------------------------\n")
