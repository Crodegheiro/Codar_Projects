import json
class Alunos:
    id = 1
    def __init__(self, nome, g1, g2, g3, resultado = ""):
        self.id = Alunos.id
        Alunos.id +=1
        self.nome= nome
        self.g1= g1
        self.g2= g2
        self.g3= g3
        self.resultado = resultado

    def calcular(self,):
        resultado = (self.g1+ self.g2+self.g3)/3
        self.resultado = resultado

    def imprimir(self):
        print(f"Aluno= {self.nome}")
        print(f"Nota G1= {self.g1}")
        print(f"Nota G2= {self.g2}")
        print(f"Nota G3= {self.g3}")
        print(f"Nota Final= {self.resultado}")
    
    def to_json(self):
        return json.dumps(self.__dict__)