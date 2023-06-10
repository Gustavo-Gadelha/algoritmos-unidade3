cod = 0


def cadastrar_produto(usuario):
    global cod
    nomeproduto = str(input('Digite o nome do produto: '))

    valorproduto = float(input('Digite o valor do produto: '))
    while valorproduto <= 0:
        valorproduto = float(input('O valor do produto deve ser maior que zero! Digite novamente: '))

    quantidade = int(input('Digite a quantidade de produto: '))
    while quantidade <= 0:
        quantidade = int(input('O quantidade deve ser um número maior que zero! Digite novamente: '))

    descript = str(input('Digite uma descrição do produto(ou aperte ENTER para ignorar): '))

    cod += 1
    produto = {'codigo': cod,
               'nome': nomeproduto,
               'valor': valorproduto,
               'quantidade': quantidade,
               'descrição': descript}

    usuario['produtos'].append(produto)
    print('Produto cadastrado com sucesso!')


def exibir_produto(produto):
    print(f"COD: {produto['codigo']:0>3} - "
          f"Nome: {produto['nome']:<16} - "
          f"Valor: R$ {produto['valor']:<10.2f} - "
          f"Quantidade: {produto['quantidade']:0>3} - ", end="")

    if not produto['descrição'] == '':
        print(f"Descrição do produto: {produto['descrição']}")
    else:
        print("Produto sem descrição!")


def buscar_produto(usuario):
    op = int(input('Digite 1 para pesquisar pelo nome ou 2 para pesquisar pelo codigo: '))
    while op != 1 and op != 2:
        op = int(input('Opção inválida, digite novamente: '))

    if op == 1:
        nome = str(input('Digite o nome do produto: '))
        semelhantes = list()

        for produto in usuario['produtos']:
            if produto['nome'].find(nome) >= 0:
                semelhantes.append(produto)

                if produto['nome'] == nome:
                    print('\nProduto encontrado!')
                    exibir_produto(produto)
                    return produto

        else:
            print('\nProduto não encontrado!')
            if len(semelhantes) > 0:
                print('Veja resultados semelhantes:')
                for produto in semelhantes:
                    exibir_produto(produto)

    elif op == 2:
        codigo = int(input('Digite o codigo do produto: '))

        for produto in usuario['produtos']:
            if produto['codigo'] == codigo:
                print('\nProduto encontrado!')
                exibir_produto(produto)
                return produto

        else:
            print('\nProduto não encontrado!')


def alterar_valor(usuario):
    produto = buscar_produto(usuario)
    if produto:
        produto['valor'] = float(input('Digite o novo valor do produto: '))
        while produto['valor'] <= 0:
            produto['valor'] = float(input('O valor do produto deve ser maior que zero! Digite novamente: '))

        print('Valor do produto alterado com sucesso!')

    else:
        print('\nNenhum valor alterado!')


def remover_produto(usuario):
    produto = buscar_produto(usuario)
    if produto:
        usuario['produtos'].remove(produto)
        print('Produto removido com sucesso!')

    else:
        print('\nNenhum produto removido!')


def menu_vendedor(usuario):
    while True:
        print('\nMenu do vendedor',
              '\n1. Cadastrar produto',
              '\n2. Buscar produto',
              '\n3. Remover produto',
              '\n4. Atualizar preço do produto',
              '\n0. Voltar para o menu de acesso')

        escolha = int(input('\nSelecione a opção: '))

        if escolha < 0 or escolha > 4:
            print('Opção invalida!')

        elif escolha == 0:
            break

        elif escolha == 1:
            cadastrar_produto(usuario)

        elif escolha == 2:
            buscar_produto(usuario)

        elif escolha == 3:
            remover_produto(usuario)

        elif escolha == 4:
            alterar_valor(usuario)
