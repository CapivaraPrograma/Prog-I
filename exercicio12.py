# Programa que realize a sequência de Fibonacci

n = int(input("Que termo deseja encontrar: "))
ultimo, penultimo = 1, 1

if (n==1) or (n==2):
    print("1")
else:
    count=1
    while count <= n:
        print(f"Você está no termo: {count}")
        termo, ultimo, penultimo = ultimo ,penultimo, ultimo + penultimo
        count += 1
        print(termo)