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
                    return produto, vendedor

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
                    return produto, vendedor

                if produto['descrição'].find(descript_busca) >= 0:
                    semelhantes.append(produto)

        else:
            print('Produto não encontrado!')
            if len(semelhantes) > 0:
                print('Veja resultados semelhantes:')
                for produto in semelhantes:
                    exibir_produto(produto)


def comprar_produto(usuario):
    produto, vendedor = buscar_tudo()

    if produto is not None and vendedor is not None:
        escolha = str(input('Deseja mesmo comprar esse produto? [s/n]: '))
        while escolha.upper() != 'S' and escolha.upper() != 'N':
            escolha = str(input('Opção inválida, digite novamente [s/n]: '))

        if escolha.upper() == 'S':
            if produto in usuario['produtos']:
                print('Usuários não podem comprar seus próprios produtos!!!')
                return None

            unidades = int(input('Digite quantas unidades deseja comprar: '))
            while unidades <= 0 or unidades > produto['quantidade']:
                unidades = int(input('Valor inválido! Digite novamente: '))
            else:
                custo = produto['valor'] * unidades

            if sacar(usuario, custo):
                produto['quantidade'] -= unidades
                if produto['quantidade'] == 0:
                    vendedor['produtos'].remove(produto)

                depositar(vendedor, custo)
                anexar_ao_historico(usuario, produto, unidades, custo)
                print('Compra realizada com sucesso!')

    else:
        print('Não foi possível comprar produtos!')


def anexar_ao_historico(usuario, produto, unidades, valor):
    usuario['historico'].append(f"Compra de {unidades} unidade(s) de {produto['nome']} por R$ {valor:<6.2f}")


def exibir_historico(usuario):
    if not usuario['historico'] == []:
        print('Historico de compras: ')
        for compra in usuario['historico']:
            print(compra)

    else:
        print('Nenhuma compra no histórico')
