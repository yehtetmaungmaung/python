from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 22222))

while True:
    data = input('> ')
    if not data:
        break
    s.send(data.encode('utf-8'))
    resp = s.recv(1024)
    if not resp:
        break
    print(resp.decode("utf-8"))