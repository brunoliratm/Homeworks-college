n = int(input("Quantas pessoas serão digitadas? "))

nomes = []
idades = []
alturas = []

for i in range(n):
    print(f"Dados da {i+1}a pessoa:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)

altura_media = sum(alturas) / n
print(f"Altura média: {altura_media:.2f}")

menores = sum(1 for idade in idades if idade < 16)
porcentagem_menores_16 = (menores / n) * 100
print(f"Pessoas com menos de 16 anos: {porcentagem_menores_16:.1f}%")

if menores > 0:
    print("Nomes das pessoas com menos de 16 anos:")
    for i in range(n):
        if idades[i] < 16:
            print(nomes[i])
