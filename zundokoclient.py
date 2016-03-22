import socket

target_host = 'localhost'
target_port = 9999
get_kiyoshi = True

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((target_host, target_port))

    # 'キ・ヨ・シ!!'が送られてくるまでループ
    while get_kiyoshi:

        data = client.recv(4096)
        zundoko = data.decode()

        print(zundoko)

        if zundoko == 'キ・ヨ・シ!!':
            get_kiyoshi = False

        # 通信同期用のsend
        client.send('ok'.encode())
    else:
        client.close()
        print('ズンドコ成功')

except:
    print('ズンドコ失敗')
    client.close()
