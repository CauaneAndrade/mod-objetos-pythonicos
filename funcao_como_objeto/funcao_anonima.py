def dobro(x):
    return x * 2

dobro_2 = lambda x: x * 2  # recebe o parâmetro x e retorna o dobro de x

# diferença entre função tradicional e lambda (anônima)
print(dobro.__name__)  # return 'dobro'
print(dobro_2.__name__)  # return '<lambda>'
