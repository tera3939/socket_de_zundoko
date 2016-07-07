#!/usr/bin/env python3
# -*-coding:utf-8-*-

import socket


class ZundokoClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_zundoko(self, host, port):
        get_kiyoshi = False
        try:
            self.client.connect((host, port))
            # 'キ・ヨ・シ!!'が送られてくるまでループ
            while not get_kiyoshi:
                data = self.client.recv(4096)
                zundoko = data.decode()
                print(zundoko)
                if zundoko == 'キ・ヨ・シ!!':
                    get_kiyoshi = True
                # 通信同期用のsend
                self.client.send('ok'.encode())
            else:
                self.client.close()
                print('ズンドコ成功')
        except InterruptedError:
            print('ズンドコ失敗')
            self.client.close()

if __name__ == '__main__':
    target_host = 'localhost'
    target_port = 9999
    zundoko = ZundokoClient()
    zundoko.get_zundoko()
