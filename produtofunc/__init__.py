def exibirproduto(produto):
    print(f'Codigo: {produto[0]:0>3} - '
          f'Nome: {produto[1]:<12}\t'
          f'Quantidade: {produto[2]:<4}\t'
          f'Valor: R$ {produto[3]:<10.2f}')


def buscar_produto_do_vendedor(usuario):
    pesquisa = str(input('Digite o nome do produto: '))
    semelhantes = []

    for produto in usuario['produtos']:
        if produto[1].find(pesquisa) >= 0:
            semelhantes.append(produto)

            if produto[1] == pesquisa:
                semelhantes.clear()
                print('Produto encontrado!')
                exibirproduto(produto)
                return produto

    else:
        print('Produto não encontrado!')
        if len(semelhantes) > 0:
            print('Veja resultados semelhantes:')
            for produto in semelhantes:
                exibirproduto(produto)

        semelhantes.clear()


def menuproduto(usuario):
    escolha = -1
    while escolha != 0:
        print('\nMenu de produtos',
              '\n1. Cadastrar produto',
              '\n2. Buscar produto',
              '\n3. Remover produto',
              '\n4. Atualizar preço do produto',
              '\n0. Voltar para o menu de acesso')

        escolha = int(input('\nSelecione a opção: '))

        if escolha < 0 or escolha > 4:
            print('Opção invalida!')

        elif escolha == 1:
            codigo = len(usuario['produtos']) + 1
            nomeproduto = str(input('Digite o nome do produto: '))
            quantidade = int(input('Digite a quantidade de produto: '))
            valor = float(input('Digite o valor do produto: '))
            while valor <= 0:
                valor = float(input('O valor do produto deve ser maior que zero! Digite novamente: '))

            usuario['produtos'].append([codigo, nomeproduto, quantidade, valor])
            print('Produto cadastrado com sucesso!')

        elif escolha == 2:
            buscar_produto_do_vendedor(usuario)

        elif escolha == 3:
            produto = buscar_produto_do_vendedor(usuario)
            if produto:
                usuario['produtos'].remove(produto)
                print('Produto removido com sucesso!')

        elif escolha == 4:
            produto = buscar_produto_do_vendedor(usuario)
            if produto:
                produto[3] = float(input('Digite o novo valor do produto: '))
                while produto[3] <= 0:
                    produto[3] = float(input('O valor do produto deve ser maior que zero! Digite novamente: '))
