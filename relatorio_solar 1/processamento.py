from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command
from drivers import *
from time import sleep

class ExportReport:
    def __init__(self):
        self.__driver = iniciar_driver_solar()

    # Função que realiza o processamento do sistema
    def processar(self, email, pwd, data_ini, data_fim):
        self.__driver.get('')

        # Efetuando login
        try:
            self.__login(email, pwd)
            sleep(2.3)
            
            # Gerando relatório
            self.__gerar_relatorio(data_ini, data_fim)

            # Exportando relatório
            self.__exportar()
            return True

            # Fechando a página
            # sleep(2)
            # self.__driver.close()
        except Exception as e:
            return False
            print(e)
            

    # Função privada que realizada o login
    def __login(self, email, pwd):
        # Carregando elementos da página
        input_email = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#txtUsername > div > div.dx-texteditor-input-container > input')))
        input_senha = self.__driver.find_element(By.CSS_SELECTOR, '#txtSenha > div > div.dx-texteditor-input-container > input')
        btn_login = self.__driver.find_element(By.ID, 'btnSenha' )

        # Preenchendo campos
        self.__preencher_campo(input_email, email)
        self.__preencher_campo(input_senha, pwd)

        # Clique no botão de login
        sleep(1.5)
        btn_login.click()
        

    # Função privada que inicia o processo de gerar relatório
    def __gerar_relatorio(self, dt_ini, dt_fim):
        # Carregando elementos da página
        menu_relatorio_geral = WebDriverWait(self.__driver, 5).until(EC.element_to_be_clickable((By.ID, 'Menu_4')))
        menu_relatorio_especifico = self.__driver.find_element(By.ID, 'Menu_24')
        
        # Clique nos botões para geração do relatório
        sleep(1.5)
        menu_relatorio_geral.click()
        sleep(1.5)
        menu_relatorio_especifico.click()

        # Carregando elementos da próxima página
        data_inicio = WebDriverWait(self.__driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#DataInicio > div > div > div.dx-texteditor-input-container > input')))
        data_fim = self.__driver.find_element(By.CSS_SELECTOR, '#DataFim > div > div > div.dx-texteditor-input-container > input')
        consultar = self.__driver.find_element(By.XPATH, '//*[@id="listaAcao-btnConsultar"]/div/span')
        
        # Limpando valores e preenchendo com os dados informados
        # Data inicial
        self.__limpar_campo(data_inicio)
        self.__preencher_campo(data_inicio, dt_ini)

        # Data final
        self.__limpar_campo(data_fim)
        self.__preencher_campo(data_fim, dt_fim)

        # Gerando relatório
        sleep(1)
        consultar.click()

    # Função que realiza a exportação/download do relatório
    def __exportar(self):
        # Carregando elemento da página
        WebDriverWait(self.__driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#MapaFooterInterna > div > div.dx-datagrid-headers.dx-header-multi-row > div:nth-child(2) > table > tbody > tr.dx-row.dx-column-lines.dx-datagrid-filter-row > td:nth-child(4) > div > div.dx-editor-container > div > div > div > div.dx-texteditor-buttons-container > div.dx-button-normal.dx-button-mode-contained.dx-widget.dx-dropdowneditor-button')))
        exportar_excel = self.__driver.find_element(By.XPATH, '//*[@id="ExportMenu"]')
        sleep(1)

        # Exportando relatório
        exportar_excel.click() 
    

    # Limpa o campo de texto
    def __limpar_campo(self, input):
        sleep(1.5)
        input.click()
        sleep(0.5)
        input.send_keys(Keys.CONTROL, 'a')
        sleep(0.25)
        input.send_keys(Keys.DELETE)
    # Preenche o elemento indicado com o texto informado
    def __preencher_campo(self, input, text):
            sleep(1)
            input.click()
            sleep(0.5)
            for l in text:
                input.send_keys(l)
                sleep(0.075)