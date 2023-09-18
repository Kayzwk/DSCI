class Aluno:
    nome_ifg = 'Instituto Federal de Goiás'
    def __init__ (self, nome, ra):
        self.nome = nome
        self.ra = ra
    #metodo de classe
    def exibeAluno (self):
        return f'Nome: {self.nome} RA: {self.ra}'

class SalaAula:
    def __init__ (self, nomeSala, maxAlunos):
        self.nomeSala = nomeSala
        self.maxAlunos = maxAlunos
        self.listaAlunos = []

    def InserirAluno(self,aluno):
        if len(self.listaAlunos) < self.maxAlunos and not aluno in self.listaAlunos:
            self.listaAlunos.append(aluno)

    def ExibeSala (self):
        n = 1
        for aluno in self.listaAlunos:
            print(f'{n} - {aluno.exibeAluno()}')
            n = n +1


if __name__ == '__main__':
    POO = SalaAula('POO', 5)
    aluno = Aluno('Davi Silveira','20222010700121')
    POO.InserirAluno(aluno)
    aluno = Aluno('Guilherme Bandeira','20222010700598')
    POO.InserirAluno(aluno)
    aluno = Aluno('Kaylane Lima','20222010700548')
    POO.InserirAluno(aluno)
    aluno = Aluno('Miguel Borges','20222010500658')
    POO.InserirAluno(aluno)
    aluno = Aluno('Rafael Alcantra','20222010400659')
    POO.InserirAluno(aluno)
    aluno = Aluno('Yan Rodrigues','20222010600789')
    POO.InserirAluno(aluno)
    POO.ExibeSala()
