from funcionario.funcionario import Funcionario

class ControleDeBonificacoes:

    __slots__ = ['_total']

    def __init__(self, total = 0):
        self._total = total

    # registra - incrementa as bonificações dos funcionários
    def registra(self, obj):
        # verifica se obj é uma instância de funcionário
        if(isinstance(obj, Funcionario)):
            self._total += obj.get_bonificacao()
        else:
            print(f'Instância de {self.__class__.__name__} não impementa o método get_bonificacao()')
    @property
    def total(self):
        return self._total
