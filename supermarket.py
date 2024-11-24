import os
from datetime import datetime

cash_register = {
    'is_open': False,
    'initial_value': 1000.00,
    'current_value': 0.00,
}

SUPERVISOR_PASSWORD = '****'

file_path = os.path.join(os.path.dirname(__file__), 'product_list.txt')

products = [] 

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

def show_subtitle(text):
    '''Exibe o subtítulo'''
    os.system('cls')
    line = '*' * len(text)
    print(line)
    print(text)
    print(line)
    print()

def supervisor_authentication():
    '''Verifica se o usuário é supervisor'''
    password = input('Digite a senha do supervisor: ').strip()
    if password == SUPERVISOR_PASSWORD:
        return True
    else:
        print('Senha incorreta! Operação não autorizada.\n')
        return False

def new_sale():
    '''Executa o processo de uma nova venda'''
    os.system('cls')
    show_subtitle('Nova Venda')
    if not cash_register['is_open'] or cash_register['current_value'] == 0:
        print('Caixa fechado! Abra o caixa para realizar a venda.\n')
        return_to_main_menu()
        return

    total_value = 0.0  
    total = 0  
    add = {}  

    while True:
        cashier = input('Digite o ID do produto, digite 000 para pesquisar ou 999 para remover um item (pressione Enter para finalizar): ').strip()
        if cashier == '000':
            show_products()
            continue

        if cashier == '999':
            if not add:
                print('Nenhum produto adicionado ainda.\n')
                continue

            password = input('Digite a senha de supervisão para continuar: ').strip()
            if password != SUPERVISOR_PASSWORD:
                print('Acesso negado, senha incorreta!')
                continue

            print('\nProdutos adicionados:')
            for i, (name, amount) in enumerate(add.items(),1):
                print(f'{i}. {name} x{amount}')

            try:
                item_to_remove = int(input('\nDigite o número do produto que deseja remover (ou 0 para cancelar): ').strip())
                if item_to_remove == 0:
                    continue

                selected_product_name = list(add.keys())[item_to_remove - 1]
                selected_product = next(product for product in products if product['Nome'] == selected_product_name)

                selected_product['Estoque'] += 1
                total_value -= selected_product['Valor']
                total -= 1
                add[selected_product_name] -= 1 

                if add[selected_product_name] <= 0:
                    del add[selected_product_name]

                    print(f'Produto {selected_product_name} removido com sucesso.\n')
            except(ValueError, IndexError):
                print('Item não encontrado ou inválido.\n')
            continue

        if not cashier:
            break

        product_found = next((product for product in products if product['ID'] == cashier), None)

        if product_found:
            if product_found['Estoque'] > 0:
                product_found['Estoque'] -= 1
                total_value += product_found['Valor']
                total += 1

                add[product_found['Nome']] = add.get(product_found['Nome'], 0) + 1
                os.system('cls')
                print(f'Produto: {product_found['Nome']}')
                print(f'Valor: R${product_found['Valor']:.2f}')
                print(f'Quantidade adicionada: 1')
                print(f'Valor total até agora: R$ {total_value:.2f}\n')
            else:
                print(f'Estoque insuficiente para o produto {product_found['Nome']}.\n')
        else:
            print('ID não encontrado. Tente novamente.\n')

    os.system('cls')
    print('\nResumo de produtos adicionados:')
    for nome, quantidade in add.items():
        print(f'{nome} x{quantidade}')
    print(f'\nTotal de itens adicionados: {total}')
    print(f'Soma total dos valores: R$ {total_value:.2f}')
    return_to_main_menu()

def show_products():
    '''Pesquisar produtos'''
    search = input('Digite o nome do produto (ou pressione Enter para ver todos): ').strip().lower()
    
    
    product_found = [product for product in products if search in product['Nome'].lower()]

    if product_found:
        os.system('cls')
        print('Produtos encontrados:\n')
        for product in product_found:
            print(f'ID: {product['ID']}')
            print(f'Nome: {product['Nome']}')
            print(f'Valor: R${product['Valor']:.2f}')
            print(f'Validade: {product['Validade']}')
            print(f'Garantia: {product['Garantia']}')
            print(f'Estoque: {product['Estoque']}')
            print('-'*30) 
    else:
        print('Produto não encontrado. Tente novamente.\n')

