from inventory_report.inventory.product import Product
from datetime import date

id = 100
nome_do_produto = "Teia do Miranha"
nome_da_empresa = "Empresa de teias do Miranha"
data_de_fabricacao = date.today()
data_de_validade = date.today()
numero_de_serie = "3574819230"
instrucoes_de_armazenamento = "Cuidado que gruda"


def my_product_report():
    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    report = (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )

    return report


def test_relatorio_produto():
    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert product.__repr__() == my_product_report()
