from bancodedados import *
from vendedorfunc import exibir_produto


def depositar(usuario, valor):
    if valor >= 0:
        usuario['saldo'] += valor
        return True

    else:
        print('O valor depositado deve ser maior ou igual a 0')
        return False


def sacar(usuario, valor):
    if valor <= usuario['saldo']:
        usuario['saldo'] -= valor
        return True

    else:
        print('Saldo insuficiente')
        return False


def retornar_vendedor(produto):
    for vendedor in bancodedados:
        if produto in vendedor['produtos']:
            return vendedor


def buscar_tudo():
    escolha = int(input('\nDigite 1 para pesquisar pelo nome ou 2 para pesquisar pela descrição: '))
    while escolha != 1 and escolha != 2:
        escolha = int(input('Opção inválida, digite novamente: '))

    semelhantes = list()
    if escolha == 1:
        nome_busca = str(input('Digite o nome do produto: '))

        for vendedor in bancodedados:
            for produto in vendedor['produtos']:
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
        descript_busca = str(input('Digite a descrição do produto: '))

        for vendedor in bancodedados:
            for produto in vendedor['produtos']:
                if produto['descrição'] == descript_busca:
                    print('Produto encontrado!')
                    exibir_produto(produto)
                    return produto

                if produto['descrição'].find(descript_busca) >= 0:
                    semelhantes.append(produto)

        else:
            print('Produto não encontrado!')
            if len(semelhantes) > 0:
                print('Veja resultados semelhantes:')
                for produto in semelhantes:
                    exibir_produto(produto)


def comprar_produto(usuario):
    produto = buscar_tudo()

    if produto is not None:
        escolha = str(input('Deseja mesmo comprar esse produto? [s/n]: '))
        while escolha.upper() != 'S' and escolha.upper() != 'N':
            escolha = str(input('Opção inválida, digite novamente [s/n]: '))

        if escolha.upper() == 'S':
            if produto in usuario['produtos']:
                print('Usuários não podem comprar seus próprios produtos!!!')
                return

            quantidade_compra = int(input('Digite a quantidade que deseja comprar: '))
            while quantidade_compra <= 0 or quantidade_compra > produto['quantidade']:
                quantidade_compra = int(input('Valor inválido! Digite novamente: '))

            vendedor = retornar_vendedor(produto)
            valor_compra = produto['valor'] * quantidade_compra
            if sacar(usuario, valor_compra):
                produto['quantidade'] -= quantidade_compra
                if produto['quantidade'] == 0:
                    vendedor['produtos'].remove(produto)

                depositar(vendedor, valor_compra)
                anexar_ao_historico(usuario, produto, quantidade_compra, valor_compra)
                print('Compra realizada com sucesso!')

    else:
        print('Não foi possível comprar produtos!')


def anexar_ao_historico(usuario, produto, quantidade, valor):
    usuario['historico'].append(f"{quantidade} unidade(s) de {produto['nome']} por R$ {valor:<6.2f}")


def exibir_historico(usuario):
    if not usuario['historico'] == []:
        print('Historico de compras: ')
        for compra in usuario['historico']:
            print(compra)

    else:
        print('Nenhuma compra no histórico')