def modify_products():
    '''Adicionar ou alterar um produto'''
    os.system('cls')

    while True:
        print('1 - Adicionar produto')
        print('2 - Alterar produto')
        print('3 - Voltar ao menu principal')
        option = input('Digite a opção desejada: ').strip()

        if option == '1':
            show_subtitle('Adicionar novo produto')
            new_id = str(input('Digite o ID do novo produto: ').strip())
            if any(product['ID'] == new_id for product in products):
                print('ID já existente. Tente novamente.\n')
                continue

            new_name = input('Digite o nome do novo produto: ').strip()
            try:
                new_value = float(input('Digite o valor do novo produto: ').strip())
                new_validity = input('Digite a validade do novo produto (DD/MM/AAAA): ').strip()
                new_warranty = input('Digite a validade do novo produto em meses: ').strip()
                new_stock = int(input('Digite a quantidade em estoque do novo produto: ').strip())

                products.append({
                    'ID': new_id,
                    'Nome': new_name,
                    'Valor': new_value,
                    'Validade': new_validity,
                    'Garantia': f'{new_warranty} meses',
                    'Estoque': new_stock
                    })
                print(f'\nProduto {new_name} adicionado com sucesso.\n')
            except ValueError:
                print('Valores inseridos inválidos. Tente novamente.\n')
            continue

        elif option == '2':
            show_subtitle('Alterar produto existente')
            id_to_change = input('Digite o ID do produto a ser alterado: ').strip()
            product_to_modify = next((product for product in products if product['ID'] == id_to_change), None)

            if not product_to_modify:
                print('Produto não encontrado. Tente novamente.\n')
                continue

            print('\nProduto encontrado:')
            print(f'ID: {product_to_modify['ID']}')
            print(f'Nome: {product_to_modify['Nome']}')
            print(f'Valor: {product_to_modify['Valor']}')
            print(f'Validade: {product_to_modify['Validade']}')
            print(f'Garantia: {product_to_modify['Garantia']}')
            print(f'Estoque: {product_to_modify['Estoque']}')
            print('-'*30)

            print('Alterações disponíveis')
            print('1. Alterar valor')
            print('2. Alterar validade')
            print('3. Alterar garantia')
            print('4. Alterar estoque')
            print('5. Voltar\n')

            modification = input('Escolha o campo que deseja alterar: ').strip()
            try:
                if modification == '1':
                    new_value = float(input('Digite o novo valor: ').strip())
                    product_to_modify['Valor'] = new_value
                    print(f'\nValor do produto {product_to_modify['Nome']} alterado com sucesso.')

                elif modification == '2':
                    new_validity = input('Digite a nova validade (DD/MM/AAAA): ').strip()
                    product_to_modify['Validade'] = new_validity
                    print(f'\nValidade do produto {product_to_modify['Nome']} alterada com sucesso.')
                
                elif modification == '3':
                    new_warranty = input('Digite a nova garantia em meses: ').strip()
                    product_to_modify['Garantia'] = new_warranty
                    print(f'\nGarantia do produto {product_to_modify['Nome']} alterada com sucesso.')

                elif modification == '4':
                    new_stock = input('Digite o novo estoque: ').strip()
                    product_to_modify['Garantia'] = new_stock
                    print(f'\nEstoque do produto {product_to_modify['Nome']} alterado com sucesso.')

                elif modification == '5':
                    continue

                else:
                    print('Opção inválida. Tente novamente.\n')
            except ValueError:
                print('ERRO: Valor fornecido inválido. Tente novamente.\n')

        elif option == '3':
            return_to_main_menu()
        
        else:
            print('Opção inválida. Tente novamente.\n')

def all_products():
    '''Escolher qual sera a interação com os produtos'''
    choose = input('Digite 1 pesquisar produtos ou digite 2 para adicionar ou modificar produtos já cadastrados: ')
    if choose == '1':
        show_products()
    elif choose == '2':
        modify_products()
    else:
        print('Opção inválida.\n')

def generate_expiration_report():
    '''Lógica do relatória por data de validade'''
    try:
        os.system('cls')
        days_to_expire = int(input('Digite quantos dias faltam para o produto expirar: ').strip())
        today = datetime.now()
        matching_products = []
        for product in products:
            try:
                expiration_date = datetime.strptime(product['Validade'],'%d/%m/%Y')
                days_remaining = (expiration_date - today).days
                if days_remaining == days_to_expire:
                    matching_products.append(product)
            except ValueError:
                print('ERRO: Valor fornecido inválido. Tente novamente.\n')
        os.system('cls')
        print(f'\nProdutos que faltam {days_to_expire} dias para expirar:\n')
        if matching_products:
            for product in matching_products:
                print(f'ID: {product['ID']}')
                print(f'Nome: {product['Nome']}')
                print(f'Valor: R${product['Valor']:.2f}')
                print(f'Validade: {product['Validade']}')
                print(f'Estoque: {product['Estoque']}')
                print('-'*30)
        else:
            print('Nenhum produto encontrado com a data de validade informada.\n')
    except ValueError:
        print('ERRO: Quantidade de dias inválida.')
    except Exception as e:
        print(f'ERRO: {e}')
    return_to_main_menu

