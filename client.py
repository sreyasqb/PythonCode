import socket as s
import os
client=s.socket()
host=s.gethostname()
filename='input_data/a_an_example.in.txt'
port=9994
client.connect((host, port))
client.send(f"{filename}|{os.path.getsize(filename)}".encode())

f=open(filename,'rb')
while True:
    bytes_read=f.read(1)


    if not bytes_read:break
    # print(bytes_read, bin(ord(bytes_read))[2:].zfill(8))
    client.sendall(bin(ord(bytes_read))[2:].zfill(8).encode())


# tm=client.recv(1024)
# print(tm.decode('ascii'))
client.close()
