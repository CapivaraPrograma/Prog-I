# Programa para verificar se a senha de um usuário de um usuário.
while True:
    nome_usuario = input("Digite o seu usuário: ")
    senha_usuario = input("Digite a sua senha: ")
    if nome_usuario == senha_usuario:
        print("A senha não pode ser igual ao nome de usuário.")
    else:
        print("O seu usuário e senha foram cadastrados.")
        break