import socket, time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((socket.gethostname(), 5050))
print("[#] Server started")

clients = []

quitFLAG = False
while not quitFLAG:
    try:
        data, addr = server.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        print(f"[{addr[0]}]-[{addr[1]}]-[{itsatime}]", end='')
        print(data.decode("utf-8"))

        for client in clients:
            if addr != client:
                server.sendto(data, client)

    except:
        quitFLAG = True
        print("[#] Server stopped")

server.close()
