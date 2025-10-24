

## Programação com Acesso a Banco de Dados
# Revisão de Orientação a Objetos
# Prof. Guilherme Leal Santos & João Gabriel dos Santos :p

# from conta import Conta
# from cliente import Cliente
# from empresa.config.database import SupabaseConnection
# from funcionario.controle_de_bonificacoes import ControleDeBonificacoes
# from funcionario.funcionario import Funcionario
# from funcionario.gerente import Gerente
#from ifrn.pessoa import Pessoa
# import ifrn
# Aula 17/10 - Polimorfismo, Classes Abstratas, SupaBase

# client = SupabaseConnection().client

# pessoa = Pessoa('Guilherme', '111.222.333-44')
# print(pessoa)

# f = ifrn.Funcionario('Guilherme', '111.222.333-44', '1886519')
# print(f)

# f = Funcionario('Bartô Galeno', '111.222.333-44', 50000)
# print(f.get_bonificacao())
# print(f)
# g = Gerente('Reginaldo Rossi', '777.222.333-88', 250000, 1234, 10)
# print(g.get_bonificacao())
# print(g)

# controle = ControleDeBonificacoes()
# controle.registra(f)
# controle.registra(g)
# print(f'Total = R$ {controle.total:.2f}')

# Aula 10/10 - Métodos estáticos, métodos de classe
# Herança e Reescrita de métodos

#cliente1 = Cliente('Elvis Presley', '111.222.333-44')
#conta1 = Conta(cliente1, 1, 123, 'elvis@gmail.com', 10000)
#print(Conta.total_contas())
#cliente2 = Cliente('Jonhny Cage', '222.333.444-55')
#conta2 = Conta(cliente2, 2, 234, 'jonhny@outlook.com', 5000)
#print(Conta.total_contas())

#print(Conta.lista_contas()[0].saldo)
#print(Conta.lista_contas()[1].saldo)

#print(Conta.get_saldo_total())

#print(Conta.total_contas_cm())


# Aula 26/09 - Agregação, Composição Modificadores de Acesso
'''
cliente1 = Cliente('Elvis Presley', '111.222.333-44')
conta1 = Conta(cliente1, 1, 123, 'elvis@gmail.com', 10000)
conta1._saldo = 1
conta1.extrato()
conta1.saca(500)
conta1.deposita(300)

cliente2 = Cliente('Jonhny Cage', '222.333.444-55')
conta2 = Conta(cliente2, 2, 234, 'jonhny@outlook.com', 5000)
conta2.extrato()
conta2.saca(100)
conta2.deposita(600)
conta2.saldo = 1000000

conta1.transfere(conta2, 2000)
conta2.saca(10000)

conta1.historico.imprime()
conta2.historico.imprime()

# sem decorator
conta1.set_saldo(-100)
print(conta1.get_saldo()) # getter

# com decorator
conta1.saldo = -100
print(conta1.saldo) # getter
'''

# Aula 19/09 - Orientação a objetos
'''
if(conta2.transfere(conta1, 1000)):
    print('OK')
else:
    print('Tá Liso')
'''

# Aula 12/09 - Listas e Funções Lambda

# Lista de palavras
'''
frutas = ['Maçã', 'Banana', 'Laranja']
print(frutas)
print(frutas[0])
print(f'Tamanho: {len(frutas)}')
'''
'''
frutas.append('Uva') # append: adiciona elemento a uma lista (no final dela)
print(frutas)
'''
'''
frutas.insert(1, 'Abacaxi') # insert: adiciona elemento a uma lista (qualquer posição)
print(frutas)
'''
'''
fruta = frutas.pop() # pop: remove elementos de uma lista
print(f'Removido: {fruta}')
print(frutas)
'''
'''
# Lista de números
numeros = [3,1,4,1,5,9,2,6,5,3]
print(numeros)
'''
'''
# Ordenar - Crescente
numeros_ord_c = sorted(numeros)
print(f'Lista ordenada (c): {numeros_ord_c}')
'''
'''
# Ordenar - Decrescente
numeros_ord_d = sorted(numeros, reverse=True)
print(f'Lista ordenada (d): {numeros_ord_d}')
'''
'''
# Dobrar os valores
numeros_dobrados = []
for n in numeros:
    numeros_dobrados.append(n*2)
print(numeros_dobrados)
'''
'''
numeros_dobrados = list(map(lambda n: n*2, numeros))
print(numeros_dobrados)
'''
'''
numeros_filtrados = []
for n in numeros:
    if n > 4:
        numeros_filtrados.append(n)
print(numeros_filtrados)
'''
'''
numeros_filtrados2 = list(filter(lambda n: n > 5, numeros))
print(numeros_filtrados2)
'''
'''
soma = 0
for n in numeros:
    soma += n
print(soma)
'''
'''
from functools import reduce
soma = reduce(lambda soma, n: soma + n, numeros, 1)
print(soma)
'''