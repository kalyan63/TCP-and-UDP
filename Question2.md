## This is the answer for the 2nd Question: 

1. **Sender buffer size=1024 and receiver buffer size=2048**

    > 
        |       Options:        |       TCP         |       UDP         |
        _________________________________________________________________

        | No of Packets:        |       37          |       14          |
        -----------------------------------------------------------------
        | Set connection and    |       7           |       2           |
        | Receive list of files |                   |                   |
        -----------------------------------------------------------------
        |Which File to download |       6           |       2           |
        -----------------------------------------------------------------
        | For file data:        |       20          |       10          |
        -----------------------------------------------------------------
        | End Connection:       |       4           |       0           |
        -----------------------------------------------------------------    
    
    > There was no difference in file size and both the downloaded files were exactly same as original file.


2. **Sender buffer size=1024 and receiver buffer size=512**

    > 
        |       Options:        |       TCP         |       UDP         |
        _________________________________________________________________

        | No of Packets:        |       37          |       14          |
        -----------------------------------------------------------------
        | Set connection and    |       7           |       2           |
        | Receive list of files |                   |                   |
        -----------------------------------------------------------------
        |Which File to download |       6           |       2           |
        -----------------------------------------------------------------
        | For file data:        |       20          |       10          |
        -----------------------------------------------------------------
        | End Connection:       |       4           |       0           |
        ----------------------------------------------------------------- 

    > Tcp download size was 10KB and udp failed to download the file.

    > error: 

        OSError: [WinError 10040] A message sent on a datagram socket was larger than the internal message buffer or some other network limit, or the buffer used to receive a datagram into was smaller than the datagram itself


3. **Sender buffer size=512 and receiver buffer size=2048**

    > 
        |       Options:        |       TCP         |       UDP         |
        _________________________________________________________________

        | No of Packets:        |       57          |       24          |
        -----------------------------------------------------------------
        | Set connection and    |       7           |       2           |
        | Receive list of files |                   |                   |
        -----------------------------------------------------------------
        |Which File to download |       6           |       2           |
        -----------------------------------------------------------------
        | For file data:        |       40          |       20          |
        -----------------------------------------------------------------
        | End Connection:       |       4           |       0           |
        ----------------------------------------------------------------- 

    > There was no difference in file size and both the downloaded files were exactly same as original file.

4. **Sender buffer size=1024 and receiver buffer size=2048 and Wait time of 10ms after receiving each packet**

    > 
        |       Options:        |       TCP         |       UDP         |
        _________________________________________________________________

        | No of Packets:        |       37          |       14          |
        -----------------------------------------------------------------
        | Set connection and    |       7           |       2           |
        | Receive list of files |                   |                   |
        -----------------------------------------------------------------
        |Which File to download |       6           |       2           |
        -----------------------------------------------------------------
        | For file data:        |       20          |       20          |
        -----------------------------------------------------------------
        | End Connection:       |       4           |       0           |
        ----------------------------------------------------------------- 

    > There was no difference in file size and both the downloaded files were exactly same as original file.

5. **Concurrent running of TCP and UDP client:**

    > We can test this by running both tcp and udp server, Then run ConcurrentTcpUdp.py file to run both tcp and udp client to download Test.txt file simultaniously. 

    > This is possible because every packet is identified by Protocol information(Here its Tcp and Udp) along with, 
    SourceIp, DestinationIp, SourcePort and DestinationPort. 

    > Hence we can run both tcp and udp server with same port number and can server request concurrently. 

    > Here we can see the wireshark data which shows that tcp and udp client are downloading simultaneously. 
    
        File name: (Concurrent Tcp and UDP.pcapng)