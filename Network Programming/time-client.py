from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8889))
t = s.recv(1024)
print(t.decode('ascii'))