import socket
import threading


Server1=('192.168.43.130', 8001)
Server2=('192.168.43.130', 8002)
Server3=('192.168.43.130', 8003)
Server4=('192.168.43.130', 8004)
Server5=('192.168.43.130', 8005)

Servers=[Server1,Server2,Server3,Server4,Server5]


i=0
while i>(-1):
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8000
    s1.bind((host,port))
    print("Starting server load balancer @ {}, {}".format(host,port))
    s1.listen(10)
    print("Server load balancer Started...")
    while True:
        for k in range(len(Servers)):
            clientsocket, addr = s1.accept()
            req = clientsocket.recv(1024)
            print("Got a connection from : ", str(addr), " asking about data ", str(req))

            try:
                def cr(m,n):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    s.connect((m))

                    s.send(n)

                    msg=s.recv(1024)
    
                    clientsocket.send((msg))
                    s.close()

            

                print(Servers[k])
                t1=threading.Thread(target=cr,args=(Servers[k],req))
                t1.start()
                t1.join()

            except:
                print("Some unknown error occoured.")
                clientsocket.send("Some unknown error occoured".encode('ascii'))
            
    i+=1
