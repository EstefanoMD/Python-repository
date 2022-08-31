from ast import Return
import random
import PySimpleGUI as sg


sg.theme('BlueMono')
layout = [
        [sg.Text('Entre na sua conta.' )],
        [sg.Text('Usuário:')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha:')],
        [sg.Input(key='senha')],
        [sg.Button('login')],
        [sg.Text('',key='mensagem')]
]
window = sg.Window('Login' , layout=layout, finalize=True)



while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    elif event =='login':
        usuario_correto = 'abcde'
        senha_correta = '12345'
        #Atualizar código e implementar um banco de dados para as senhas e usuarios
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login realizado com sucesso!')
        else:
            window['mensagem'].update('senha ou usuario incorreto!')

    


        
      








