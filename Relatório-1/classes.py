class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def presenca(self):
        print(f'O aluno {self.nome} está presente')

class Professor: 
    def __init__(self, nome, assunto = None):
        self.nome = nome
        self.assunto = assunto
    
    def ministrar_aula(self):
        print(f'O professor {self.nome} está ministrando uma aula sobre {self.assunto}.')
        
class Aula:
    def __init__(self, professor, assunto, alunos=None):
        self.professor = professor
        if alunos is None:
            self.alunos = []
        else:
            self.alunos = [alunos]
        self.assunto = assunto 
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        
    def listar_presenca(self):
        lista_presenca = f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n'
        
        for aluno in self.alunos:
            lista_presenca += f'O aluno {aluno.nome} está presente\n'
        
        return lista_presenca