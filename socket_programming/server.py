import socket
import threading
import os
HEADER=1024
FORMAT='utf-8'
DISCONNECT_MESSAGE='!DISCONNECT'
topics={'topic1':['sub1Address,sub2Address'],'topic2':['sub1Address,sub2Address']}
path='D:\Coding\PythonCoding\PythonCode\socket_programming'


def handle_client(conn,address):
    producer=False
    consumer=False
    print(f'[NEW CONNECTION] {address} connected.')
    connected = True
    while connected:
        message = conn.recv(1024).decode()
        
        if not message:
            # if data is not received break
            break
        userType,topic,data=message.split(',')
        topic=topic.strip()
        data=data.strip()
        print(data)
        if userType.lower()=='c':
            consumer=True
        else:
            producer=True
        if producer:
            if topic in os.listdir(path):
                partionCount=os.listdir(f'{path}/{topic}')
                print(partionCount)
                partFile=open(f'socket_programming/{topic}/{partionCount[-1]}','a+')
                print(partFile.readlines())
                testFile=open(f'socket_programming/{topic}/{partionCount[-1]}','r')
                noOfLines=len(testFile.readlines())
                testFile.close()
                if noOfLines<2:
                    partFile.write(data+"\n")
                    partFile.close()
                else:
                    print('exceeded')
                    f=open(f'socket_programming/{topic}/partion{len(partionCount)+1}.txt','a')
                    f.write(data+"\n")
                    f.close()
                
            else:
                os.mkdir(f'socket_programming/{topic}')
                f=open(f'socket_programming/{topic}/partion{1}.txt','a')
                f.write(data+"\n")
                f.close()
            if topic in topics:
                pass
                # for sub in topics[topic]:
                #     conn.send(data.encode())
            else:
                pass
            print(f'{topic} - {data}')
        else:
            f=open(f'socket_programming/{topic}/partion1.txt','r')
            conn.send(' '.join(f.readlines()).encode())
    conn.close()


def main():
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)



    


    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        thread=threading.Thread(target=handle_client,args=(conn,address))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')
        # receive data stream. it won't accept data packet greater than 1024 bytes
        
        # data = input(' -> ')
        
        # conn.send(data.encode())  # send data to the client


if __name__ == '__main__':
    main()