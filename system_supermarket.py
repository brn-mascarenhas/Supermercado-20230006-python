import os


file_path = r'C:/Users/gomes\Desktop/Nova pasta/product_list.txt' #base de dados do mercado

products = [] #lista para armazenar os produtos como dicionarios

with open(file_path,'r', encoding = 'utf-8') as file:
    next(file)
    for line in file:
        columns = line.strip().split('|')
        if len(columns) >= 6:
            product = {
                'ID': columns[1].strip(),
                'Nome': columns[2].strip(),
                'Valor': columns[3].strip(),
                'Validade': columns[4].strip(),
                'Garantia': columns[5].strip(),
                'Estoque': columns[6].strip(),
            }
            products.append(product)

                
'''Essa função é responsavel por exibir o titulo do programa'''
def show_program_name():      
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
      '''Essa função é responsavel por exibir as opçoes de entrada no menu principal'''
      print('1. Nova venda')
      print('2. Relatório')
      print('3. Produtos')
      print('4. Caixa')
      print('''5. Sair
            ''')

def close_app():
    '''Essa função é responsavel por fechar o aplicativo''' 
    show_subtitle('🅕 🅘 🅝 🅐 🅛 🅘 🅩 🅐 🅝 🅓 🅞  🅐 🅟 🅟')
    input('\nDigite uma tecla para sair: ')
    exit()

def return_to_main_menu():
    '''Essa função é responsavel por voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu princial: ')
    main()

def invalid_option():
     '''Essa função é responsavel por exibir uma mensagem e voltar ao menu principal caso o usuario escolha uma opçao invalida'''
     print('Opção Invalida!\n')
     return_to_main_menu()

def show_subtitle(texto):
     '''Essa função é responsavel por exibir o subtitulo'''
     os.system('cls')
     linha = '*' * (len(texto))
     print(linha)
     print(texto)
     print(linha)
     print()


def show_products():
    for product in products:
        print(product)



def choose_options():
    '''Essa função é responsalve por escolher uma opcao de entrada'''
    try:
        chosen_option = str(input('Escolha uma opção:'))
        if chosen_option == '1':
            new_sale()
        elif chosen_option == '2':
            show_report()
        elif chosen_option == '3':
            show_products()
        elif chosen_option == '4':
            chashier()
        elif chosen_option == '5':
            close_app()
        else:
            invalid_option()
    except:
        invalid_option()
        


def main():
    '''Essa função é responsavel por armazenar todas as ações que terao no menu principal'''
    os.system('cls')
    show_program_name()
    show_options()
    choose_options()

if __name__ == '__main__':
    main()

#for product in products: #imprimir na tela para testes
    #print(product)
