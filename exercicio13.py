# Programa que execute uma tabuada simples

numero = int(input("Digite um número entre 1 e 10 para ver sua tabuada: "))
while True:
    if numero > 0 and numero < 11:
        print("\nAdição")
        for i in range(1, 11):
            adi = numero + i
            print(f"{numero} + {i}: {adi}")

        print("\nSubtração")
        for i in range(1, 11):
            sub = numero - i
            print(f"{numero} - {i}: {sub:2}")
        

        print("\nMultiplicação")
        for i in range(1, 11):
            mult = numero * i
            print(f"{numero} x {i}: {mult}")

        print("\nDivisão inteira")
        for i in range(1, 11):
            div = numero // i
            print(f"{numero} / {i}: {div:2}")

        break
    else:
        print("Número inválido, digite um número de 1 até 10:")