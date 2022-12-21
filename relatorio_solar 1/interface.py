from processamento import ExportReport
from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime, timedelta
import re

class Interface:
    def __init__(self):
        self.__start_hour = '00:00'
        self.__end_hour = '23:59'
        self.__yesterday = datetime.now() - timedelta()

        self.__first_date = self.__yesterday.strftime("%d/%m/%Y ") + self.__start_hour
        self.__last_date = self.__yesterday.strftime("%d/%m/%Y ") + self.__end_hour

    def execute(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Email', size=(7,1)),sg.Input(key='usuario', size=(30,1))],
            [sg.Text('Senha',size=(7,1)),sg.Input(key='senha',password_char='*', size=(30,1))],
            [sg.Text('Dt Inicial',size=(7,1)),sg.Input(default_text=self.__first_date, key='dt_ini', size=(30,1))],
            [sg.Text('Dt Final',size=(7,1)),sg.Input(default_text=self.__last_date, key='dt_fim', size=(30,1))],
            [sg.Button(button_text='Exportar', key='next')]
        ]

        janela = sg.Window('Login', layout)  
        while True:
            eventos, valores = janela.read()
            if eventos == sg.WINDOW_CLOSED:
                break
            if eventos == 'next':
                email = valores['usuario']
                senha = valores['senha']
                data_inicio = valores['dt_ini']
                data_fim = valores['dt_fim']

                validacao, campo = self.__validar_campos(valores)
                if (validacao):
                    relatorio = ExportReport()
                    processamento = relatorio.processar(email, senha, data_inicio, data_fim)

                    if processamento:
                        janela['dt_ini'].set_focus()
                        sg.Popup('Relatório exportado')
                        
                    else:
                        sg.popup_error('Erro ao exportar relatório')
                else:
                    sg.popup_error('Campo(s) inválido(s)')
                    janela[campo].set_focus()
        
        #janela.close()
        

    def __validar_campos(self, campos):
        if (not re.match(r"\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}$", campos['dt_ini'])):
            flag = False
            elemento = 'dt_ini'
        elif (not re.match(r"\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}$", campos['dt_fim'])):
            flag = False
            elemento = 'dt_fim'
        elif (not re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", campos['usuario'])):
            flag = False
            elemento = 'usuario'
        elif (campos['senha'] == ''):
            flag = False
            elemento = 'senha'
        else:
            flag = True
            elemento = ''

        return (flag, elemento)
