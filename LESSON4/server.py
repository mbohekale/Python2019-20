import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('0.0.0.0', 10002)
sock.bind(server_address)

sock.listen( 5 )
print("Server is up...")

packer = struct.Struct("f f c")

try:
	while True:
		client, client_info = sock.accept()
		print("Client address: %s client port: %d" % client_info)

		data = client.recv(100)
		a,b,op = packer.unpack( data )

		print("Message as a string: %f %f %c" % (a,b,op) )

		if op=='+':
			a = a+b

		resp = packer.pack(a,0.0,'R')
		
		client.sendall( resp )
		print("Message sent: %f" % a)

		client.close()
except:
	print("Termination")
finally:
	print("Closing socket...")
	sock.close()