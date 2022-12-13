#IMPORTAR TODASFUNCIONALIDADES DO SELELIUN
from selenium import webdriver
import getpass
import pyautogui
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from PySimpleGUI import PySimpleGUI as sg
#DEFINIR OPCOES DE INICIALIZACAO
from selenium.webdriver.chrome.options import Options
from func import * #importando arquivo python
from time import*


sg.theme('Reddit')
layout = [
   #recebe o texto / faz o input para usuario
   [sg.Text('Email', size=(7,1)),sg.Input(key='usuario', size=(30,1))],
   [sg.Text('Senha',size=(7,1)),sg.Input(key='senha',password_char='*', size=(30,1))],
   #[sg.Checkbox('Salvar Login ?')],
   [sg.Text('Dt Inicial',size=(7,1)),sg.Input(key='Dt Inici', size=(30,1))],
   [sg.Text('Dt Final',size=(7,1)),sg.Input(key='Dt Fina', size=(30,1))],
   [sg.Button('Salvar')],
   [sg.Button('Seguir')]
]

#janela
#                 titulo  / o layout a usar
janela = sg.Window('Login', layout)
#ler eventos
while True:
   eventos, valores = janela.read()
   if eventos == sg.WINDOW_CLOSED or eventos == 'Seguir':
      break
   if eventos == 'Salvar':
      digitar_email = valores['usuario']
      digitar_senha = valores['senha']
      digitar_data_inicio = valores['Dt Inici']
      digitar_data_fim = valores['Dt Fina']
      
janela.close()


# digitar_email = input('Digite o email de Login - ')

# digitar_senha = getpass.getpass ('Digite sua Senha - ')

# digitar_data_inicio = input('Digite a data e hora INICIAL - ')
# digitar_data_fim = input('Digite a data e hora FINAL - ')

passar_data_inicio=''
passar_data_fim =''

drive_inicial = iniciar_driver_solar()

# 1* abrir o navegador ( Google crhome )
# 2* abri o site (  )
drive_inicial.get('')
sleep(5)
# 3 fazer Login
# 	3.1 digitar email (orniliooficial@gmail.com)
email = drive_inicial.find_element(By.ID, 'txtUsername' )
sleep(1)
email.click()
sleep(1)
digitar_email = pyautogui.typewrite(digitar_email)
# 	3.2 digitar Senha (********)
senha = drive_inicial.find_element(By.ID, 'txtSenha' )
sleep(1)
senha.click()
sleep(1)
digitar_senha = pyautogui.typewrite(digitar_senha)
# 	3.3 clicar em entrar/ok
btn_login = drive_inicial.find_element(By.ID, 'btnSenha' )
sleep(1)
btn_login.click()
sleep(2.3)
# 4* clicar no icone de relatorio
menu_relatorio_geral = drive_inicial.find_element(By.ID, 'Menu_4' )
sleep(1.5)
menu_relatorio_geral.click()
# 5* clicar em relatorio GERAL (relatorios de rastreamento)
menu_relatorio_especifico = drive_inicial.find_element(By.ID, 'Menu_24' )
sleep(1.5)
menu_relatorio_especifico.click()
# 6* informar periofo ( preferencia informar no inicio do programa as datas de pesquisa)
# 	6.1 data inicila + hora
data_inicio = drive_inicial.find_element(By.ID, 'DataInicio' )
sleep(1.5)
data_inicio.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('del')
# data_inicio.click()
for i in digitar_data_inicio:
    pyautogui.press(i)   
    passar_data_inicio = passar_data_inicio+i
    ###DESCARTADO###
# 	6.2 unidade organizacional ( GM Transportes)
# 		6.2.1 clica em OK

# 	6.3 data final + hora
data_fim = drive_inicial.find_element(By.ID, 'DataFim')
sleep(1.5)
data_fim.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('del')
for i in digitar_data_fim:
    pyautogui.press(i)   
    passar_data_fim = passar_data_fim+i
# 7* clica em consultar/ok
consultar = drive_inicial.find_element(By.ID, 'listaAcao-btnConsultar')
sleep(1)
consultar.click()
sleep(40)
# 8* na aba do sub menu clicar em exportar ( execel)
exportar_execel = drive_inicial.find_element(By.ID, 'ExportMenu')
sleep(1)
exportar_execel.click()
sleep(1)


input('')
drive_inicial.close()
