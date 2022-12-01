import threading
import sys
import socket
import pickle
import os


class Cliente():
    
    def __init__(self, host=input("Introduzca la IP del Servidor: "), port=int(input("Introduzca el puerto del servidor: ")), nick=input('Introduce tu Nickname: ')):
            
            self.s = socket.socket()
            self.s.connect((host, int(port)))
            
            print('\n\tProceso con PID = ',os.getpid(), '\n\tHilo Principal con ID = ',threading.current_thread().name, '\n\tHilo en Modo DAEMON = ', 
                  threading.current_thread().isDaemon(), '\n\tHilos activos en este punto de programa = ', threading.active_count())

            threading.Thread(target=self.recibir, daemon=True).start()

            while True:

                msg = input('\nIntroduzca su mensaje -> ** Enviar = ENTER ** Salir = 1 \n')

                if msg != '1' : self.enviar(msg)
                else:
                        print('Me piro del chat, cierro el socket y mato al CLIENTE con PID = ', os.getpid())
                        self.s.close()
                        sys.exit()

    def recibir(self):

            print('\nHilo RECIBIR con ID = ', threading.current_thread().name, '\n\tPertenece al proceso con PID = ', os.getpid(), '\n\tHilos Activos totales = ', threading.active_count())
            while True:
                try:
                        data = self.s.recv(32)
                        if data: print(pickle.loads(data))

                except: pass

    def enviar(self,msg):
        self.s.send(pickle.dumps(msg))
        

arrancar = Cliente()