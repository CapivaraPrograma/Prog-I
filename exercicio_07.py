# 07 - Programa para calcular a fatorial de um número que foi inserido pelo usuário.

numero_digitado = int(input("Digite um número: "))
fatorial = 1

for n in range(1, numero_digitado+1):
    fatorial *= n
    
print(f"A fatorial do número {numero_digitado} é: {fatorial}")
