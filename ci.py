import socket


host = '192.168.43.23'
port = 5000

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

while True:
    msg_client = input('client@-->').encode()
    client.send(msg_client)
    recv_data = client.recv(8192).decode()
    print('Server Msg :',recv_data)
