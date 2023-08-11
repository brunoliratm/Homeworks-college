import os
import time


historico = {}

def limpador():
    os.system('cls' if os.name =='nt' else 'clear')

def inicio():
    limpador()
    print("Bem-Vindo a calculadora em python")
    print("By Bruno Magno")
    time.sleep(2)
    print("")
    print("")
    menu()

def menu():
    print("--- Menu ---")
    print("")
    time.sleep(1)
    print("Escolha o número da opção desejada")
    print("1 - Calculadora")
    print("2 - histórico da calculos")
    print("3 - Sair do programa")
    opcao = input("--> ")
    limpador()

    match opcao:
        case '1':
            calculadora()
        case '2':
            mostrar_historico()
        case '3':
            saida()
        case other:
            print("Opção inválida") 
            time.sleep(2)
            menu()  

def calculadora():
    print("--- Calculadora ---")
    print("")
    time.sleep(1)
    expressao = input("Digite a expressão matemática: ")
    try:
        resultado = eval(expressao)
        print(f"Resultado: {resultado:0.2f}")
        historico[expressao]={'resultado':resultado}
        time.sleep(3)
        limpador()
        menu()
    except (SyntaxError, ValueError, Exception):
        print("expressão inválida, tente novamente")
        time.sleep(3)
        limpador()
        calculadora()

def mostrar_historico():
    print("--- Historico --- ")
    print("")
    for expressao, resultado in historico.items():
        print(f"Expressão: {expressao} | Resultado: {resultado['resultado']:0.2f}")
    time.sleep(5)
    limpador()
    menu()

def saida():
    exit()

inicio()