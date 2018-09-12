
import socket

import threading


Server1=('192.168.43.130', 8001)
Server2=('192.168.43.130', 8002)
Server3=('192.168.43.130', 8003)
Server4=('192.168.43.130', 8004)
Server5=('192.168.43.130', 8005)

Servers=[(Server1,3),(Server2,2),(Server3,3),(Server4,1),(Server5,2)]

i=0
while i>(-1):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 7999
    s.bind((host,port))
    print("Starting server Load Balancer @ {}, {}".format(host,port))
    s.listen(10)
    print("Server Load Balancer Started...")
    while True:
        for server,capacity in Servers:
            count=0
            while count<capacity:
                clientsocket, addr = s.accept()
                req = clientsocket.recv(1024)
                print("Got a connection from : ", str(addr), " asking about data ", str(req))
                try:
                    def cr(server,capacity):
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((server))

                        s.send(req)

                        msg = s.recv(1024)
                        clientsocket.send((msg))
                        s.close()

                    print(server)
                    t1=threading.Thread(target=cr,args=((server,req)))
                    t1.start()
                    t1.join()

                except:
                    print("Some unknown error occoured.")
                    clientsocket.send("Some unknown error occoured".encode('ascii'))


                count+=1

                
        
        i+=1
