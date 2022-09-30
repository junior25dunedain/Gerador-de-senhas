import random, string
from interface import *

def Criar(valor):
    tamanho = int(valor)

    chars = string.ascii_letters + string.digits + 'ç!@#$%&*()+/?_'

    rnd = random.SystemRandom() # os.urandom gera caracteres aleatorios a partir do sistema operacional
    while True:
        cont = 0
        cont2 = 0
        senha = ''.join(rnd.choice(chars) for i in range(tamanho))
        for j in senha:
            if j in string.digits:
                cont += 1
            elif j in 'ç!@#$%&*()+/?_':
                cont2 += 1
        if cont > 0 and cont2 > 0:
            break
    with open('senhas.txt','a+') as arp:
        arp.write(f'Senha criada: {senha}\n')

    return senha


Tela()
while True:
    janela, evento, valores = sg.read_all_windows()

    if evento == sg.WIN_CLOSED:
        break

    if evento == 'Gerar':
        try:
            senha = Criar(valores['tamanho'])
            janela['senha'].update(senha)
        except:
            sg.Popup('Cuidado! Digite o tamanho da senha.',title='Erro')