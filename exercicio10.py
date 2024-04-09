# Programa que verifique se um CPF é válido

while True:
    cpf_usuario = input("Digite apenas os números do ceu cpf: ")
    
    # Validação para entrada de CPF.
    cpf_valido = cpf_usuario.isdigit() and (cpf_usuario != cpf_usuario[0] * 11)
    
    if len(cpf_usuario) == 11 and cpf_valido:
        soma1, soma2 = 0,0
        
        # Teste para verificar se o 1º digito verificador "não" é válido
        for i in range(9):
            soma1 += int(cpf_usuario[i]) * (10 - i)
            
        resto = soma1 % 11
        validacao_dig_verificador = 0 if resto < 2 else 11 - resto
        if str(validacao_dig_verificador) != cpf_usuario[9]:
            print("O CPF digitado é invalido. Verifique se os dados estão corretos")
            continue
        
        # Teste para verificar se o 2º digito verificador "não" é válidor
        for i in range(10):
            soma2 += int(cpf_usuario[i]) * (11 - i)
        resto = soma2 % 11
        validacao_dig_verificador = 0 if resto < 2 else 11 - resto
        if str(validacao_dig_verificador) != cpf_usuario[10]:
            print("O CPF digitado é invalido. Verifique se os dados estão corretos")
            continue
        
        #Caso os 2 digitos forem válidos.
        print("O CPF digitado é valido.")
        break
    else:
        print("Entrada inválida. O CPF deve conter apenas números e ter menos de 11 dígitos")