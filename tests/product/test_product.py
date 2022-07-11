from inventory_report.inventory.product import Product
from datetime import date

id = 100
nome_do_produto = "Teia do Miranha"
nome_da_empresa = "Empresa de teias do Miranha"
data_de_fabricacao = date.today()
data_de_validade = date.today()
numero_de_serie = "3574819230"
instrucoes_de_armazenamento = "Cuidado que gruda"


def my_product():
    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )
    return product


def test_cria_produto():
    product = my_product()
    assert product.id == id
    assert product.nome_do_produto == nome_do_produto
    assert product.nome_da_empresa == nome_da_empresa
    assert product.data_de_fabricacao == str(data_de_fabricacao)
    assert product.data_de_validade == str(data_de_validade)
    assert product.numero_de_serie == numero_de_serie
    assert product.instrucoes_de_armazenamento == instrucoes_de_armazenamento
