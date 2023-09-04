def exibe(*args):
    """Função recebera uma lista de parametro e sera exibido cada parametro passado"""
    for parametro in args:
        print(f'Parametro: {parametro}')

if __name__ == '__main__':
    exibe('Tiago')
    exibe('Tiago','Teste')
    exibe('Tiago','Teste',1)