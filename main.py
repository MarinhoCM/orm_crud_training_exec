""" Criado por MarinhoCM -> ADS.3 """

from database import *

MENU = """
        +----------------------Mercado------------------------+
        |           O que deseja fazer:                       |
        |               1) Cadastrar                          |
        |               2) Atualizar cadastro                 |
        |               3) Deletar um cadastro                |
        |               4) Mostrar produtos                   |
        +-----------------------------------------------------+
"""


def informacoes_produto() -> list:
    nome_prod = str(input("\tDigite o nome do produto: "))
    qtd_prod = str(input("\tDigite a quantidade para o produto: "))
    preco_prod = str(input("\tDigite o valor para o produto: "))
    has_desc = str(input("\tO produto possui desconto? "))
    if has_desc.lower() in "s":
        desc_prod = int(input("\tDigite a porcentagem do desconto: "))
        return [nome_prod, qtd_prod, preco_prod, desc_prod]
    return [nome_prod, qtd_prod, preco_prod, 0]


def select_operation(option):
    produtos = Shop("shop")

    if option == 1:
        obj_list = informacoes_produto()
        print("\tinserindo os dados...")
        produtos.insert_in_table(obj_list)
    elif option == 2:
        product_name = str(input("\tDigite o nome do produto que deseja atualizar: "))
        print("\tinsira as informações para a atualização...")
        obj_list = informacoes_produto()
        print("\tatualizando os dados...")
        produtos.update_one_in_table(obj_list, product_name)
    elif option == 3:
        product_name = str(input("\tDigite o nome do produto que deseja deletar: "))
        print("\tdeletando o produto...")
        produtos.delete_one_in_table(product_name)
    elif option == 4:
        produtos.select_all_from_table()

    produtos.close_all()


def main():
    loop_control = True
    while loop_control:
        option = int(input(MENU + "\n\t------> "))
        select_operation(option)
        stop = str(input("\tDeseja continuar? [s/n]: "))
        loop_control = False if "n" in stop.lower() else True

    print("\tEncerrando o sistema...")

if __name__ == "__main__":
    main()
