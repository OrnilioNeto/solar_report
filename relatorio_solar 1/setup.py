import sys
import os
from cx_Freeze import setup,Executable

#Definir arquivos 
arquivos = ['func.py']
#saida de arquivos
configuracao = Executable(
    script='relatorio_solar.py',
    icon='icone.ico'
)
#configuracao
setup(
    name='Relatorio Unidade',
    version='1.0',
    description='Automação para download de relatorio',
    author='Ornilio Neto',
    options={'build_exe':{
        'include_files': arquivos,
        'include_msvcr': True
    }},
    executables=[configuracao]
)