import socket

ip = "129.236.228.97"   #IP address of the server
port = 23456

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # creating the socket

s.connect((ip, port))    # connecting the socket to the server

print("> connected to %s" %ip)
print("> Type 'exit' to leave this room")

proceed = "exit"   # creating an option to exit the chat
message = ""

while True:
    try:
        while message != proceed:   # if the client enters exit, the while loop stops
                data = s.recv(60)   # data the socket receives

                if data:
                    print("> Server recieved: %s" %data.decode("utf-8"))
                    message = input("enter your text: ") # is printed to the client
                    message = message + "\n" + "that is your new line" 
                    message1 = str(message).encode("utf-8")     # message is decoded in UTF-8
                    s.sendall(message1)     # message is send to server

    except ConnectionError:     # handling connectionerror
        print("You have lost the Connection. Try again.")
        s.close()   # close socket
        break

    except (KeyboardInterrupt, SystemExit):     # handling an Keyboardinterrupt and Systemexit
        raise

s.close()   # close socket
