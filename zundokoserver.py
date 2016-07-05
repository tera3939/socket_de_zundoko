import random
import socket
import threading


class ZundokoServer:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def zundoko_start(self, bind_ip, bind_port):
        self.server.bind((bind_ip, bind_port))
        self.server.listen(5)
        while True:
            client_socket, addr = self.server.accept()
            client_thread = threading.Thread(
                    target=self.zundoko_handler, args=(client_socket,))
            client_thread.start()

    def zundoko_handler(self, client_socket):
        send_kiyoshi = False
        zun = 0
        # 'キ・ヨ・シ!!'が送られるまでループ
        while not send_kiyoshi:
            zundoko = random.choice(['ズン', 'ドコ'])
            client_socket.send(zundoko.encode())
            if zundoko == 'ズン':
                zun += 1
            elif zun >= 4:
                client_socket.send('キ・ヨ・シ!!'.encode())
                send_kiyoshi = True
            else:
                zun = 0
            # 通信同期用のrecv
            buf = client_socket.recv(1024)
        else:
            print('ズンドコ完了')
            client_socket.close()
            print('ズンドコ待機中……')

if __name__ == '__main__':
    zundoko = ZundokoServer()
    bind_ip = '127.0.0.1'
    bind_port = 9999
    zundoko.zundoko_start(bind_ip, bind_port)

