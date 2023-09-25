class Produto:
    def __init__ (self, nome, tipo_unidade, quantidade, preco):
        self.nome=nome
        self.tipo_unidade=tipo_unidade # lt, ml, kg, unidade
        self.quantidade=quantidade # 600 ml
        self.preco=preco

    def exibeProduto(self):
        print(f'Produto: {self.nome}')
        print(f'Quantidade: {self.quantidade} {self.tipo_unidade}')
        print(f'Valor: R$ {self.preco:.2f}')

if __name__ == '__main__':
    prod1 = Produto('Coca-Cola','ml',600,6.00)
    prod1.exibeProduto()
    print(type(prod1.preco))
    prod1.preco = 6.00
    prod1.exibeProduto()