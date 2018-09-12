
import socket

## data set

i=0
while i>(-1):

    d = {1:"Bangalore",2:"Mumbai",3:"Chennai"}

    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8002
    s1.bind((host,port))
    print("Starting server @ {}, {}".format(host,port))
    s1.listen(10)
    print("Server2 Started...")
    while True:
        clientsocket, addr = s1.accept()
        req = clientsocket.recv(1024)
        print("Got a connection from : ", str(addr), " asking about data ", str(req))
        try:
            id = int(req)
            if id <= 0 or id > 3:
                msg = "Invalid Index"
            else:
                #msg = d[id]
                msg = str('This response is from Server2 and answer is : {}'.format(d[id]))
            clientsocket.send(msg.encode('ascii'))
            print("Responsed")
        except:
            print("Some unknown error occoured.")
            clientsocket.send("Some unknown error occoured".encode('ascii'))
        finally:
            clientsocket.close()
        i+=1
