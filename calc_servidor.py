import socket
serverHost = 'localhost'
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))

print("Servidor pronto para receber: ")

def soma(a, b):
	return a + b

while True:
	escolha, clientAddress = serverSocket.recvfrom(2048)
	a = escolha.decode('utf-8')
	print (a)

	num1, clientAddress = serverSocket.recvfrom(2048)
	b1 = num1.decode('utf-8')
	print (b1)

	num2, clientAddress = serverSocket.recvfrom(2048)
	b2 = num2.decode('utf-8')
	print (b2)

	if a == '1':
		Message = soma(int(b1), int(b2))
		modifiedMessage = str(Message).encode('utf-8')
		serverSocket.sendto(modifiedMessage, clientAddress)



