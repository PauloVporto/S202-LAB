from motorista import Motorista
from passageiro import Passageiro
from corrida import Corrida

class MotoristaCLI:
    def __init__(self, motorista_dao):
        self.motorista_dao = motorista_dao

    def menu(self):
        while True:
            print("=== Menu ===")
            print("1. Criar motorista")
            print("2. Ler motorista")
            print("3. Atualizar motorista")
            print("4. Deletar motorista")
            print("5. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.criar_motorista()
            elif escolha == "2":
                self.ler_motorista()
            elif escolha == "3":
                self.atualizar_motorista()
            elif escolha == "4":
                self.deletar_motorista()
            elif escolha == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    def criar_motorista(self):
        nome_motorista = input("Digite o nome do motorista: ")
        nota_motorista = int(input("Digite a nota do motorista: "))

        nome_passageiro = input("Digite o nome do passageiro: ")
        documento_passageiro = input("Digite o documento do passageiro: ")

        nota_corrida = int(input("Digite a nota da corrida: "))
        distancia_corrida = float(input("Digite a distância da corrida: "))
        valor_corrida = float(input("Digite o valor da corrida: "))

        passageiro = Passageiro(nome_passageiro, documento_passageiro)
        corrida = Corrida(nota_corrida, distancia_corrida, valor_corrida, passageiro)

        corridas = [corrida]

        motorista = Motorista(nome_motorista, corridas, nota_motorista)
        
        self.motorista_dao.criar_motorista(motorista, corridas)

        print("Motorista criado com sucesso!")

    def ler_motorista(self):
        nome_motorista = input("Digite o nome do motorista: ")
        motorista = self.motorista_dao.ler_motorista(nome_motorista)
        if motorista:
            print(f"Nome: {motorista.nome}")
            print(f"Nota: {motorista.nota}")
            print("Corridas:")
            for corrida in motorista.corridas:
                print(f"Nota: {corrida.nota}, Distância: {corrida.distancia}, Valor: {corrida.valor}, Passageiro: {corrida.passageiro.nome}")
        else:
            print("Motorista não encontrado.")

    def atualizar_motorista(self):
        nome_motorista = input("Digite o nome do motorista: ")
        nova_nota = int(input("Digite a nova nota do motorista: "))
        motorista = Motorista(nome_motorista, nota=nova_nota)
        self.motorista_dao.atualizar_motorista(motorista)
        print(f"Motorista {nome_motorista} atualizado com sucesso.")

    def deletar_motorista(self):
        nome_motorista = input("Digite o nome do motorista que deseja deletar: ")
        self.motorista_dao.deletar_motorista(nome_motorista)
        print(f"Motorista {nome_motorista} deletado com sucesso.")
