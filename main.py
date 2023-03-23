from product import ProductAnalyzer
from database import Database
from save_json import writeAJson

db = Database(database="mercado", collection="compras")
db.resetDatabase()

# #Média de gasto por cliente
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$group": {"_id": None, "media": {"$avg": "$total"}}}
# ])
#
# writeAJson(result, "media")
#
# #Produto mais vendido
# result2 = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
#     {"$sort": {"total": -1}},
#     {"$limit": 1}
# ])
#
# writeAJson(result2, "produto_mais_vendido")
#
# #Cliente que mais comprou em cada dia
#
# result3= db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$sort": {"_id.data": 1, "total": -1}},
#     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
# ])
#
# writeAJson(result3, "maior_comprador")

prod = ProductAnalyzer()
prod.db = db
prod.total_gasto()
prod.menos_vendido()
prod.menos_gasto()
prod.maior_que_2()