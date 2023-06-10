import usuariofunc as uf
import produtofunc as pf
import clientefunc as cf

bancodedados = [{'email': 'login',
                 'senha': 'senha',
                 'nome': 'teste',
                 'produtos': [{'codigo': 1, 'nome': 'camisa', 'valor': 10, 'quantidade': 3, 'descrição': 'Branca'},
                              {'codigo': 2, 'nome': 'chapeu', 'valor': 15, 'quantidade': 5, 'descrição': 'Vermelho'},
                              {'codigo': 3, 'nome': 'sapato', 'valor': 25, 'quantidade': 2, 'descrição': ''},
                              {'codigo': 4, 'nome': 'sandália', 'valor': 5, 'quantidade': 1, 'descrição': 'Fruta'}],
                 'saldo': 0,
                 'token': None
                 }]

while True:
    print('\nMenu de acesso',
          '\n1. Cadastrar usuário',
          '\n2. Fazer Login',
          '\n3. Redefinir senha',
          '\n0. Fechar o programa')

    escolha = int(input('\nSelecione a opção: '))

    if escolha < 0 or escolha > 3:
        print('Opção invalida!')

    elif escolha == 0:
        break

    elif escolha == 1:
        uf.cadastrar_usuario(bancodedados)

    elif escolha == 2:
        login = str(input('Digite o seu e-mail: '))
        senha = str(input('Digite a sua senha: '))
        usuario = uf.autenticar_login(bancodedados, login, senha)

        if usuario:
            if usuario['token'] == 'cliente':
                print('Acesso liberado!')
                cf.menu_cliente(usuario)

            elif usuario['token'] == 'vendedor':
                print('Acesso liberado!')
                pf.menu_vendedor(usuario)

        else:
            print('E-mail ou senha invalidos!')

    elif escolha == 3:
        uf.recuperar_senha(bancodedados)
