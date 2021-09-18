import os
import socket
import time
import select
from threading import Thread

def tcp(f_name):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port=12345
    buffer_size=1024
    s.connect(('127.0.0.1',port))
    msg=s.recv(1024).decode()
    print('TCP message')   
    msg=s.recv(1024).decode()
    start_time=end_time=0
    while True:  
        input_st=f_name
        start_time=time.time_ns()
        s.send(input_st.encode())
        msg=s.recv(1024).decode()
        if(msg=='File_Downloading'):
            fname=s.recv(1024).decode()
            fname+="_Protocol=TCP_"+str(os.getpid())+".txt"
            with open(fname,'wb') as f:
                while True:
                    line=s.recv(buffer_size)
                    if(line):
                        f.write(line)
                    else:
                        break      
                end_time=time.time_ns()    
                break
        else:
            print(msg)
    print("Time taken to download is: {}".format((end_time-start_time)/10**6))        
    s.close()

def udp(f_name):
    addr=('127.0.0.1',12345)
    buffer_size=1024
    start_time=end_time=0
    wait_time=1
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.sendto('Hi'.encode(),addr)
    msg,addr=s.recvfrom(1024)
    print('UDP message')
    start_time=time.time_ns()
    s.sendto(f_name.encode(),addr)
    data,addr=s.recvfrom(1024)
    f_name=data.decode()
    f_name+='_Protocol=UDP_'+str(os.getpid())+'.txt'
    with open(f_name,mode='wb') as file:
        while True:
            ready=select.select([s],[],[],wait_time)
            if(ready[0]):
                data,addr=s.recvfrom(buffer_size)
                file.write(data)
            else:
                end_time=time.time_ns()
                break    
    print("Time taken to download the file is: {}".format((end_time-start_time)/10**6-wait_time*1000))
    s.close()

t1=Thread(target=tcp,args=('Test.txt',))
t2=Thread(target=udp,args=('Test.txt',))

t1.start()
t2.start()