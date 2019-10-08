import socket
import time

ip = "129.236.229.157"#"129.236.229.240"
port = 23456

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((ip,port))
#s.get.... nicht socket
selfip = socket.gethostbyname(socket.gethostname())
print(selfip)
print("> connected to %s" %ip)

print("> Type 'exit' to leave this room")

proceed = "exit"
message = ""
while True:
    try:
        while message != proceed:
                data = s.recv(60)


                if data:
                    print("> Server recieved: %s" %data)
                    message = input("enter your text: ")
                    message1 = str(message).encode("utf-8")
                    s.sendall(message1)


    except ConnectionError:
        print("You have lost the Connection. Try again.")
        s.close()
        break

    except (KeyboardInterrupt, SystemExit):
        raise

s.close()