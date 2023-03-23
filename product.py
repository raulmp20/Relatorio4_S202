from database import Database
from save_json import writeAJson


class ProductAnalyzer:
    db = None
    def __int__(self, db):
        db = Database(database="mercado", collection="compras")
        pass

    def total_gasto(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "B",
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        ])
        writeAJson(result, 'total_gasto')

    def menos_vendido(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": 1}},
            {"$limit": 1},
        ])
        writeAJson(result, 'menos_vendido')

    def menos_gasto(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": 1}},
            {"$limit": 1},
        ])
        writeAJson(result, 'menos_gasto')

    def maior_que_2(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$match":{"total": {"$gt": 2}}},
            {"$sort": {"total": 1}},
        ])
        writeAJson(result, 'maior_que_2')

