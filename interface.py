import usuariofunc as user
import vendedorfunc as vendor
import clientefunc as client
from gpt import consultarchatgpt


def menu_acesso(escolha=-1):
    while escolha != 0:
        print('\nMenu de acesso',
              '\n1. Cadastrar usuário',
              '\n2. Acessar Menu do cliente',
              '\n3. Acessar Menu do vendedor'
              '\n4. Redefinir senha',
              '\n0. Fechar o programa')

        escolha = int(input('\nSelecione a opção: '))

        if escolha < 0 or escolha > 4:
            print('Opção invalida!')

        elif escolha == 1:
            user.cadastrar_usuario()

        elif escolha == 2:
            usuario = user.autenticar_login()
            if usuario is not None:
                print('\nAcesso liberado!')
                menu_cliente(usuario)

        elif escolha == 3:
            usuario = user.autenticar_login()
            if usuario is not None:
                print('\nAcesso liberado!')
                menu_vendedor(usuario)

        elif escolha == 4:
            user.recuperar_senha()


def menu_vendedor(usuario, escolha=-1):
    while escolha != 0:
        print('\nMenu do vendedor - Saldo: {}'.format(usuario["saldo"]),
              '\n1. Cadastrar produto',
              '\n2. Buscar produto',
              '\n3. Remover produto',
              '\n4. Atualizar preço do produto',
              '\n5. Exportar produtos para arquivo txt',
              '\n6. Ler arquivo txt do vendedor'
              '\n7. Plotar grafico de produtos e quantidades'
              '\n0. Voltar para o menu de acesso')

        escolha = int(input('\nSelecione a opção: '))

        if escolha < 0 or escolha > 7:
            print('Opção invalida!')

        elif escolha == 1:
            vendor.cadastrar_produto(usuario)

        elif escolha == 2:
            vendor.buscar_produto(usuario)

        elif escolha == 3:
            vendor.remover_produto(usuario)

        elif escolha == 4:
            vendor.alterar_valor(usuario)

        elif escolha == 5:
            vendor.exportar_txt(usuario)

        elif escolha == 6:
            vendor.ler_txt(usuario)

        elif escolha == 7:
            vendor.plotar_grafico(usuario)


def menu_cliente(usuario, escolha=-1):
    while escolha != 0:
        print('\nMenu do cliente - Saldo: {}'.format(usuario["saldo"]),
              '\n1. Comprar produto',
              '\n2. Listar histórico de compras',
              '\n3. Consultar o ChatGPT',
              '\n4. Fazer deposito',
              '\n5. Fazer Saque',
              '\n0. Voltar para o menu de acesso')

        escolha = int(input('\nSelecione a opção: '))

        if escolha < 0 or escolha > 5:
            print('Opção invalida')

        elif escolha == 1:
            client.comprar_produto(usuario)

        elif escolha == 2:
            client.exibir_historico(usuario)

        elif escolha == 3:
            consulta = str(input('Digite o nome do produto: '))
            consultarchatgpt(consulta)

        elif escolha == 4:
            deposito = float(input('Digite o valor do deposito: '))
            while not client.depositar(usuario, deposito):
                deposito = float(input('Digite o valor do deposito novamente: '))

        elif escolha == 5:
            saque = float(input('Digite o valor do saque: '))
            while not client.sacar(usuario, saque):
                saque = float(input('Digite o valor do saque novamente: '))


menu_acesso()
