import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_numero(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem)
        try:
            numero = int(entrada)
            if numero >= minimo and numero <= maximo:
                return numero
            else:
                print("O número deve estar entre", minimo, "e", maximo)
        except ValueError:
            print("Por favor, insira um número válido")

def validar_texto(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada != "":
            return entrada
        print("Isto não pode estar vazio")
