import socket
serverName = 'localhost'
serverPort = 12000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Selecione a operacao.")
print("1.Soma")
print("2.Raiz Quadrada")

escolha = input("Entre com o numero da Operacao:")
if escolha == '1':
        num1 = input("Primeiro valor: ")
        num2 = input("Segundo valor: ")
        byte_msg1 = escolha.encode('utf-8')
        byte_msg2 = num1.encode('utf-8')
        byte_msg3 = num2.encode('utf-8')
        clientSocket.sendto(byte_msg1, (serverName, serverPort))
        clientSocket.sendto(byte_msg2, (serverName, serverPort))
        clientSocket.sendto(byte_msg3, (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode('utf-8'))
        clientSocket.close()
else:
       num1 = input("Primeiro valor: ")
       byte_msg1 = escolha.encode('utf-8')
       byte_msg2 = num1.encode('utf-8')
       clientSocket.sendto(byte_msg1, (serverName, serverPort))
       clientSocket.sendto(byte_msg2, (serverName, serverPort))
       modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
       print(modifiedMessage.decode('utf-8'))
       clientSocket.close()