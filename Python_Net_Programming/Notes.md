# Protocol

- set of rules that allow 2 or more devices to communicate.

##OSI: 

    1. Physical:
        - physical transmission of bite stream.
       
    2.Data Link:
        - Data validation and bite packaging in frames.
    
    3. Network:
        - transformation to packages and distribution to network.
    
    4. Transport:
        - 
        
    5. Sessions:
        - 
        
    6. Presentation:
        - 
        
    7. Application:
        - 

##PCP-IP:

    1. Link/Physical Layer
    2. Internet Layer
    3. Transportation Layer
    4. Application Layer


## HTTP, FTP, SMTP 

### Physical Layer:
#### ARP Protocol
    - MAC Address
        - length of 48 bites
        - unic, hexadecimal
        - first 24 bites are from the producer 
        - last 24 bites are the unic numbers

    -IP Address:
        - length of 32 bites
        - decimal numbers.

    - Subnet Mask:
        - tells the length of the ip and the number of bites of the first part.(ip-address)
        - last part will be the host.

    - Hostname - device name 

    - Loopback - local address.
        -127.0.0.1

### Internet Layer
    
### Transportation Layer
    - TCP (Transmission Control Protocol)
    - User Datagram Protocol (User Datagram Protocol)
    - ICMP (Internet COntrol Message Protocol)

### Protocol TCP 
- A connection maintained until closed.
- Bidirectional Transfer
>Characteristics:
> - High fiability (FTP, HTTP, SMTP ...)
> - Low reconnection, not useable by real time communication.

> Components:
>  - Source port and destination port are
>  - Sequence number
>  - Acknoledgement numbers
>  - data offset, reserved, Flags, Window 
>  - Checksum , Urgent Pointer 
>  - Options, Padding 
>  - Data 

 >Handshake TCP (3 way handshake):
> 1. SYN
> 2. SYN-ACK 
> 3. ACK 


### Protocol UDP:

- Do not require a persistent connection between the points.
  
> Characteristics:
> - Speed and efficiency
> - Bad data integrity.

> UDP packages:
> - Source port - destination port
> - length, Checksum

## Socket 
 > http://beej.us/guide/bgnet/
