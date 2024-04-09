#  08 - Programa para calcular a média de 4 notas de um aluno
soma = 0
for i in range(1,5):
    nota  = int(input(f"Digite o valor da {i}º nota: "))
    soma += nota

media = soma / 4
print(f"A media das notas do aluno é {media}.")