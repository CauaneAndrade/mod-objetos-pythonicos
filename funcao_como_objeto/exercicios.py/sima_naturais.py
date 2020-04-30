import operator
from functools import reduce

'''
1. Defina a função soma_nat que recebe como argumento um número
natural  n  e devolve a soma de todos os números naturais até  n

>>> soma_nat(10)
55

2. Defina a função quadrados que recebe como argumento um número
natural n  devolve a lista dos  n  primeiros quadrados perfeitos

>>> quadrados(5)
[1, 4, 9, 16, 25]
'''

# 1
n = 10
soma_nat = reduce(operator.add, range(n + 1))
# print(soma_nat)

# 2
n = 5
quadrados = lambda x: operator.pow(x, 2)
result = list(map(quadrados, range(1, n + 1)))
print(result)