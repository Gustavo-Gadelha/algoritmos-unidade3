def comprarproduto(comprador, mercadoria):
    pass


def menu_cliente(usuario):
    escolha = -1
    while escolha != 0:
        print('\nMenu do cliente'
              '\n1. Exibir todos os produtos'
              '\n2. Buscar produto'
              '\n3. Comprar produto')

        escolha = int(input('Selecione a opção: '))

        if escolha < 0 or escolha > 2:
            print('Opção invalida')

        elif escolha == 1:
            pass

        elif escolha == 2:
            buscar_produto()

        elif escolha == 3:
            produto = buscar_produto()
            comprarproduto(usuario, produto)
