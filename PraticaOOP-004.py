class Aluno:

    def __init__(self, nome, matricula, nota1, nota2):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        if self.media() >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

aluno1 = Aluno('Wally', 123, 7, 9)
print(aluno1.media())
print(aluno1.situacao())