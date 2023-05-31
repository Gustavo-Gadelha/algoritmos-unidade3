def cadastrarusuario(bancodedados):
    email = str(input('Digite o seu e-mail: '))
    senha = str(input('Digite a sua senha: '))

    for vendedor in bancodedados:
        while vendedor['email'] == email or vendedor['senha'] == senha:
            print('Email ou senha já estão sendo usados!')
            email = str(input('Digite outro e-mail: '))
            senha = str(input('Digite outra senha: '))

    nome = str(input('Digite o seu nome: '))

    cadastro = {'email': email,
                'senha': senha,
                'nome': nome,
                'produtos': [],
                'saldo': 0,
                'token': None}

    bancodedados.append(cadastro)
    print('Cadastro do usuário realizado com sucesso!')


def autenticarlogin(login, senha, bancodedados):
    for usuario in bancodedados:
        if usuario['email'] == login and usuario['senha'] == senha:
            print('\nVocê deseja acessar como:'
                  '\n1. Cliente'
                  '\n2. Vendedor')

            escolha = int(input('\nDigite sua escolha: '))
            while escolha != 1 and escolha != 2:
                escolha = int(input('Valor invalido, digite novamente: '))

            if escolha == 1:
                usuario['token'] = 'cliente'

            elif escolha == 2:
                usuario['token'] = 'vendedor'

            return usuario

    else:
        return False


def recuperarsenha(bancodedados):
    email = str(input('Digite o seu e-mail: '))

    for usuario in bancodedados:
        if usuario['email'] == email:
            usuario['senha'] = str(input('Digite a sua nova senha: '))
            print('Senha atualizada com sucesso!')
            break

    else:
        print('E-mail não encontrado!')
