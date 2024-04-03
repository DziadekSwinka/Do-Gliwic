import random
import time
import socket as s
import json

<<<<<<< Updated upstream
HOST='192.168.0.104'
PORT=1313
=======
HOST = '192.168.0.97'
PORT = 1313
>>>>>>> Stashed changes
print("Klient")
client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)

while True:
    t = round(random.random() * 10 + 20, 0)
    h = round(random.random() * 10 + 20, 0)
    data = {"temp": str(t),"hum": str(h)}
    json_data = json.dumps(data)
    client_socket.sendto(json_data.encode(), (HOST, PORT))
    time.sleep(1)

client_socket.close()
input()
