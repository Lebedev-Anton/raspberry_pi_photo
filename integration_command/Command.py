import socket
import time
import json
import os
import inspect
from threading import Thread


def start_gphoto2():
    path = os.path.abspath(os.path.join(os.getcwd(), '..', 'gphoto2_runner'))
    command = f'cd {path}; python main.py'
    th = Thread(target=_execute_command_, args=(command,))
    th.start()
    time.sleep(5)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10002)
    sock.connect(server_address)

    # mess = {'command': 'capture_image', 'parameter': '7'}
    # message = json.dumps(mess).encode('utf-8')
    # sock.sendall(message)
    # # Смотрим ответ
    # data = sock.recv(1024)
    return sock, th


def stop_server(sock):
    mess = {'command': 'stop_server', 'parameter': 'None'}
    message = json.dumps(mess).encode('utf-8')
    sock.sendall(message)
    sock.close()


def get_ISO(sock):
    return _send_command_(sock, inspect.stack()[0][3])


def get_white_balance(sock):
    return _send_command_(sock, inspect.stack()[0][3])


def get_zoom(sock):
    return _send_command_(sock, inspect.stack()[0][3])


def get_exposure(sock):
    return _send_command_(sock, inspect.stack()[0][3])


def get_flashcompensation(sock):
    return _send_command_(sock, inspect.stack()[0][3])


def get_aperture(sock):
    return _send_command_(sock, inspect.stack()[0][3])


def get_focusingpoint(sock):
    return _send_command_(sock, inspect.stack()[0][3])


def get_shutterspeed(sock):
    return _send_command_(sock, inspect.stack()[0][3])


def get_shootingmode(sock):
    return _send_command_(sock, inspect.stack()[0][3])


def get_camera_setting(sock):
    command = 'get_white_balance'
    return _send_command_(sock, command)


def set_ISO(sock, parameter):
    command = 'set_ISO'
    return _send_command_(sock, command, parameter)


def _send_command_(sock, command, parameter='None'):
    mess = {'command': command, 'parameter': parameter}
    message = json.dumps(mess).encode('utf-8')
    sock.sendall(message)
    # Смотрим ответ
    data = sock.recv(1024)
    meas = data.decode('utf-8')
    meas = json.loads(meas)
    if 'get' in command:
        return meas['status']['Current']
    else:
        return meas['status']


def _execute_command_(command):
    return os.system(command)


if __name__ == '__main__':
    sock, th = start_gphoto2()
    print(get_camera_setting(sock))
    print(get_ISO(sock))
    print(set_ISO(sock, '80'))
    print(get_white_balance(sock))
    print(get_white_balance(sock))
    print(get_zoom(sock))
    print(get_exposure(sock))
    print(get_flashcompensation(sock))
    print(get_aperture(sock))
    print(get_focusingpoint(sock))
    print(get_shutterspeed(sock))
    print(get_shootingmode(sock))
    stop_server(sock)
