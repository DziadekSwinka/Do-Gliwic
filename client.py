import random
import time
import socket as s

HOST='192.168.56.1'
PORT=1313
temp=0
print("Klient")
client_socket=s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((HOST,PORT))
while True:
    name=str(round(random.random()*10+20,0)).encode("utf8")
    print(f"Temp: {name}")
    client_socket.send(name)
    time.sleep(1)
input()    
    