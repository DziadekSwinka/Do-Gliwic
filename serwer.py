import socket as s
import os
#from PySide6.QtWidgets import QApplication,QWidget,QLabel,QLineEdit

'''class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()
    def setup(self):
        label=QLabel(self)
        label.setText(f"Temperatura: ")
        self.setFixedSize(800,600)
        self.setWindowTitle("MainWindow")
        self.show()
    def OnTextChanged(self,text):
        label.setText('Temperatura'+text)
        self.update()
'''
if __name__=="__main__":

    #app=QApplication([])
    #main_window=MainWindow()
    HOST='192.168.0.97'
    PORT=1313
    BUFFER=1024
    #app.exec()
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
            #main_window.OnTextChanged(name)
            if float(name)>=28:
                os.system("C://Users//pc//Desktop//Na_gliwice//Alarm//bin//Release//Alarm.exe")
    