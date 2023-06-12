from datetime import datetime
current_dateTime = datetime.now()


def exportar_txt(usuario):
    with open(f"logs/produtos_{usuario['email']}.txt", 'a') as txt:
        txt.write(f'[{current_dateTime}]\n')
        for produto in usuario['produtos']:
            texto = f"COD: {produto['codigo']:0>3} - Nome: {produto['nome']:<16} - " \
                    f"Valor: R$ {produto['valor']:<6.2f} - Quantidade: {produto['quantidade']:0>3}"

            txt.write(f'{texto}\n')

        else:
            txt.close()


def ler_txt(usuario):
    # Observação: Causa erro se não houver documento txt
    txt = open(f"logs/produtos_{usuario['email']}.txt", 'r')

    for linha in txt.readlines():
        print(linha, end='')

    txt.close()
