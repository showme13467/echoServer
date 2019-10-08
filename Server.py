import socket
import threading
import concurrent.futures


# Multithreaded Python server : TCP Server Socket Thread Pool

# main method, running all the time until server is shut down
def run(conn,ip,port):
    try:
           while 1:     # while True, the server is running
                data = conn.recv(2024)      # message received and saved as data
                if data:
                    print("Server received data:", data)    # the received data printed out in the server console
                    conn.send(data)     # the server sends this data back to the user
                else:
                    # if there are no more data packages from the user, the server console uses the IP of the user
                    # to specify his identity in the print-order
                    print("User " + ip + " disconnected from the server.")
                    conn.close()    # after printing the connection to the user is shut down
                    break
    except ConnectionResetError:    # Exception Handling for Losing Connection
        # This text is printed to the console of the server after user lost connection
        print("Connection to " + ip + " lost")
        conn.close()    # connection is shut down


TCP_IP = "129.236.228.97"  # The IP-Address for the Server
TCP_PORT = 23456           # The port for the server, should be >1024 caused of already reserved ports

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Server is created with general socket modules
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     # Server is set with general socket modules
tcpServer.bind((TCP_IP, TCP_PORT))      # the server is bound to the given IP and Port
threads = []    # The threads saved in an empty list

tcpServer.listen(4)     # Server is set listening

while 1:
        print ("Multithreaded Python server : Waiting for connections from TCP clients on IP: " + TCP_IP + ":" + str(TCP_PORT) + "...")
        (conn, (ip, port)) = tcpServer.accept()     # Server accepts client
        conn.send(b'connected')     # Server sends after successful connection to user message to user
        print("Server connected to " + ip + ":" + str(port))

        # A new thread is set every time a user connects to the server
        newthread = threading.Thread(target = run, args = (conn,ip,port))
        newthread.start()  # The new thread is started
        print("New thread started")
        threads.append(newthread)       # The thread is added to the list of threads