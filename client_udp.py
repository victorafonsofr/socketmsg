import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket.AF_INET: IPv4, socket.SOCK_DGRAM: UDP
SERVER_IP = '192.168.0.55'
PORT = 8090

try: 

    msg = input("mensagem: ")
    client.sendto(msg.encode(), (SERVER_IP, PORT)) #conexao mais envio
    data, sender = client.recvfrom(1024) #conexao mais recebimento
    print(sender[0] + ': ' + data.decode())
except Exception as err:
    print("algo deu errado com a conexao!\n")
    print(err)