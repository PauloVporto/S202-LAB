from database import Database
from helper.write_a_json import writeAJson
from product_analyzer import ProductAnalyzer

db = Database(database="mercado", collection="produtos")
#db.resetDatabase()

product_analyzer = ProductAnalyzer()

total_sales_per_day = product_analyzer.total_sales_per_day()
writeAJson(total_sales_per_day, "Total de vendas por dia")

most_sold_product = product_analyzer.most_sold_product()
writeAJson(most_sold_product, "Produto mais vendido")

customer_highest_spending = product_analyzer.customer_highest_spending()
writeAJson(customer_highest_spending, "Cliente que mais gastou em uma única compra")

products_sold_above_quantity = product_analyzer.products_sold_above_quantity()
writeAJson(products_sold_above_quantity, "Produtos vendidos acima de 1 unidade")