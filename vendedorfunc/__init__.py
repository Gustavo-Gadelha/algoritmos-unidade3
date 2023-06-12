import matplotlib.pyplot as plt
cod = 0


def cadastrar_produto(usuario):
    nomeproduto = str(input('Digite o nome do produto: '))
    valorproduto = float(input('Digite o valor do produto: '))
    quantidade = int(input('Digite a quantidade de produto: '))
    descript = str(input('Digite uma descrição do produto(ou aperte ENTER para ignorar): '))

    while nomeproduto == '':
        nomeproduto = str(input('O nome do produto não foi preenchido! Digite o nome do produto: '))
    while valorproduto <= 0:
        valorproduto = float(input('O valor do produto deve ser maior que zero! Digite novamente: '))
    while quantidade <= 0:
        quantidade = int(input('A quantidade deve ser maior que zero! Digite novamente: '))

    global cod
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
          f"Valor: R$ {produto['valor']:<6.2f} - "
          f"Quantidade: {produto['quantidade']:0>3} - ", end="")

    if not produto['descrição'] == '':
        print(f"Descrição do produto: {produto['descrição']}")
    else:
        print("Produto sem descrição!")


def buscar_produto(usuario):
    escolha = int(input('\nDigite 1 para pesquisar pelo nome ou 2 para pesquisar pelo codigo: '))
    while escolha != 1 and escolha != 2:
        escolha = int(input('Opção inválida, digite novamente: '))

    if escolha == 1:
        nome_busca = str(input('Digite o nome do produto: '))
        semelhantes = list()

        for produto in usuario['produtos']:
            if produto['nome'] == nome_busca:
                print('Produto encontrado!')
                exibir_produto(produto)
                return produto

            if produto['nome'].find(nome_busca) >= 0:
                semelhantes.append(produto)

        else:
            print('Produto não encontrado!')
            if len(semelhantes) > 0:
                print('Veja resultados semelhantes:')
                for produto in semelhantes:
                    exibir_produto(produto)

    elif escolha == 2:
        codigo_busca = int(input('Digite o codigo do produto: '))

        for produto in usuario['produtos']:
            if produto['codigo'] == codigo_busca:
                print('Produto encontrado!')
                exibir_produto(produto)
                return produto

        else:
            print('Produto não encontrado!')


def alterar_valor(usuario):
    produto = buscar_produto(usuario)
    if produto is not None:
        produto['valor'] = float(input('Digite o novo valor do produto: '))
        while produto['valor'] <= 0:
            produto['valor'] = float(input('O valor do produto deve ser maior que zero! Digite novamente: '))

        print('Valor do produto alterado com sucesso!')

    else:
        print('Nenhum valor alterado!')


def remover_produto(usuario):
    produto = buscar_produto(usuario)
    if produto is not None:
        usuario['produtos'].remove(produto)
        print('Produto removido com sucesso!')

    else:
        print('Nenhum produto removido!')


def exportar_txt(usuario):
    with open(f"logs/produtos_{usuario['email']}.txt", 'a') as txt:
        for produto in usuario['produtos']:
            texto = f"COD: {produto['codigo']:0>3} - Nome: {produto['nome']:<16} - " \
                    f"Valor: R$ {produto['valor']:<6.2f} - Quantidade: {produto['quantidade']:0>3}"

            txt.write(f'{texto}\n')

        else:
            txt.close()


def ler_txt(usuario):
    txt = open(f"logs/produtos_{usuario['email']}.txt", 'r')

    for linha in txt.readlines():
        print(linha, end='')

    txt.close()


def plotar_grafico(usuario):
    produtos = list(produto['nome'] for produto in usuario['produtos'])
    quantidades = list(produto['quantidade'] for produto in usuario['produtos'])

    plt.figure(figsize=(10, 5))
    plt.bar(produtos, quantidades, color='maroon', width=0.4)
    plt.xlabel('Produtos')
    plt.ylabel('Quantidade')
    plt.title('Gráfico')
    plt.show()
