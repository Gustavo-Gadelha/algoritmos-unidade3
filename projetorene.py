import usuariofunc as uf
import produtofunc as pf
import clientefunc as cf

bancodedados = [{'email': 'login',
                 'senha': 'senha',
                 'nome': 'teste',
                 'produtos': [[1, 'carro', 1, 10],
                              [2, 'camisa', 2, 20],
                              [3, 'chapeu', 3, 30],
                              [4, 'banana', 4, 40]]
                 }]

escolha = -1
while escolha != 0:
    print('\nMenu de acesso',
          '\n1. Cadastrar usuário',
          '\n2. Fazer Login',
          '\n3. Redefinir senha',
          '\n0. Fechar o programa')

    escolha = int(input('\nSelecione a opção: '))

    if escolha < 0 or escolha > 3:
        print('Opção invalida!')

    elif escolha == 1:
        uf.cadastrarusuario(bancodedados)

    elif escolha == 2:
        login = str(input('Digite o seu e-mail: '))
        senha = str(input('Digite a sua senha: '))
        usuario = uf.autenticarlogin(login, senha, bancodedados)

        if usuario['token'] == 'cliente':
            print('Acesso liberado!')

        elif usuario['token'] == 'vendedor':
            print('Acesso liberado!')
            pf.menuproduto(usuario)

        else:
            print('E-mail ou senha invalidos!')

    elif escolha == 3:
        uf.recuperarsenha(bancodedados)

    elif escolha == 4:
        pass
