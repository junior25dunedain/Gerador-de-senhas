import PySimpleGUI as sg

def Tela():
    sg.theme('DarkGreen2')
    Titulo = [[sg.Text('Gerador de Senhas',font='arial 20 bold')]]
    botoes = [
        [sg.Button('Gerar',font='arial 12',size=(8,1))],
        [sg.CButton('Sair',font='arial 12',size=(8,1))]
    ]
    coluna2 = [[sg.Text('Tamanho da senha:',font='arial 10 bold')],[sg.Text('Senha:',font='arial 16 bold')]]
    coluna3 = [[sg.Input(font='arial 12', key='tamanho', size=(5, 1),justification='center')],[sg.Input(font='arial 15',key='senha',size=(25,1))]]
    c1,c2,c3,c4 = [coluna2[0]],[coluna3[0]],[coluna2[1]],[coluna3[1]]
    layout = [
        [sg.Column(Titulo, justification='center', element_justification='center')],
        [sg.Column(c1,justification='left'),sg.Column(c2,element_justification='center')],
        [sg.Column(c3, justification='center',pad=(0,0))],
        [sg.Column(c4, justification='center',pad=(0,0))],
        [sg.Column(botoes, justification='center')]
    ]

    telaprint = sg.Window('Gerador_Senha', element_padding=(0, 10), layout=layout, size=(400, 380), finalize=True)

