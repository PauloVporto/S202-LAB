# Aggregation Pipelines

### Referências:

**[[ 1 ]](https://docs.mongodb.com/manual/reference/method/js-collection/)** Guia completo de métodos de Coleções (`find()`, `insert()`, `remove()`, `update()`, etc)

**[[ 2 ]](https://docs.mongodb.com/manual/reference/method/js-cursor/)** Guia completo de métodos de *Cursors* (objetos que são retornados do `find()` de Coleções)

**[[ 3 ]](https://www.w3schools.com/python/python_mongodb_getstarted.asp)** Guia básico sobre o PyMongo

**[[ 4 ]](https://docs.mongodb.com/manual/core/aggregation-pipeline/)** Introdução básica sobre o conceito de aggregation pipeline

[**[ 5 ]**](https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/) Guia completo de todos os pipeline **stages** de uma aggregation 

[**[ 6 ]**](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) Guia completo de **expressões** em aggregations

**[[ 7 ]](https://docs.mongodb.com/manual/reference/operator/aggregation/)** Guia completo de todos os **operadores** para aggregations

[**[ 8 ]**](https://docs.mongodb.com/manual/reference/sql-aggregation-comparison/) Comparação entre o SELECT do SQL e aggregations 🌟

[**[ 9 ]**](https://docs.mongodb.com/manual/reference/sql-comparison/) Breve comparação entre conceitos do SQL e do MongoDB 🌟

[**[ 10 ]**](https://docs.mongodb.com/manual/tutorial/aggregation-with-user-preference-data/) Exemplo 1 do uso de aggregations — Users collection 🌟

[**[ 11 ]**](https://docs.mongodb.com/manual/tutorial/aggregation-zip-code-data-set/) Exemplo 2 do uso de aggregations — Zip Code (CEP estadunidense) collection 🌟

---

# Como funciona

A aggregation pipeline do MongoDB é formada por ***stages*** (etapas). Cada etapa transforma os documentos a medida que eles caminham pela pipeline. Essas etapas não precisam obrigatoriamente produzir um novo documento: podem, por exemplo, apenas contar os documentos `$count`, ordená-los `$sort`, filtrá-los `$match`, entre outras funções.

<aside>
💡 Utilizem os links de referência no topo dessa página! Os links marcados com 🌟 eu considerei bem legais para aprender.

</aside>

Stages podem aparecer várias vezes numa pipeline, com exceção de `$out`, `$merge`, `$geoNear` .

### Pipeline Expressions

Alguns stages usam uma expressão como operando. As expressões de pipeline especificam a transformação a ser aplicada aos documentos de entrada. Cada expressão tem uma estrutura de documento e pode conter outra expressão.

Expressões de pipeline podem operar apenas no documento atual no pipeline e não podem se referir a dados de outros documentos.

Geralmente, as expressões não têm estado e são avaliadas apenas quando vistas pelo processo de aggregation, com uma exceção: expressões de [**acumulação**](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-accumulator-operators). 

Os operadores de acumulação, usados no stage `$group`, mantêm seu estado (por exemplo, totais, máximos, mínimos e dados relacionados) à medida que os documentos caminham na pipeline.

---

## Arquivo main.py

```jsx
from database import Database
from writeAJson import writeAJson

db = Database(database="mercado", collection="produtos")
db.resetDatabase()
```

## Média de gasto por cliente:

1. **`$unwind: "$produtos"`**: Este estágio "desmonta" a matriz "produtos" em cada documento da coleção, para que cada produto apareça em seu próprio documento, com seus valores correspondentes para "quantidade", "preco" etc. Isso é necessário para permitir a agregação de dados por produto ou por cliente, por exemplo.
2. **`$group: {_id: "$cliente_id", total: {$sum: {$multiply: ["$produtos.quantidade", "$produtos.preco"]}}}}`**: Este estágio agrupa os documentos com base no campo "cliente_id" e calcula o valor total de compras para cada cliente, multiplicando a "quantidade" de cada produto pelo seu respectivo "preco" e somando esses valores. O resultado da agregação é um conjunto de documentos que incluem o ID do cliente e o total de suas compras.
3. **`$group: {_id: null, media: {$avg: "$total"}}`**: Este estágio agrupa todos os documentos resultantes do estágio anterior em um único documento (usando o ID nulo) e calcula a média do campo "total" em todos eles. O resultado é um único documento com a média do valor total de compras para todos os clientes na coleção.

```python
db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
])

```

## Produto mais vendido:

1. **`$unwind: "$produtos"`** - esse estágio descontrói o array de produtos e cria um novo documento para cada produto dentro do array. Isso significa que, se houver vários produtos em um documento, serão criados vários documentos para cada produto, cada um com uma cópia dos outros campos do documento original.
2. **`$group: {_id: "$produtos.descricao", total: {$sum: "$produtos.quantidade"}}`** - esse estágio agrupa os documentos pelo campo "produtos.descricao" e, em seguida, soma as quantidades de cada produto com o operador **`$sum`**, armazenando o resultado na variável "total".
3. **`$sort: {total: -1}`** - esse estágio ordena os documentos resultantes em ordem decrescente de "total", para que o produto mais vendido apareça em primeiro lugar.
4. **`$limit: 1`** - esse estágio limita a saída a apenas um documento, que é o primeiro na ordem estabelecida pelo estágio de classificação. Nesse caso, esse documento representa o produto mais vendido.

```python
db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}
])
```

## Cliente que mais comprou em cada dia:

1. **`$unwind: "$produtos"`**: Desconstrói o array "produtos" para que possa ser agregado de forma individual.
2. **`$group: {_id: {cliente: "$cliente_id", data: "$data_compra"}, total: {$sum: {$multiply: ["$produtos.quantidade", "$produtos.preco"]}}}}`**: Agrupa os documentos com base na combinação do cliente e da data da compra e calcula o total de cada compra.
3. **`$sort: {"_id.data": 1, total: -1}}`**: Ordena os documentos em ordem crescente da data da compra e em ordem decrescente do total de cada compra.
4. **`$group: {_id: "$_id.data", cliente: {$first: "$_id.cliente"}, total: {$first: "$total"}}`**: Agrupa novamente os documentos por data da compra e retorna o primeiro cliente e o primeiro total de cada grupo, que serão os maiores valores para cada data da compra.

```python
db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"_id.data": 1, "total": -1}},
    {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
])
```