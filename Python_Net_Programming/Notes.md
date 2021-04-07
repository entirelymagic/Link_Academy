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


### Protocol UDP(User Datagram Protocol:

- Do not require a persistent connection between the points.
  
> Characteristics:
> - Speed and efficiency
> - Bad data integrity.

> UDP packages:
> - Source port - destination port
> - length, Checksum

## Socket 
 > http://beej.us/guide/bgnet/

API-us BSD 
1. Socket: create socket object
2. Bind: Occupy port 
3. Listen: wait for connection
4. Accept:  Accept the entry connection.
5. Connect:  Establish connection
6. Send: Send the data 
7. Recv: Get the data
8. Close: close socket

### HTTP Protocol

Requests and responses in HTTP:
> Request:
> 
> Method (`get`, `post` ...)
> 
> - hostname
> 
> - address 
> 
> - the resource
>
> Reply:
> - the status ( `200` if okay, `404` if not)
> - Headers
> - Content

> HTTP Messages :
> 
> - Headers
> 
> - Body 
> 

GET request does not contain a body!

> MIME (Multipurpose Internet Mail Extensions):
> 
> http://iana.org media types 
>

### Authentication - Basic Authentication

    - WHen client request a protected resource the server will respond with\
    a 401 status code and will communicate how to authenticate through\
    the www-authenticate
    - Client will send a new request that will include the credentials access\
    (username and password) in header Authorization
    - The server check the authorization of the user.
    - If the request is denied do to invalid login will return 401 or 403 if the\
    resource is not accessible.

The answer send from client will be BASE64 encoded.

### Websocket 

    - Used for bidirectional communication, persistent.
    - Based on TCP 
    - It is using HTTP protocol to initiate the connection
    - used by browser and server 
    - used for bidirectinal communication between programs who do not run in browser.

#### Websocket structure:

    - F = if message is complete 
    - 3 * R = reserved
    - opcode = reading (1=text, 2=binary)  # content_type similar to
    - M = check if the content is masked or not
    - message lenght = 7 bytes for message length
    - mask = If the mask exists this will ocuppy the next 32 bytes
    - content = the message, of data length


