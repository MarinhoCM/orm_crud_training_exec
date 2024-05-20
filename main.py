""" Criado por MarinhoCM -> ADS.3 """
from database import *


MESSAGE = """
    +----------------------Mercado------------------------+
    |           O que deseja fazer:                       |
    |               1) Cadastrar                          |
    |               2) Atualizar cadastro                 |
    |               3) Deletar um cadastro                |
    |               4) Mostrar produtos                   |
    +-----------------------------------------------------+
"""

def informacoes_produto() -> list:
    nome_prod = str(input('Digite o nome do produto: ')) 
    qtd_prod = str(input("Digite a quantidade para o produto: "))
    preco_prod = str(input("Digite o valor para o produto: "))
    has_desc = str(input("O produto possui desconto? "))
    if has_desc.lower() in "s":
        desc_prod = int(input("Digite a porcentagem do desconto: "))
        return [nome_prod, qtd_prod, preco_prod, desc_prod]
    return [nome_prod, qtd_prod, preco_prod, 0]

def select_operation(option):
    produtos = Produtos("produtos")

    if option == 1:
        obj_list = informacoes_produto()
        print("inserindo os dados...")
        produtos.insert_in_table(obj_list)
    elif option == 2:
        print("atualizando os dados...")
        product_name = str(input("Digite o nome do produto que deseja atualizar: "))
        print("insira as informações para a atualização...")
        obj_list = informacoes_produto()
        produtos.update_one_in_table(obj_list, product_name)
    elif option == 3:
        product_name = str(input("Digite o nome do produto que deseja deletar: "))
        print("deletando o produto...")
        produtos.delete_one_in_table(product_name)
    elif option == 4:
        produtos.select_all_from_table()

    produtos.close_all()


def main():
    option = int(input(MESSAGE))
    select_operation(option)




if __name__ == "__main__":
    main()