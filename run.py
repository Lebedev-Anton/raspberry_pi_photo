# test-server.py
import socket
import sys

from gphoto2_runner.socket_communicator.CommandParser import command_parser
import json

# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ('localhost', 10001)
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)

while True:
    # ждем соединения
    connection, client_address = sock.accept()
    try:
        # Принимаем данные порциями и ретранслируем их
        while True:
            data = connection.recv(4096)
            if data:
                json_string = data.decode('utf-8')
                json_data = json.loads(json_string)
                answer = command_parser(json_data)
                if answer == 'stop_server':
                    sys.exit()
                connection.sendall(answer)
            else:
                break
    finally:
        # Очищаем соединение
        connection.close()