import socket
import threading

# main method, running all the time until server is shut down
def run(conn,ip,port):
    try:
           while 1:     # while True, the server is running
                data = conn.recv(2024)      # message received and saved as data
                if data:
                    newMessage = str(data).split('\\n')     # message is split at new line symbol
                    newMessage[0] = newMessage[0].replace("b'", "", 1) # removing useless parts
                    newMessage[0] += " "
                    print(newMessage)
                    finalMessage = ""

                    # puts chars from newMessage in finalMessage
                    for i in newMessage:
                         finalMessage += i
                    finalMessage[:-1]   # removes last useless char
                    print(finalMessage)
                    
                    # received data printed out in the server console
                    print("Server received data from " + ip + " : " , data)
                    conn.send(data)     # the server sends this data back to the user

                else:
                    # if there are no more data packages from the user, the server console uses the IP of the user
                    # to specify his identity in the print-order
                    print("User " + ip + " disconnected from the server.")
                    conn.close()    # after printing the connection to the user is shut down
                    break

    except ConnectionResetError:    # exception Handling for losing the connection
        # This text is printed to the console of the server after user lost connection
        print("Connection to " + ip + " lost")
        conn.close()    # connection is shut down


TCP_IP = "129.236.228.97"  # IP-Address for the Server
TCP_PORT = 23456           # port for the server, should be >1024 caused of already reserved ports

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Server is created with general socket modules
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     # Server is set with general socket modules
tcpServer.bind((TCP_IP, TCP_PORT))      # the server is bound to the given IP and Port
threads = []    # tne threads saved in an empty list

tcpServer.listen(4)     # Server is set listening

while 1:
        print ("Multithreaded Python server : Waiting for connections from TCP clients on IP: "
               + TCP_IP + ":" + str(TCP_PORT) + "...")
        
        (conn, (ip, port)) = tcpServer.accept()     # server accepts client
        conn.send(b'connected')     # server sends a message to the user after successful connection to the user
        print("Server connected to " + ip + ":" + str(port))

        # A new thread is set every time a user connects to the server
        newthread = threading.Thread(target = run, args = (conn,ip,port))
        newthread.start()  # The new thread is started
        print("New thread started")
        threads.append(newthread)     # the thread is added to the list of threads
