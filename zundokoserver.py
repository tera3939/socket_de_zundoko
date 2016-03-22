import random
import socket
import threading

bind_ip = '127.0.0.1'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

def zundoko_server():
    print('ズンドコ待機中……')
    while True:
        client_socket, addr = server.accept()

        print('ズンドコ開始!!')
        client_thread = threading.Thread(
                target=zundoko_handler, args=(client_socket,))
        client_thread.start()

def zundoko_handler(client_socket):
    check_kiyoshi = True
    zun = 0
    # 'キ・ヨ・シ!!'が送られるまでループ
    while check_kiyoshi:
        zundoko = random.choice(['ズン'.encode(), 'ドコ'.encode()])
        client_socket.send(zundoko)

        if zundoko == 'ズン'.encode():
            zun += 1
        elif zun >= 4:
            client_socket.send('キ・ヨ・シ!!'.encode())
            check_kiyoshi = False
        else:
            zun = 0

        # 通信同期用のrecv
        buf = client_socket.recv(1024)
    else:
        print('ズンドコ完了')
        client_socket.close()
        print('ズンドコ待機中……')

if __name__ == '__main__':
    zundoko_server()
