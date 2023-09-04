def informacoes(**kwargs):

    for dado, valor in kwargs.items():
        print(f"'{dado}':'{valor}'")
if __name__ == '__main__':
    informacoes(nome='Tiago')
    informacoes(nome='Tiago',acao='teste')
    informacoes(nome='Tiago',acao='teste',ip='192.168.1.1')