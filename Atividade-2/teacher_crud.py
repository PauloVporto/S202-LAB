from database import Database

class TeacherCRUD:
    def __init__(self, db):
        self.db = db

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t"
        parameters = {"name": name}
        return self.db.execute_query(query, parameters)

    def update(self, name, new_cpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $new_cpf RETURN t"
        parameters = {"name": name, "new_cpf": new_cpf}
        return self.db.execute_query(query, parameters)

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

if __name__ == "__main__":
    db = Database("bolt://localhost:7687", "neo4j", "password")
    teacher_crud = TeacherCRUD(db)
    teacher_crud.create("Chris Lima", 1956, "189.052.396-66")
    print(teacher_crud.read("Chris Lima"))
    teacher_crud.update("Chris Lima", "162.052.777-77")
    print(teacher_crud.read("Chris Lima"))
    teacher_crud.delete("Chris Lima")
    db.close()
