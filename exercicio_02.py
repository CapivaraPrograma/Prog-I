# 02 - Programa que receba um número e retornar se o valor é positivo ou negativo
numero = int(input("Digite um número positivo ou negativo: "))
sinal_numero = "positivo" if numero >= 0 else "negativo"
print(f"O número {numero:+} é {sinal_numero}")