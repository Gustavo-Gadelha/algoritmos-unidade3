from projetorene import bancodedados
from produtofunc import exibirproduto


def buscar_produto_por_cliente():
    pesquisa = str(input('Digite o nome do produto: '))
    semelhantes = []

    for usuario in bancodedados:
        for produto in usuario['produtos']:
            if produto[1].find(pesquisa) >= 0:
                semelhantes.append(produto)

                if produto[1] == pesquisa:
                    semelhantes.clear()

                    exibirproduto(produto)
                    return produto

    else:
        print('Produto não encontrado!')
        if len(semelhantes) > 0:
            for produto in semelhantes:
                exibirproduto(produto)

        semelhantes.clear()


def comprarproduto(comprador, mercadoria):
    pass


def menucliente(usuario):
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
            buscar_produto_por_cliente()

        elif escolha == 3:
            produto = buscar_produto_por_cliente()
            comprarproduto(usuario, produto)