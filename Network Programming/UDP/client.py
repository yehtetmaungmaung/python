from socket import *

s = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    s.sendto(data.encode('utf-8'), ('localhost', 8888))
    resp, addr = s.recvfrom(1024)
    if not resp:
        break
    print(resp.decode('utf-8'))