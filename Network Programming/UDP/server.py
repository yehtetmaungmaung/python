from socket import *
from time import ctime

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 8888))

while True:
    print('Waiting for message....')
    data, addr = s.recvfrom(1024)
    resp = f"server reply message[{ctime()}]- {data.decode('utf-8')}"
    s.sendto(resp.encode('utf-8'), addr)