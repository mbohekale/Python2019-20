import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10002)

packer = struct.Struct('f f c')

sock.connect( server_address )

print("Connection established...")

data = packer.pack(12.0,11.0,b'+')

sock.sendall(data)
print("Msg sent: 12+11")

data = sock.recv(1024)
res= packer.unpack(bytes(data,utf-8)) 
print("Message from server: %f" % res )

sock.close()