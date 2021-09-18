import socket
import os
import select
import time

addr=('127.0.0.1',12345)
buffer_size=1024
start_time=end_time=0
wait_time=3 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto('Hi'.encode(),addr)
print('The Available Files are: ')
msg,addr=s.recvfrom(1024)
print(msg.decode())
print('Enter the file name from above to be Downloaded:')
f_name=input()
start_time=time.time_ns()
s.sendto(f_name.encode(),addr)
data,addr=s.recvfrom(1024)
f_name=data.decode()
f_name+='_Protocol=UDP_'+str(os.getpid())+'.txt'
with open(f_name,mode='wb') as file:
    while True:
        ready=select.select([s],[],[],wait_time)
        if(ready[0]):
            # time.sleep(0.01)
            data,addr=s.recvfrom(buffer_size)
            file.write(data)
        else:
            end_time=time.time_ns()
            break    
print("Time taken to download the file is: {}".format((end_time-start_time)/10**6-wait_time*1000))
s.close()