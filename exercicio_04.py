# 04 - Crie um programa que receba um número inteiro positivo e depois calcule a soma de todos
# os número pares até esse número.

numero_int_positivo = int(input("Digite um número inteiro positivo: "))
soma = 0
i = 0
print(f"O número pares de 0 até {numero_int_positivo} são: ")
while i <= numero_int_positivo:
    print(f"Numero: {i}")
    soma += i
    i += 2
    
print(f"A soma desses números é: {soma}")
    
    