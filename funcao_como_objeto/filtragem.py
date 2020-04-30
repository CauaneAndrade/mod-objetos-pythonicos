# filtragem mapa
alunos = [('dé', 5), ('bebéu', 8), ('cazuza', 9)]

print([(aluno, nota) for aluno, nota in alunos if nota > 5])  # list comprehension, usando o conceito de filtro

# filtro utilizando programação funcional
def possui_nota_maior_que_5(aluno):
    _, nota = aluno
    return nota > 5

print(list(filter(possui_nota_maior_que_5, alunos))) # função de alta ordem
