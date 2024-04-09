# 01 - Programa para receber dois números e retornar o maior:
numero_01 = int(input("Digite um número inteiro: "))
numero_02 = int(input("Digite um número inteiro: "))

maior = numero_01
if numero_01 < numero_02:
    maior = numero_02

print(f"O maior número digitado é: {maior}")
