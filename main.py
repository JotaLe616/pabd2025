## Programação com Acesso a Banco de Dados
# Revisão de Orientação a Objetos
# Prof. Guilherme Leal Santos & João Gabriel dos Santos :p

frutas = ['Maçã', 'Banana', 'Laranja']
print(frutas)
print(frutas[0])
print(f'Tamanho: {len(frutas)}')

frutas.append('Uva') # append: adiciona elemento a uma lista (no final dela)
print(frutas)

frutas.insert(1, 'Abacaxi') # insert: adiciona elemento a uma lista (qualquer posição)
print(frutas)

fruta = frutas.pop() # pop: remove elementos de uma lista
print(f'Removido: {fruta}')
print(frutas)

numeros = [3,1,4,1,5,9,2,6,5,3]
print(numeros)

# Ordenar - Crescente
numeros_ord_c = sorted(numeros)
print(f'Lista ordenada (c): {numeros_ord_c}')

# Ordenar - Decrescente
numeros_ord_d = sorted(numeros, reverse=True)
print(f'Lista ordenada (d): {numeros_ord_d}')

# Dobrar os valores
# numeros_dobrados = []
# for n in numeros:
#    numeros_dobrados.append(n*2)
# print(numeros_dobrados)

numeros_dobrados = list(map(lambda n: n*2, numeros))
print(numeros_dobrados)

numeros_filtrados = []
for n in numeros:
    if n > 4:
        numeros_filtrados.append(n)
print(numeros_filtrados)

numeros_filtrados2 = list(filter(lambda n: n > 5, numeros))
print(numeros_filtrados2)

soma = 0
for n in numeros:
    soma += n
print(soma)

from functools import reduce

soma = reduce(lambda soma, n: soma + n, numeros, 1)
print(soma)