from database import Database

class Queries:
    def __init__(self, db):
        self.db = db

    def query1_1(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc, t.cpf"
        return self.db.execute_query(query)

    def query1_2(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
        return self.db.execute_query(query)

    def query1_3(self):
        query = "MATCH (c:City) RETURN c.name"
        return self.db.execute_query(query)

    def query1_4(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
        return self.db.execute_query(query)

    def query2_1(self):
        query = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS oldest, MAX(t.ano_nasc) AS youngest"
        return self.db.execute_query(query)

    def query2_2(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS average_population"
        return self.db.execute_query(query)

    def query2_3(self):
        query = "MATCH (c:City {cep: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A') AS city_name"
        return self.db.execute_query(query)

    def query2_4(self):
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS char_from_name"
        return self.db.execute_query(query)

if __name__ == "__main__":
    db = Database("bolt://localhost:7687")
    queries = Queries(db)
    print(queries.query1_1())
    print(queries.query1_2())
    print(queries.query1_3())
    print(queries.query1_4())
    print(queries.query2_1())
    print(queries.query2_2())
    print(queries.query2_3())
    print(queries.query2_4())
    db.close()
