import usuariofunc as user
import produtofunc as product
import clientefunc as client


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
        user.cadastrar_usuario()

    elif escolha == 2:
        usuario = user.autenticar_login()

        if usuario:
            if usuario['token'] == 'cliente':
                print('Acesso liberado!')
                client.menu_cliente(usuario)

            elif usuario['token'] == 'vendedor':
                print('Acesso liberado!')
                product.menu_vendedor(usuario)

        else:
            print('E-mail ou senha invalidos!')

    elif escolha == 3:
        user.recuperar_senha()
