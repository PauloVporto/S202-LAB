from pymongo import MongoClient
from bson import ObjectId


class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]


class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

    def to_dict(self):
        return {"nome": self.nome, "documento": self.documento}


class Corrida:
    def __init__(self, nota: float, distancia: float, valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def to_dict(self):
        return {
            "nota": self.nota,
            "distancia": self.distancia,
            "valor": self.valor,
            "passageiro": self.passageiro.to_dict()
        }


class Motorista:
    def __init__(self, nome: str, cnh: str, corridas: list):
        self.nome = nome
        self.cnh = cnh
        self.corridas = corridas

    def to_dict(self):
        return {
            "nome": self.nome,
            "cnh": self.cnh,
            "corridas": [corrida.to_dict() for corrida in self.corridas]
        }


class MotoristaDAO:
    def __init__(self, db: Database):
        self.collection = db.get_collection("Motoristas")

    def create_motorista(self, motorista: dict):
        return self.collection.insert_one(motorista)

    def read_motorista(self, motorista_id: str):
        try:
            return self.collection.find_one({"_id": ObjectId(motorista_id)})
        except Exception as e:
            print(f"Erro ao encontrar motorista: {e}")
            return None

    def update_motorista(self, motorista_id: str, updated_data: dict):
        try:
            return self.collection.update_one({"_id": ObjectId(motorista_id)}, {"$set": updated_data})
        except Exception as e:
            print(f"Erro ao atualizar motorista: {e}")

    def delete_motorista(self, motorista_id: str):
        try:
            return self.collection.delete_one({"_id": ObjectId(motorista_id)})
        except Exception as e:
            print(f"Erro ao deletar motorista: {e}")

# Classe MotoristaCLI para gerenciar a interação via linha de comando
class MotoristaCLI:
    def __init__(self, motorista_dao: MotoristaDAO):
        self.motorista_dao = motorista_dao

    def menu(self):
        while True:
            print("\n1. Criar Motorista")
            print("2. Ler Motorista")
            print("3. Atualizar Motorista")
            print("4. Deletar Motorista")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.create_motorista()
            elif opcao == '2':
                self.read_motorista()
            elif opcao == '3':
                self.update_motorista()
            elif opcao == '4':
                self.delete_motorista()
            elif opcao == '5':
                break
            else:
                print("Opção inválida!")

    def create_motorista(self):
        nome = input("Nome do motorista: ")
        cnh = input("CNH do motorista: ")
        corridas = []
        while True:
            nota = float(input("Nota da corrida: "))
            distancia = float(input("Distância percorrida: "))
            valor = float(input("Valor da corrida: "))
            passageiro_nome = input("Nome do passageiro: ")
            passageiro_doc = input("Documento do passageiro: ")
            passageiro = Passageiro(passageiro_nome, passageiro_doc)
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)
            mais_corrida = input("Adicionar outra corrida? (s/n): ")
            if mais_corrida.lower() != 's':
                break
        motorista = Motorista(nome, cnh, corridas)
        self.motorista_dao.create_motorista(motorista.to_dict())
        print("Motorista criado com sucesso!")

    def read_motorista(self):
        motorista_id = input("Digite o ID do motorista: ")
        motorista = self.motorista_dao.read_motorista(motorista_id)
        if motorista:
            print(f"Motorista encontrado: {motorista}")
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        motorista_id = input("Digite o ID do motorista que deseja atualizar: ")
        nome = input("Novo nome do motorista: ")
        cnh = input("Nova CNH do motorista: ")
        self.motorista_dao.update_motorista(motorista_id, {"nome": nome, "cnh": cnh})
        print("Motorista atualizado com sucesso.")

    def delete_motorista(self):
        motorista_id = input("Digite o ID do motorista que deseja deletar: ")
        self.motorista_dao.delete_motorista(motorista_id)
        print("Motorista deletado com sucesso.")


if __name__ == "__main__":

    uri = "mongodb://localhost:27017"
    db_name = "SistemaDeMotoristas"
    db = Database(uri, db_name)

    motorista_dao = MotoristaDAO(db)
    cli = MotoristaCLI(motorista_dao)
    cli.menu()
