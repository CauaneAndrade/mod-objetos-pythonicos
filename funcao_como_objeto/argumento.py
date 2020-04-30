# função que recebe função como parâmetro: função de alta ordem

def ola_mundo():
    print("olá mundo!")

def exe(f, n):
    for _ in range(n):
        f()

exe(ola_mundo, 5)