import socket as s
import os
from PySide6.QtWidgets import QApplication,QWidget,QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()
       
    def setup(self):
        label=QLabel(self)
        label.setText("Temperatura: ")
        self.setFixedSize(800,600)
        self.setWindowTitle("MainWindow")
        self.show()

if __name__=="__main__":

    #app=QApplication([])
    #main_window=MainWindow()
    #app.exec()
    HOST='192.168.56.1'
    PORT=1313
    BUFFER=1024
    
    print("Serwer")

    server_socket= s.socket(s.AF_INET,s.SOCK_STREAM)
    server_socket.bind((HOST,PORT))
    server_socket.listen()
    
    while True:
        client_socket,address=server_socket.accept()
        print(f"Uzyskano połączenie od {address}")
        while True:
            name=client_socket.recv(BUFFER).decode("utf8")
            print(f"Temperatura: {name} C")
            if float(name)>=28:
                os.system("C://Users//pc//Desktop//Na_gliwice//Alarm//bin//Release//Alarm.exe")