import random
from utils import limpar, validar_numero, validar_texto
from logica_jogo import ler_json, salvar_pontuacao, filtrar_perguntas, mostrar_classificacao

def jogar():
    perguntas = ler_json("perguntas.json")
    if len(perguntas) == 0:
        return

    limpar()
    print("\n--- PARTIDA ---")
    nome = validar_texto("Seu nome: ")

    print("\nEscolha uma categoria:")
    print("1 - Geografia")
    print("2 - História")
    print("3 - Ciência")
    print("4 - Literatura")
    print("5 - Geral")
    print("6 - Todas")
    escolha_cat = validar_numero("Sua escolha: ", 1, 6)
    if escolha_cat == 1: cat = "Geografia"
    elif escolha_cat == 2: cat = "História"
    elif escolha_cat == 3: cat = "Ciência"
    elif escolha_cat == 4: cat = "Literatura"
    elif escolha_cat == 5: cat = "Geral"
    else: cat = "Todas"

    print("\nEscolha uma dificuldade:")
    print("1 - Fácil")
    print("2 - Média")
    print("3 - Difícil")
    print("4 - Todas")
    escolha_diff = validar_numero("Sua escolha: ", 1, 4)
    if escolha_diff == 1: diff = "facil"
    elif escolha_diff == 2: diff = "médio"
    elif escolha_diff == 3: diff = "difícil"
    else: diff = "Todas"

    perguntas_jogo = filtrar_perguntas(perguntas, cat, diff)
    if len(perguntas_jogo) == 0:
        print("Nenhuma pergunta encontrada para esta seleção.")
        return

    random.shuffle(perguntas_jogo)
    perguntas_jogo = perguntas_jogo[:5]

    pontos = 0
    for q in perguntas_jogo:
        limpar()
        print("\nPergunta:")
        print(q["pergunta"])
        print("")
        print("1 -", q["opcoes"][0])
        print("2 -", q["opcoes"][1])
        print("3 -", q["opcoes"][2])
        print("4 -", q["opcoes"][3])
        print("")

        resp = validar_numero("Sua resposta (1-4): ", 1, 4)
        indice_resp = resp - 1

        if resp == q["resposta"]:
            print("\nCorreto!")
            pontos = pontos + 1
        else:
            print("\nIncorreto.")
            indice_correto = q["resposta"] - 1
            print("A resposta era:", q["opcoes"][indice_correto])

        if "explicacao" in q:
            print("Explicação:", q["explicacao"])

        input("\nEnter para continuar...")

    limpar()
    print("\nPartida terminada!")
    print("Pontuação:", pontos, "/", len(perguntas_jogo))

    salvar_pontuacao("pontuacoes.json", nome, pontos, len(perguntas_jogo), diff, cat)

def main():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Iniciar uma partida")
        print("2 - Ver a classificação")
        print("3 - Sair")
        print("----------------------")

        escolha = validar_numero("Sua escolha: ", 1, 3)

        if escolha == 1:
            jogar()
        elif escolha == 2:
            mostrar_classificacao("pontuacoes.json")
            input("Enter para voltar ao menu...")
        elif escolha == 3:
            print("Fim do jogo.")
            break

if __name__ == "__main__":
    main()
