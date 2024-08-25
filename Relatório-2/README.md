# BSON & Collection


# Comparação SQL x MongoDB

Sabemos que os registros são as **unidades básicas de dados** em bancos relacionais. No caso do MongoDB, essas unidades básicas são os documentos, reunidos em coleções de um banco.

Comparação entre as unidades de dados de bancos relacionais e bancos não relacionais

Esses documentos são estruturados e entendidos pelo MongoDB como **[BSONs](https://www.mongodb.com/json-and-bson)** — *Binary JSON*. Vamos aprender o que é JSON e porque o BSON foi desenvolvido.

Veremos também as diferenças entre as tabelas (relacionais) e coleções (não relacionais).

---

# JSON

*JavaScript Object Notation*, mais conhecido como JSON, é uma estrutura associativa onde uma chave de texto é associada a um valor. Esse valor pode ser um número, uma string, um array, uma função ou até outro objeto.


Devido a facilidade de representar objetos JavaScript em texto, ser entendível tanto para humanos quanto máquinas e simples de implementar em outras linguagens, o JSON foi escolhido para o modelo de orientação a documentos do MongoDB.

Porém, haviam alguns problemas:

1. JSON é um formato baseado em texto, ou seja, sua análise sintática é lenta (*text parsing*).
2. JSON toma muito espaço devido à legibilidade para humanos.
3. JSON suporta um número limitado de tipos de dados básicos.

Para sanar esses obstáculos, o BSON foi inventado. 

---

# BSON

Representação binária para guardar dados no formato JSON. Otimizado para velocidade, espaço e flexibilidade. A estrutura binária do BSON **codifica as informações de tipo e comprimento**, o que permite que sejam analisadas muito mais rapidamente. Além disso, oferece suporte a outros tipos de dados mais completos.

---

# JSON *vs* BSON

Com certeza ambos são muito semelhantes. A principal diferença entre eles é o suporte a tipos de dados mais sofisticados pelo BSON. A linguagem JavaScript não diferencia números inteiros e números de ponto flutuante, por exemplo.

---

# Flexibilidade

Um dos grandes atrativos para desenvolvedores que usam bancos com modelos de dados JSON e BSON é o esquema dinâmico e flexível que eles fornecem quando comparados aos modelos de dados tabulares rígidos utilizados por bancos relacionais.

- Documentos JSON são **polimórficos** - os campos podem variar de documento para documento em uma única coleção.
- Não há necessidade de declarar a estrutura dos documentos no banco de dados — os documentos são **autodescritivos**.
- Se um novo campo precisar ser adicionado a um documento, ele poderá ser criado sem afetar todos os outros documentos da coleção e sem colocar o banco de dados offline.

---

# Collection

Uma coleção é um agrupamento de documentos. É o equivalente a uma tabela em um sistema de banco de dados relacional.

## Relacionamentos [🖇️](https://docs.mongodb.com/manual/applications/data-models-relationships/)

Quando o assunto é relacionamento entre entidades, o MongoDB consegue trabalhar com eficiência em relacionamentos 1️⃣↔️1️⃣ e 1️⃣↔️Ⓜ️. Para isso, podemos utilizar duas estratégias:

### *Embedded Documents*

Nessa abordagem, os relacionamentos são estruturados utilizando objetos embutidos em outros numa mesma *collection*.

```json
{
   _id: "joe",
   name: "Joe Bookreader",
   address: {
              street: "123 Fake Street",
              city: "Faketon",
              state: "MA",
              zip: "12345"
            }
}
```

```python
{
    "nome": "Bruno",
    "shoppingCart": [
        {
            "id": 1,
            "name": "Xbox",
            "price": 1000.0,
            "quantity": 1
        },
        {
            "id": 2,
            "name": "Batata",
            "price": 20.0,
            "quantity": 2
        },
        {
            "id": 3,
            "name": "Coca-Cola",
            "price": 5.0,
            "quantity": 3
        }
    ]
}
```

### *Document References*

Nessa estratégia, os relacionamentos são estruturados por referências a objetos entre diferentes *collections*. Parecido com o que vemos nos bancos relacionais.

```json
// collection *movie*

{
  "_id": 1,
  "title": "The Arrival of a Train",
  "year": 1896,
  "runtime": 1,
  "released": ISODate("1896-01-25"),
  "type": "movie",
  "directors": [ "Auguste Lumière", "Louis Lumière" ],
  "countries": [ "France" ],
  "genres": [ "Documentary", "Short" ],
}
```

```json
// collection *movie_details*

{
  "_id": 156,
  "movie_id": 1, // referência para a collection movie
  "poster": "http://ia.media-imdb.com/images/M/MV5BMjEyNDk5MDYzOV5BMl5BanBnXkFtZTgwNjIxMTEwMzE@._V1_SX300.jpg",
  "plot": "A group of people are standing in a straight line along the platform of a railway station, waiting for a train, which is seen coming at some distance. When the train stops at the platform, ...",
  "fullplot": "A group of people are standing in a straight line along the platform of a railway station, waiting for a train, which is seen coming at some distance. When the train stops at the platform, the line dissolves. The doors of the railway-cars open, and people on the platform help passengers to get off.",
  "lastupdated": ISODate("2015-08-15T10:06:53"),
  "imdb": {
    "rating": 7.3,
    "votes": 5043,
    "id": 12
  },
  "tomatoes": {
    "viewer": {
      "rating": 3.7,
      "numReviews": 59
    },
    "lastUpdated": ISODate("2020-01-29T00:02:53")
  }
}
```

<aside>
💡 Relacionamentos do tipo Ⓜ️↔️Ⓜ️ podem ser trabalhados no MongoDB, mas geralmente não é uma boa prática. Essa opção não aparece nem mesmo na [**documentação**](https://docs.mongodb.com/manual/applications/data-models-relationships/) oficial.

</aside>

### ⚠️ Importante

A estruturação dos relacionamentos depende muito da sua aplicação. Quais dados serão buscados? Quantas *querys* serão necessárias? A tendência é que as buscas mais frequentes exijam menos poder computacional.

---