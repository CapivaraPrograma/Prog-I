""" 06 - Programa que valida uma senha. A senha dever ter:
- Pelo menos 8 caracter.
- Pelo menos 1 letra maiúscula e minúscula.
- E pelo menos 1 número.
"""

print(20*"-----")
print("Crie uma senha válida. Para um senha ser válida deve atender os seguintes requisitos:\n " +
"- Ter pelo menos oito caracteres\n - Pelo menos uma letra maiúscula e uma minúscula\n - E pelo menos um número\n"
+ "Exemplo: ABCdef123, 123ABCdef,abc123DEF")

print(20*"-----")


while True:
    # Entrada do Usuario
    senha_usuario = input("Digite uma senha válida: ")
    
    # Condições de Validação da senha
    min_caracter = len(senha_usuario) >= 8
    letra_maiscula, letra_minuscula, tem_numero = False, False, False
    for caracter in senha_usuario:
        if caracter.isupper():
            letra_maiscula = True
        elif caracter.islower():
            letra_minuscula = True
        elif caracter.isdigit():
            tem_numero = True
    
    #  Verificar se a senha é válida 
    if min_caracter and letra_maiscula and letra_minuscula and tem_numero:
        print("A sua senha é válida.")
        break
    else:
        if not min_caracter:
            print("A senha é muito curta")
        if not letra_maiscula:
            print("A senha deve ter pelo menos uma letra maiúscula")
        if not letra_minuscula:
            print("A senha deve ter pelo menos uma letra minúscula")
        if not tem_numero:
            print("A senha deve ter pelo menos um número")