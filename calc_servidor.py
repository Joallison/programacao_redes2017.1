import socket
import math

serverHost = 'localhost'
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))

print("Servidor pronto para receber: ")

def soma(a, b):
	return a + b
def raiz(a):
	r = math.sqrt(a)
	return r

while True:
	escolha, clientAddress = serverSocket.recvfrom(2048)
	a = escolha.decode('utf-8')
	print (a)
	
	if a == '1':
		num1, clientAddress = serverSocket.recvfrom(2048)
		b1 = num1.decode('utf-8')
		print (b1)

		num2, clientAddress = serverSocket.recvfrom(2048)
		b2 = num2.decode('utf-8')
		print (b2)
		
		Message = soma(int(b1), int(b2))
		modifiedMessage = str(Message).encode('utf-8')
		serverSocket.sendto(modifiedMessage, clientAddress)  
	elif a == '2':
		num1, clientAddress = serverSocket.recvfrom(2048)
		b1 = num1.decode('utf-8')
		print (b1)
		
		Message = raiz(int(b1))
		print (Message)
		modifiedMessage = str(Message).encode('utf-8')
		serverSocket.sendto(modifiedMessage, clientAddress)
	else:
		print ("Mensagem Invalida")