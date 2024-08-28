from database import Database
from collections import defaultdict

class ProductAnalyzer:
    def __init__(self, database="mercado", collection="produtos"):
        self.db = Database(database=database, collection=collection)

    def total_sales_per_day(self):
        pipeline = [
            {"$group": {"_id": "$data_compra", "total_sales": {"$sum": {"$size": "$produtos"}}}}
        ]
        return list(self.db.collection.aggregate(pipeline))

    def most_sold_product(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_sold": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_sold": -1}},
            {"$limit": 1}
        ]
        return list(self.db.collection.aggregate(pipeline))

    def customer_highest_spending(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_spent": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_spent": -1}},
            {"$limit": 1}
        ]
        return list(self.db.collection.aggregate(pipeline))

    def products_sold_above_quantity(self, quantity_threshold=1):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": quantity_threshold}}},
            {"$group": {"_id": "$produtos.descricao", "total_sold": {"$sum": "$produtos.quantidade"}}}
        ]
        return list(self.db.collection.aggregate(pipeline))