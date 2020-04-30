# função é um cidadão de primeira classe: é um objeto como outro qualquer

def dobro(x):
    return x * 2

# função têm atributos
from dis import dis
print(dobro.__code__.co_code)
dis(dobro.__code__.co_code)

# criar atributos para função
dobro.n = 42
print(dobro.n)

# deletar atributos de uma função
del dobro.n

# coisas que fazemos com outros objetos: atribuições
# com funções é a mesma coisa
f = dobro
print(f.__name__)