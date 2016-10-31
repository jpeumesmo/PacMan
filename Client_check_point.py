import socket, select, string, sys
import thread
import sys

HOST = sys.argv[1]  # HOST = '172.16.254.209'# Endereco IP do Servidor
PORT = int(sys.argv[2])  # Porta que o Servidor esta

dest = (HOST, PORT)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(dest)

class Mensagem():

    def envia(self):
        thread.start_new_thread(m.recebe, tuple([1,2]))
        msg = raw_input('digite .. para sair\n')
        while msg <> '..':
            tcp.send (msg)
            msg = raw_input()
        tcp.send ('out')
        tcp.close()

    def recebe(self,a,b):
        while True:

            msg = tcp.recv(32)
            print msg
            if str(msg) <> 'out':
                print msg
# t = treadd(tcp)

m = Mensagem()
m.envia()
