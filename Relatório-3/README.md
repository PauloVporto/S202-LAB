# Querys MQL

> Bancos de dados relacionais utilizam do SQL como linguagem para estruturação, manipulação e consulta de dados. O MongoDB usa da linguagem MongoDB Query Language (MQL).

### Referências:

[**[ 1 ]**](https://docs.mongodb.com/compass/current/query/filter/) Guia para a query bar do *Compass* (tem até comparação com SQL e *Aggregation*)

[**[ 2 ]**](https://docs.mongodb.com/manual/tutorial/query-documents/) Guia para querys em diversos *drivers* (bibliotecas de MongoDB em várias linguagens)

**[[ 3 ]](https://docs.mongodb.com/manual/reference/operator/query/)** Guia dos operadores para FILTER e PROJECT

**[[ 4 ]](https://account.mongodb.com/account/login?nds=true)** Link rápido para o Atlas

---

# *Query Bar* no Compass

Vamos dar uma olhada no que significa cada um desses campos.


- **FILTER**: filtra os documentos utilizando regras e operações (semelhante ao WHERE do SQL),
- **PROJECT**: especifica quais campos do documento serão apresentados (tipo quando escolhemos as colunas no SELECT),
- **SORT**: permite que a consulta seja ordenada com base em um critério (tipo o ORDER BY),
- **COLLATION**: especifica regras para lidar com uma língua específica,
- **MAX TIME MS**: estabelece um tempo limite (em milisegundos) para a operação ser concluída,
- **SKIP**: pula um determinado número de documentos do resultado (não serão apresentados),
- **LIMIT**: define um número máximo de documentos a serem retornados,
- **RESET**: limpa todos os campos anteriores.

---

# Praticando

Bora ver na prática como funciona a busca de documentos no Python?

## Arquivo database.py

```python
from typing import Collection
import pymongo # pip install pymongo
from dataset.pokemon_dataset import dataset

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try: 
            self.db.drop_collection(self.collection)
            self.collection.insert_many(dataset)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)
```

## Arquivo writeAJson.py

 

```python
import json
import os
from bson import json_util # pip install bson

def writeAJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./json"):
        os.makedirs("./json")
        

    with open(f"./json/{name}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))
```

## Arquivo main.py

```python
from database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()
```

### Todos os pokémons

```python
pokemons = db.collection.find()
```

### Pokémon por nome

```python
def getPokemonByName(name: str):
    return db.collection.find({"name": name})

pikachu = getPokemonByName("Pikachu")
writeAJson(pikachu, "pikachu")
```

### Pokémons por tipo

```python
def getPokemonsByType(types: list):
    return db.collection.find({"type": {"$in": types}})

types = ["Fighting"]
pokemons = getPokemonsByType(types)

writeAJson(pokemons, "pokemons_by_type")
```

### Pokémons tipo grama OU veneno que tem evolução

```python
tipos = ["Grass", "Poison"]
pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })
```

### Pokémons fracos contra psíquico E gelo

```python
fraquezas = ["Psychic", "Ice"]
pokemons = db.collection.find({"weaknesses": {"$all": fraquezas}})
```

### Pokémons que tem APENAS uma fraqueza

```python
pokemons = db.collection.find({"weaknesses": {"$size": 1})
```

### Pokémons que tem chance de *spawn* ENTRE 0.3 e 0.6

```python
pokemons = db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
```

### Pokémons que NÃO tem o campo *multipliers* ou ele é *None*/*null*

```python
pokemons = db.collection.find({"multipliers": None})
```

### Pokémons SEM o campo *multipliers*

```python
pokemons = db.collection.find({"multipliers": {"$exists": False}})
```

### Pokémons que a segunda evolução aparece ATÉ o #021 da pokédex

```python
pokemons = db.collection.find({"next_evolution.1.num": {"$lte": "020"}
```

### Pokémons que são de fogo OU fracos contra fogo

```python
pokemons = db.collection.find({"$or": [{"type":"Fire"},{"weaknesses": "Fire"}]})
```

<aside>
💡 **Lembrem-se:** as querys apresentadas muito provavelmente não são a única maneira de se obter os mesmos resultados. Nem as formas mais otimizadas.

</aside>

Todas as querys feitas em python podem ser feitas no compass ou Atlas de forma muito semelhante.

Veremos na próxima aula outras opções de tratamento das querys em python (PROJECT, SORT, LIMIT, SKIP, etc) sobre o conceito de **aggregation pipelines**.

---