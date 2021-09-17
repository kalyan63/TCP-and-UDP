import socket
buffer_size=1024

Available_Files=['DreamDays.txt','FamilyOfEngineers.txt','IntroToRobertBrowning.txt','LifeAndDeath.txt','Test.txt','WarAndPeace.txt']
msg="\n".join([str(i+1)+') '+Available_Files[i] for i in range(len(Available_Files))])

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',12345))
data,addr=s.recvfrom(1024)
s.sendto(msg.encode(),addr)
data,addr=s.recvfrom(1024)
f_name=data.decode()
s.sendto(f_name[:-4].encode(),addr)
with open(f_name,mode='rb') as file:
    data=file.read(buffer_size)
    while(data):
        s.sendto(data,addr)
        data=file.read(buffer_size)
print("{} Sent to: {}".format(f_name,addr))    
s.close()