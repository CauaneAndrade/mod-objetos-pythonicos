# 1. global: em nível de módulo (globals())
# 2. local: disponível apenas no nível, por exemplo, de uma função (locals())

# o Python primeiro procura no escopo local e depois no global
# se não achou no local, então procura no global

a = 5

def f(a=1):
    b = 3
    print(globals())
    print(locals())

f()

print(globals())