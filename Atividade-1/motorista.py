from typing import List
from corrida import Corrida

class Motorista:
    def __init__(self, nome: str, corridas: List[Corrida] = None, nota: int = 0):
        if corridas is None:
            corridas = []
        self.nome = nome
        self.corridas = corridas
        self.nota = nota