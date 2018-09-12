


import socket

i=0
while i>(-1):
    g=input("Press Enter: ")
    k=str(g)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8000
    s.connect((host,port))
    s.send(k.encode('ascii'))
    msg = s.recv(1024)
    s.close()
    print("REPLY : ", msg)
    i+=1

    




