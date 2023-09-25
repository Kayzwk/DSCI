class Produto:
    def __init__ (self, nome, tipo_unidade, quantidade, preco):
        self.nome=nome
        self.tipo_unidade=tipo_unidade # lt, ml, kg, unidade
        self.quantidade=quantidade # 600 ml
        self._preco=preco
    
    @property #getter
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, vl):
        if isinstance(vl, str):
            valor = vl.replace(' ','')
            valor = float(valor.replace('R$',''))
            self._preco=valor
        else:
            self._preco = vl

    def exibeProduto(self):
        print(f'Produto: {self.nome}')
        print(f'Quantidade: {self.quantidade} {self.tipo_unidade}')
        print(f'Valor: R$ {self.preco:.2f}')

    def venda(self,quantidade):
        print(f'{self.nome} x {quantidade} = R$ {self.preco*quantidade}')

if __name__ == '__main__':
    prod1 = Produto('Coca-Cola','ml',600,6.00)
    prod1.exibeProduto()
    print(type(prod1.preco))
    prod1.preco = 6.00
    prod1.exibeProduto()
    prod1.venda(6)
