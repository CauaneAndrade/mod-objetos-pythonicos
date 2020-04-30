import operator

'''
Construa uma função de ordenação que ordene os alunos por nota. Se houver empate, nome
deverá definir a ordem

>>> alunos = [('dé', 5), ('bebéu', 8), ('cazuza b', 9), ('cazuza a', 9)]
>>> alunos.sort(key=ordenar_por_nota_e_nome)
>>> alunos
[('dé', 5), ('bebéu', 8), ('cazuza a', 9), ('cazuza b', 9)]
'''

alunos = [('dé', 5), ('bebéu', 8), ('cazuza b', 9), ('cazuza a', 9), ('cazuza ba', 9)]
ordenar_por_nota_e_nome = operator.itemgetter(1, 0)
alunos.sort(key=ordenar_por_nota_e_nome)
print(alunos)