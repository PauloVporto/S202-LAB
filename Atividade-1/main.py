from database import Database
from motoristaDAO import MotoristaDAO
from cli import MotoristaCLI
from motorista import Motorista
from passageiro import Passageiro
from corrida import Corrida

def main():
    db = Database("atlas-cluster", "usuarios")

    motorista_dao = MotoristaDAO(db)

    motorista_cli = MotoristaCLI(motorista_dao)

    motorista_cli.menu()

    db.disconnect()
if __name__ == "__main__":
    main()
