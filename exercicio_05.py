# Programa para calcular a área de um triângulo considerando que a base e a altura
# são fornecidas pelo usuário. Se a área for maior que 100 o código deve exibir "grande" se não "pequeno"

altura_triangulo = int(input("Digite o valor da altura do trinagulo: "))
base_triangulo = int(input("Digite o valor da base do triangulo: "))

area_do_triangulo = altura_triangulo * base_triangulo / 2
tamanho_triangulo = "grande" if area_do_triangulo > 100 else "pequeno"
print(f"A área do triângulo é: {area_do_triangulo}, o triangulo é {tamanho_triangulo}")


    
    
