from bancodedados import *


def cadastrar_usuario():
    email = str(input('Digite seu e-mail: '))
    senha = str(input('Digite sua senha: '))
    nome = str(input('Digite seu nome: '))

    while email == '' or email in [user['email'] for user in bancodedados]:
        email = str(input('E-mail inválido! Digite seu e-mail novamente: '))
    while senha == '' or senha in [user['senha'] for user in bancodedados]:
        senha = str(input('Senha inválida! Digite sua senha novamente: '))
    while nome == '':
        nome = str(input('O campo "nome" não foi preenchido! Digite o seu nome: '))

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

    for usuario in bancodedados:
        if usuario['email'] == email:
            nova_senha = str(input('Digite a sua nova senha: '))
            while nova_senha == '' or nova_senha in [user['senha'] for user in bancodedados]:
                nova_senha = str(input('A senha não foi preenchida! Digite sua senha: '))

            else:
                usuario['senha'] = nova_senha
                print('Senha atualizada com sucesso!')
                break

    else:
        print('E-mail não encontrado!')