def generate_amount_report():
    '''Lógica do relatória por quantidade no estoque'''
    try:
        os.system('cls')
        amount = int(input('Digite a quantidade de itens tem o produto: ').strip())
        matching_products = []
        for product in products:
            try:
                if product['Estoque'] == amount:
                    matching_products.append(product)
            except ValueError:
                print('ERRO: Valor fornecido inválido. Tente novamente.\n')
        os.system('cls')
        print(f'\nProdutos com {amount} itens no estoque:\n')
        if matching_products:
            for product in matching_products:
                print(f'ID: {product['ID']}')
                print(f'Nome: {product['Nome']}')
                print(f'Valor: R${product['Valor']:.2f}')
                print(f'Validade: {product['Validade']}')
                print(f'Garantia: {product['Garantia']}')
                print(f'Estoque: {product['Estoque']}')
                print('-'*30)
        else:
            print('Nenhum produto com essa quantidade encontrada.\n')
    except ValueError:
        print('ERRO: Valor fornecido inválido.')
    except Exception as e:
        print(f'ERRO: {e}')
        return_to_main_menu

def report():
    '''Imprime os relatórios'''
    show_subtitle('Relátorios')
    print('Escolha o tipo de relatório que deseja gerar:')
    print('1. Relatório por validade.')
    print('2. Relatório por estoque.')
    print('3. Voltar ao menu principal.')
    option = input('Digite a opção desejada: ')

    if option == '1':
        show_subtitle('Relatório por validade')
        generate_expiration_report()
    elif option == '2':
        show_subtitle('Relatório por estoque')
        generate_amount_report()
    else:
        return_to_main_menu()

def manage_cash_register():
    '''Gerencia o caixa'''
    os.system('cls')
    print('1. Abrir o caixa')
    print('2. Fechar o caixa\n')
    option = input(str('Escolha a opção desejada: '))

    if option == '1':
        open_cash_register()
    elif option == '2':
        close_cash_register()
    else:
        invalid_option()

def open_cash_register():
    '''Abertura do caixa'''
    os.system('cls')
    show_subtitle('Abertura de caixa')
    if supervisor_authentication():
        cash_register['is_open'] = False
        cash_register['current_value'] = cash_register['initial_value']
        print(f'Caixa aberto com sucesso. Valor inicial: R${cash_register['initial_value']:.2f}\n')
    else:
        print('Autenticação de supervisor falhou. Operação não autorizada.\n')
    return_to_main_menu()

def close_cash_register():
    '''Fechamento do caixa'''
    os.system('cls')
    show_subtitle('Fechamento de caixa')
    if supervisor_authentication():
        cash_register['is_open'] = True
        cash_register['current_value'] = 0.00  #pode ser que precise arrumar aqui para o valor do proximo dia ser o mesmo do dia anterior
        print('Caixa fechado com sucesso.\n')
    else:
        print('Autenticação de supervisor falhou. Operação não autorizada.\n')
        return_to_main_menu()

def add_sale_to_cash(value):
    '''Adicionar o valor das vendas ao caixa'''
    if not cash_register['is_open']:
        print('Caixa não está aberto. Abra antes de iniciar as vendas.\n')
        return False
    cash_register['current_value'] += value
    return True

def choose_options():
    '''Lê a entrada do usuário e executa a opção escolhida'''
    try:
        chosen_option = input('Escolha uma opção: ').strip()
        if chosen_option == '1':
            show_subtitle('Nova venda')
            new_sale()
        elif chosen_option == '2':
            show_subtitle('Relatório')
            report()
            return_to_main_menu()
        elif chosen_option == '3':
            show_subtitle('Produtos')
            all_products()
            return_to_main_menu()
        elif chosen_option == '4':
            show_subtitle('Caixa')
            manage_cash_register()
            return_to_main_menu()
        elif chosen_option == '5':
            close_app()
        else:
            invalid_option()
    except Exception as e:
        print(f'Erro: {e}')
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
