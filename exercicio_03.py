# Programa para verificar qual o gênero de uma pessoa.Ex: M (masculino) e F (feminino)
while True:
    opcao_genero = input("Escolha um gênero: [M]asculino ou [F]eminino: ")
    if opcao_genero[0].upper() == "M":
        genero = "Masculino"
    elif opcao_genero[0].upper() == "F":
        genero = "Feminino"
    else:
        print("Opção inválida, digite novamente")
        continue
    print(f"Você digitou o gênero: {genero}.")
    break
