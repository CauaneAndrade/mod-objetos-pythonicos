import operator

alunos = [('dé', 5), ('bebéu', 8), ('cazuza', 9)]

# filtro utilizando programação funcional
def possui_nota_maior_que_5(aluno):
    _, nota = aluno
    return nota > 5

print(list(map(operator.itemgetter(0), filter(possui_nota_maior_que_5, alunos))))