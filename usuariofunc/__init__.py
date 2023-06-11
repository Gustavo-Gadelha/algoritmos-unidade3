from bancodedados import *


def cadastrar_usuario():
    email = str(input('Digite seu e-mail: '))
    senha = str(input('Digite sua senha: '))
    nome = str(input('Digite seu nome: '))

    while email == '':
        email = str(input('O e-mail não foi preenchido! Digite seu e-mail: '))
    while senha == '':
        senha = str(input('A senha não foi preenchida! Digite sua senha: '))
    while nome == '':
        nome = str(input('O nome não foi preenchido! Digite o seu nome: '))

    for usuario in bancodedados:
        while usuario['email'] == email:
            email = str(input('Esse e-mail já está sendo usado! Digite outro e-mail: '))
        while usuario['senha'] == senha:
            senha = str(input('Essa senha já está sendo usada! Digite outra senha: '))

    cadastro = {'email': email,
                'senha': senha,
                'nome': nome,
                'produtos': [],
                'saldo': 0,
                'historico': [],
                'token': None}

    bancodedados.append(cadastro)
    print('Cadastro de usuário realizado com sucesso!')


def autenticar_login():
    login = str(input('Digite o seu e-mail: '))
    senha = str(input('Digite a sua senha: '))

    for usuario in bancodedados:
        if usuario['email'] == login and usuario['senha'] == senha:
            print('\nVocê deseja acessar como:'
                  '\n1. Cliente'
                  '\n2. Vendedor')

            escolha = int(input('\nDigite sua escolha: '))

            while escolha != 1 and escolha != 2:
                escolha = int(input('Opção inválida, digite novamente: '))

            if escolha == 1:
                usuario['token'] = 'cliente'

            elif escolha == 2:
                usuario['token'] = 'vendedor'

            return usuario


def recuperar_senha():
    email = str(input('Digite o seu e-mail: '))

    # OBSERVAÇÃO: Através dessa função o usuario pode colocar uma senha que já está em uso, CONSERTE ISSO!
    for usuario in bancodedados:
        if usuario['email'] == email:
            usuario['senha'] = str(input('Digite a sua nova senha: '))
            while usuario['senha'] == '' or usuario['senha']:
                usuario['senha'] = str(input('A senha não foi preenchida! Digite sua senha: '))

            print('Senha atualizada com sucesso!')
            break

    else:
        print('E-mail não encontrado!')
