
import socket
import threading
import random

Server1=('192.168.43.130', 8001)
Server2=('192.168.43.130', 8002)
Server3=('192.168.43.130', 8003)
Server4=('192.168.43.130', 8004)
Server5=('192.168.43.130', 8005)

Servers=[Server1,Server2,Server3,Server4,Server5]
m=len(Servers)


i=0
while i>(-1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 7998
    s.bind((host,port))

    print("Starting server load balancer @ {}, {}".format(host,port))
    s.listen(10)
    print("Server load balancer Started...")
    while True:
        n=(random.randint(0,m))
        clientsocket, addr = s.accept()
        req = clientsocket.recv(1024)
        print("Got a connection from : ", str(addr), " asking about data ", str(req))
        try:
            def cr(address,request):
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((address))
                s.send(request)
                msg=s.recv(1024)
                clientsocket.send((msg))
                s.close()

            t1=threading.Thread(target=cr,args=((Servers[n],req)))
            
            t1.start()
            t1.join()
            t1.lock()
        except:
            print("Some unknown error occoured.")
            clientsocket.send("Some unknown error occoured".encode('ascii'))
        
    i+=1
