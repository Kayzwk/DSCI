


def imc(**kwargs):
    """
        Função para calcular o imc:
        parametros:
        peso:
        altura:
        retorno: imc
    
    """
    # python imc.py 64 1.93
    usage="""
    Parametros obrigatorios:
    imc(peso=64,altura=1.93)
    """

    if 'peso' not in kwargs:
        print(usage)
        return
    
    if 'altura' not in kwargs:
        print(usage)
        return
    
    peso=kwargs['peso']
    altura=kwargs['altura']

    imc = peso/(altura**2)

    #print(f'O imc é: %.2f'%imc)
    print(f'O imc é: {imc:.2f}')
    return imc

if __name__ == '__main__':
    peso = int(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    vimc = imc (peso = peso, altura = altura)
    print('-'*40)
    if vimc <= 18:
        print('Desnutrido')
    if 18 < vimc < 25:
        print('Adequado')
    if vimc >= 25:
        print('Obeso')
        