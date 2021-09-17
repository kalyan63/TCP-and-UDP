import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=12345
buffer_size=1024
s.bind(('127.0.0.1',port))
s.listen(5)
print('Server listning at port: {}'.format(port))


Available_Files=['DreamDays.txt','FamilyOfEngineers.txt','IntroToRobertBrowning.txt','LifeAndDeath.txt','Test.txt','WarAndPeace.txt']

while True:
    c,addr=s.accept()
    print('Connected with : {}'.format(addr))
    c.send("The Connection is Set".encode())
    msg="\n".join([str(i+1)+') '+Available_Files[i] for i in range(len(Available_Files))])
    c.send(msg.encode())
    while True:
        msg=c.recv(1024).decode()
        if(msg in Available_Files): 
            c.send('File_Downloading'.encode())
            c.send(msg[:-4].encode())
            with open(msg,'rb') as file:
                data=file.read(buffer_size)
                while(data):
                    c.send(data)
                    data=file.read(buffer_size)
            print('Done Sending {} File to: {}'.format(msg,addr))   
            break 
        else:
            c.send('File Doesn\'t Exists'.encode())    
    print("Server Closed")    
    c.close()
    break
print("Done serving")
