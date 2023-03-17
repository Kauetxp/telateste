import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text("Nome"),sg.Input()],
            [sg.Text("Nome"),sg.Input()],
            [sg.Button("Enviar dados")]
        ]
        #Janela
        janela = sg.Window("Dados do usuário").layout(layout)
        #Extração
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()