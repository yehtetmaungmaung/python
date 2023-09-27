from socket import *
from time import ctime

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 22222))
s.listen(5)

while True:
    print("Waiting for connection...")
    client, addr = s.accept()
    print(f"Connected from {addr}")

    while True:
        data = client.recv(1024)
        if not data:
            break
        resp = f"server reply message[{ctime()}] {data.decode('utf-8')}"
        client.send(resp.encode('utf-8'))