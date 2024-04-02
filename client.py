import random
import time
import socket as s

HOST='192.168.0.104'
PORT=1313
print("Klient")
client_socket=s.socket(s.AF_INET, s.SOCK_DGRAM)
client_socket.connect((HOST,PORT))
while True:
    name=str(round(random.random()*10+20,0))
    print(f"Temp: {name}")
    client_socket.sendall(name.encode())
    time.sleep(1)
client_socket.close()    
input()      