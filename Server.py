import socket #подключение библиотек
import os

server = socket.socket(

    socket.AF_INET,      #Настройка протокола итернет
    socket.SOCK_STREAM,  #TCP/IP

)

server.bind(

    ("127.0.0.1", 1236) #ip и порт 

)

server.listen(#Даёт зеленый цвет для принятия данных
    10 #огронечение в клиентах
    ) #дает серверу право подключать другил клиентам

print('Сервер запустился')

while True:
    try:

        user_socket, address = server.accept() #Принимает клиента

        data = user_socket.recv(2048)

        if data.decode('utf-8') == 'homework':
            user_socket.send('OK'.encode('utf-8'))

            homework = open('homework.txt', 'r')

            home = homework.read()

            user_socket.send(home.encode('utf-8'))

            homework.close()

    except: 

        print("Клиент не смог подключился")