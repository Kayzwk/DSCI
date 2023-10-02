class Pessoa():
    def __init__(self, nome, data_nascimento, cor):
        self.nome=nome
        self.data_nascimento=data_nascimento
        self.cor=cor

class Aluno(Pessoa):
    def __init__(self, ra, cod_curso, ano_entrada, campus, periodo, nome, data_nascimento, cor):
        self.ra=ra
        self.cod_curso=cod_curso
        self.ano_entrada= ano_entrada
        self.campus=campus
        self.periodo=periodo
        super().__init__(nome, data_nascimento, cor)

    def exibeAluno(self):
        print(f"Aluno: {self.nome}")
        print(f"Data nascimento: {self.data_nascimento}")
        print(f"RA: {self.ra}")
        print(f"Código do Curso: {self.cod_curso}")
        print(f"Ano entrada: {self.ano_entrada}")
        print(f"Período: {self.periodo}")
        print(f"Campus: {self.campus}")

if __name__ == '__main__':
    tiago = Aluno(142715,'CECAD045',2020,'Goiânia',7,"Davi Silveira Gama Braga",'19/04/2004','Branca')
    tiago.exibeAluno()