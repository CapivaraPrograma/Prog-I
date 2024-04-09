# Programa para retornar a quantidade de vogais dentro de uma palavra dada pelo usuário.

palavra_usuario =input("Digite uma palavra: ")
vogais = "aeiou"
qtd_vogais = 0

# Verificar se existi uma vogal na palavra
for indice in range(len(palavra_usuario)):
    if palavra_usuario[indice].lower() in vogais:
        qtd_vogais += 1

# Formatação do texto
tem_volta = f"A palavra que você digitou tem um total de {qtd_vogais} vogais"
nao_tem_vogal = "A palavra que você digitou não possue vogais"
saida_final = tem_volta if qtd_vogais > 0 else nao_tem_vogal

print(saida_final)

