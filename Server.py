import socket
import threading
import concurrent.futures


# Multithreaded Python server : TCP Server Socket Thread Pool

# main method, running all the time until server is shut down
def run(conn,ip,port):
    try:
           while 1:     # while True, the server is running
                data = conn.recv(2024)      # data is named the bytes which the server receives from the user divided in 2024 bytes
                if data:
                    print("Server received data:", data)    # the received data printed out in the server console
                     conn.send(data)     # the server sends this data back to the user
                else:
                    print("User " + ip + " disconnected from the server.")      # if there are no more data packages the user sends, the server console uses the IP of the user to specify his identity in the print-order
                    conn.close()    # after printing the connection to the user is shut down
                    break
    except ConnectionResetError:    # Exception Handling for Losing Connection
        print("Connection to " + ip + " lost")  # This text is printed to the console of the server after user lost connection
        conn.close()    # after printing and using the IP of the user to specify his identity the connection to the user is shut down



# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = "192.168.1.107"   #"209.2.215.140"     # The IP-Address for the Server, should be from the computer creating this server
TCP_PORT = 23456           # The port for the server, should be >1024 caused of already reserved ports
BUFFER_SIZE = 20        # The buffer size depends on underlying device´s block size to buffer binary files in fixed size chunks
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # The server is assigned a pair (IP,Port) in the AF_INET part and a type of socket in the SOCK_STREAM part as part of the creation of the server
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     # Server is set with general socket modules
tcpServer.bind((TCP_IP, TCP_PORT))      # the server is bound to the given IP and Port
threads = []    # The threads saved in an empty list
connections = []    # The connections saved in an empty list

tcpServer.listen(4)     # Server is set listening to the 4th part of the receiving connection, the data

#with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
 #   executor.map(openConn , range(3))
while 1:
        print ("Multithreaded Python server : Waiting for connections from TCP clients on IP: " + TCP_IP + ":" + str(TCP_PORT) + "...")
        (conn, (ip, port)) = tcpServer.accept()
        conn.send(b'connected')
        print("Server connected to " + ip + ":" + str(port))
        newthread = threading.Thread(target = run, args = (conn,ip,port))
        newthread.start()
        print("New thread started")
        threads.append(newthread)




#read the msg line by line
#read implementieren
#wenn jemand die verbindung abbricht dann den thread raus schmeißen mit steg c e.g.



#for t in threads:
 #   t.join()