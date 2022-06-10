import socket as s

serversocket=s.socket(s.AF_INET,s.SOCK_STREAM)

host=s.gethostname()
port=9994
serversocket.bind((host,port))
