




from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
#DEFINIR OPCOES DE INICIALIZACAO
from selenium.webdriver.chrome.options import Options



def iniciar_driver_solar():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1250,970',]
    for arguments in arguments:
        chrome_options.add_argument(arguments)
        
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'E:\\downloads',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
        
    })
    
#inicializando webdrive
    driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()),options=chrome_options)
    return driver
