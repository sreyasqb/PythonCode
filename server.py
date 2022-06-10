import socket as s
import os
server=s.socket()

host=s.gethostname()
port=9994

server.bind((host,port))
server.listen()
client,addr=server.accept()
print(f'got connection from {addr}')
rec=client.recv(4096).decode()
filename,fsize=rec.split('|')
filename=os.path.basename(filename)
fsize=int(fsize)
# f=open(filename,'wb')
while True:
    bytes_read=client.recv(8)
    if not bytes_read:break
    print(bytes_read)
client.close()
server.close()