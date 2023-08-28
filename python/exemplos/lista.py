alunos=[]
for aluno in range (1, 4):
    nome_aluno = input('Digite o nome do {}º aluno: '.format(aluno))
    alunos.append(nome_aluno)
print('\nLista de alunos:')
for idx in alunos:
    print('{}'.format(idx))

alunos.reverse()
print('\nLista de alunos reversa:')
for idx in alunos:
    print('{}'.format(idx))

alunos.sort()
print('\nOrdenando em ordem alfabética:')
for idx in alunos:
    print('{}'.format(idx))