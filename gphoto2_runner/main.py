# test-server.py
import socket
from server_communicator.CommandParser import command_parser
import json

# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ('localhost', 10001)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)

while True:
    # ждем соединения
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    try:
        print('Подключено к:', client_address)
        # Принимаем данные порциями и ретранслируем их
        while True:
            data = connection.recv(1024)
            print(f'Получено: {data.decode()}')
            if data:
                print('Обработка данных...')
                json_string = data.decode('utf-8')
                json_data = json.loads(json_string)
                answer = command_parser(json_data)
                print('Ответ серверу на запрос...')
                connection.sendall(answer)
            else:
                print('Нет данных от:', client_address)
                break

    finally:
        # Очищаем соединение
        connection.close()