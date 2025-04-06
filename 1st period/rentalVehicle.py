import os
import time
from datetime import datetime, timedelta, date


today= date.today()
usuarios = {}
veiculos = {}  


#menu do usuario
def userMenu():
    print("---Área do Usuário---")
    print("")
    time.sleep(1)
    print("digite o número da opção desejada:")
    print("1 - Cadastro de usuário")
    print("2 - Descadastro de usuário")
    print("3 - Verificar usuários cadastrados")
    print("4 - Retornar ao menu inicial")
    opcao = input("--> ")
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:
        case '1':
            cadastroUsuario()
        case '2':
            removeUsuario()
        case '3':
            mostrarUsuarios()
        case '4':
            menu()
        case other:
            userMenu()

#cadastro do usuario
def cadastroUsuario():
    nome= input("Digite o nome do usuário: ").upper()
    email= input("Digite o e-mail do usuário: ")
    senha= input("Digite a senha do usuário: ")

    if nome in usuarios:
        print("Usuário já cadastrado.")
    else:
        usuarios[nome] = {'email': email, 'senha': senha}
        print(f"Usuário {nome} adicionado com sucesso.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    userMenu()

#remover usuario
def removeUsuario():
    nome = input("Digite o nome do usuário que deseja remover: ").upper()
    if nome in usuarios:
        del usuarios[nome]
        print("Usuário removido com sucesso.")
    else:
        print("Usuário não encontrado.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    userMenu()

#verificar usuários cadastrados
def mostrarUsuarios():
    print("Usuários cadastrados:")
    print("")
    for nome, dados in usuarios.items():
        print(f"Nome: {nome}  E-mail: {dados['email']}")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    userMenu()

#Menu de gerenciamento de veículos
def vehicleMenu():
    print("---Área de gerenciamento de veículos---")
    print("")
    time.sleep(1)
    print("digite o número da opção desejada:")
    print("1 - Cadastro de veículo")
    print("2 - Descadastro de veículo")
    print("3 - Alugar veículos")
    print("4 - Consultar veículos disponíveis e alugados")
    print("5 - Retornar ao menu inicial")
    opcao = input("--> ")
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:
        case '1':
            cadastroVeiculo()
        case '2':
            removerVeiculo()
        case '3':
            locarVeiculo()
        case '4':
            mostrarVeiculos()
        case '5':
            menu()
        case other:
            vehicleMenu()

#cadastrar veículos
def cadastroVeiculo():
    modelo= input("Digite o modelo do veículo: ").upper()
    placa = input("Digite a placa do veículo: ").upper()
    if placa in veiculos:
        print("Veículo já cadastrado!")
    else:
        veiculos[placa] = {"modelo": modelo, "disponivel": True}
        print("Veículo cadastrado com sucesso!")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    vehicleMenu()

#Remover veículo
def removerVeiculo():
    placa = input("Digite a placa do veículo a ser removido: ").upper()
    if placa in veiculos:
        del veiculos[placa]
        print("Veículo removido com sucesso!")
    else:
        print("Veículo não encontrado!")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    vehicleMenu()

#locar veiculo
def locarVeiculo():
    usuario=input("Digite o seu nome de usuário: ").upper()
    senha = input("Digite a sua senha: ")
    for i, j in usuarios.items():
        if i == usuario and j['senha'] == senha:
            placa = input("Digite a placa do veículo a ser alugado: ").upper()
            devolucao = int(input("Por quantos dias você deseja alugar o veículo: "))
            data_devolucao = datetime.now() + timedelta(days=devolucao)
            if placa in veiculos:
                if veiculos[placa]["disponivel"]:
                  veiculos[placa]["disponivel"] = False
                  veiculos[placa]["data_devolucao"] = data_devolucao
                  print("Veículo locado com sucesso!")
                else:
                  print("Veículo não disponível para locação!")
            else:
                print("Veículo não encontrado!")
        else:
            print("Usuário não encontrado")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    vehicleMenu() 

#Mostrar veiculos disponiveis e alugados
def mostrarVeiculos():
    print("Lista de veículos cadastrados:")
    for placa, dados in veiculos.items():
        modelo = dados["modelo"]
        disponivel = "Disponível" if dados["disponivel"] else "Alugado até " + dados["data_devolucao"].strftime("%d/%m/%Y, %H:%M:%S")
        print(f"Placa: {placa} - Modelo: {modelo} - Status: {disponivel}")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    vehicleMenu()

#saida do programa
def saida():
    exit()

#menu inicial
def menu():
    print(" ---Menu Inicial--- ")
    print("")
    time.sleep(1)
    print("digite o número da opção desejada:")
    print("1 - área do usuário")
    print("2 - Gerenciamento de Veículos")
    print("3 - Sair do programa")
    opcao = input("--> ")
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:
        case '1':
            userMenu()
        case '2':
            vehicleMenu()
        case '3':
            saida()
        case other:
            menu()
            
#introdução ao programa
def entrada():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nBem vindo ao nosso sistema de locação de carros")
    print(f"Dia de acesso do programa: {today}\n")
    time.sleep(2)
    menu()
    
entrada()
