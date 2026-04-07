import socket

serverIP = '192.168.0.52'
port = 8090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET: IPv4, socket.SOCK_STREAM: TCP


try:
   
    client.connect((serverIP, port))
    client.send(b"ola\n") #saudação inicial
    print("você: ola \n")

    while True:
        #recebe mensagem do servidor
        data = client.recv(1024).decode()
        
        if not data:
            print("conexão encerrada pelo servidor\n")
            break

        print(f"servidor: {data}")

        #usuario envia mensagem

        text = input("você: ")
        client.send(text.encode())

        #condição de parada das mensagens

        if text.lower()=='tchau':
            break


except ConnectionRefusedError:
    print("Não foi possível conectar...\nverifique se o servidor está online.\n")

finally:
    print("conexao finalizada")
    client.close()

