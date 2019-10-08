import socket
import threading



def run(conn,ip,port):
    try:
           while 1:
                data = conn.recv(2024)
                if data:
                    print("Server received data:", data)
                    conn.send(data)
                else:
                    print(ip + " disconnected from the server.")
                    conn.close()
                    break
    except ConnectionResetError:
        print("Connection to " + ip + " lost")
        conn.close()



# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = "129.236.229.157" #'129.236.229.240'
TCP_PORT = 23456
BUFFER_SIZE = 20
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []
connections = []

tcpServer.listen(4)

while 1:
        print ("Multithreaded Python server : Waiting for connections from TCP clients on IP: " + TCP_IP + ":" + str(TCP_PORT) + " ...")
        (conn, (ip, port)) = tcpServer.accept()
        conn.send(b'connected')
        print("Server connected to " + ip + ":" + str(port))
        newthread = threading.Thread(target = run, args = (conn,ip,port))
        newthread.start()
        print("New thread started")
        threads.append(newthread)




#read the msg line by line
#read implementieren



