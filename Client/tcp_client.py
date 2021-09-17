import os
import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=12345
buffer_size=1024
st=time.time_ns()
s.connect(('127.0.0.1',port))
msg=s.recv(1024).decode()
ed=time.time_ns()
print((st-ed)/10**6)
print(msg)   
print('\n'+'The Available files are: ')
msg=s.recv(1024).decode()
print(msg)
print()
start_time=end_time=0
while True:
    print("Enter the File to be Downloaded: ")    
    input_st=input()
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