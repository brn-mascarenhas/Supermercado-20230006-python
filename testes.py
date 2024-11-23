import os

file_path = r'product_list.txt'  # Base de dados do mercado

products = []  # Lista para armazenar os produtos como dicionários

with open(file_path, 'r', encoding='utf-8') as file:
    next(file)
    for line in file:
        columns = line.strip().split('|')
        if len(columns) >= 6:
            product = {
                'ID': str(columns[1].strip()),
                'Nome': columns[2].strip(),
                'Valor': float(columns[3].strip()),
                'Validade': columns[4].strip(),
                'Garantia': columns[5].strip(),
                'Estoque': int(columns[6].strip()),
            }
            products.append(product)


def show_program_name():
    '''Exibe o título do programa'''
    print('''
███╗░░░███╗███████╗██████╗░░█████╗░░█████╗░██████╗░██╗███╗░░░███╗  ██████╗░░█████╗░
████╗░████║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║████╗░████║  ██╔══██╗██╔══██╗
██╔████╔██║█████╗░░██████╔╝██║░░╚═╝███████║██║░░██║██║██╔████╔██║  ██║░░██║██║░░██║
██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██╗██╔══██║██║░░██║██║██║╚██╔╝██║  ██║░░██║██║░░██║
██║░╚═╝░██║███████╗██║░░██║╚█████╔╝██║░░██║██████╔╝██║██║░╚═╝░██║  ██████╔╝╚█████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░░░░╚═╝  ╚═════╝░░╚════╝░

███╗░░░███╗░█████╗░██╗░░░░░███████╗░█████╗░░██████╗
████╗░████║██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔════╝
██╔████╔██║███████║██║░░░░░█████╗░░███████║╚█████╗░
██║╚██╔╝██║██╔══██║██║░░░░░██╔══╝░░██╔══██║░╚═══██╗
██║░╚═╝░██║██║░░██║███████╗██║░░░░░██║░░██║██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░
''')


def show_options():
    '''Exibe as opções do menu principal'''
    print('1. Nova venda')
    print('2. Relatório')
    print('3. Produtos')
    print('4. Caixa')
    print('5. Sair\n')


def close_app():
    '''Fecha o aplicativo'''
    show_subtitle('🅕 🅘 🅝 🅐 🅛 🅘 🅩 🅐 🅝 🅓 🅞  🅐 🅟 🅟')
    input('\nDigite uma tecla para sair: ')
    exit()


def return_to_main_menu():
    '''Volta ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()


def invalid_option():
    '''Exibe uma mensagem e volta ao menu principal para opções inválidas'''
    print('Opção Inválida!\n')
    return_to_main_menu()


def show_subtitle(texto):
    '''Exibe o subtítulo'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def new_sale():
    '''Executa o processo de uma nova venda'''
    total_value = 0.0  # Soma dos valores
    quantidade_total = 0  # Quantidade total dos produtos
    adicionados = {}  # Produtos adicionados

    while True:
        cashier = input("Digite o ID do produto (ou pressione Enter para finalizar): ").strip()
        if not cashier:  # Sai do loop se o ID for vazio
            break

        # Busca produto pelo ID
        produto_encontrado = next((product for product in products if product['ID'] == cashier), None)

        # Exibe resultado se o produto for encontrado
        if produto_encontrado:
            if produto_encontrado['Estoque'] > 0:
                produto_encontrado['Estoque'] -= 1
                total_value += produto_encontrado['Valor']
                quantidade_total += 1

                # Atualiza o registro de produtos adicionados
                adicionados[produto_encontrado['Nome']] = adicionados.get(produto_encontrado['Nome'], 0) + 1

                print(f"Produto: {produto_encontrado['Nome']}")
                print(f"Quantidade adicionada: 1")
                print(f"Valor total até agora: R$ {total_value:.2f}\n")
            else:
                print(f"Estoque insuficiente para o produto {produto_encontrado['Nome']}.\n")
        else:
            print("ID não encontrado. Tente novamente.\n")

    # Exibe o resumo final
    print("\nResumo de produtos adicionados:")
    for nome, quantidade in adicionados.items():
        print(f"{nome} x{quantidade}")
    print(f"\nTotal de itens adicionados: {quantidade_total}")
    print(f"Soma total dos valores: R$ {total_value:.2f}")
    return_to_main_menu()


def show_products():
    '''Exibe todos os produtos'''
    for product in products:
        print(product)


def choose_options():
    '''Lê a entrada do usuário e executa a opção escolhida'''
    try:
        chosen_option = input('Escolha uma opção: ').strip()
        if chosen_option == '1':
            new_sale()
        elif chosen_option == '2':
            show_subtitle('Relatório')
            # Implementar a função de relatório
            return_to_main_menu()
        elif chosen_option == '3':
            show_subtitle('Produtos')
            show_products()
            return_to_main_menu()
        elif chosen_option == '4':
            show_subtitle('Caixa')
            # Implementar a função de caixa
            return_to_main_menu()
        elif chosen_option == '5':
            close_app()
        else:
            invalid_option()
    except Exception as e:
        print(f"Erro: {e}")
        invalid_option()


def main():
    '''Exibe o menu principal e gerencia as ações'''
    while True:
        os.system('cls')
        show_program_name()
        show_options()
        choose_options()


if __name__ == '__main__':
    main()
