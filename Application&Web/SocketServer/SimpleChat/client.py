import socket, threading, time

KEY = 1488
shutdown = join = False


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except:
            pass


SERVER = (socket.gethostname(), 5050)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 0))
clientName = input("Name: ")

rT = threading.Thread(target=receving, args=("RecvThreading", server))
rT.start()

while not shutdown:
    if not join:
        server.sendto(f"{clientName} connect to chat".encode("utf-8"), SERVER)
        join = True
    else:
        try:
            message = input()
            if message.rstrip():
                """
                # Begin
                crypt = ""
                for i in message:
                    crypt += chr(ord(i) ^ KEY)
                message = crypt
                # End
                """
                server.sendto(f"{clientName} :: {message}".encode("utf-8"), SERVER)
            time.sleep(0.2)
        except:
            server.sendto((f"{clientName} left chat").encode("utf-8"), SERVER)
            shutdown = True
rT.join()
server.close()
