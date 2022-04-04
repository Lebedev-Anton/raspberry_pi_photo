import socket
import sys
import time
import json
import os
import inspect
from threading import Thread


def connect_to_socket(func):
    def connect(sock, ip, port, parameter=None):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, port)
        sock.connect(server_address)
        func(sock, ip, port, parameter, sock)
        sock.close()
    return connect


def start_gphoto2(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    mess = {'command': 'capture_image', 'parameter': '7'}
    message = json.dumps(mess).encode('utf-8')
    sock.sendall(message)
    # Смотрим ответ
    data = sock.recv(4096)
    sock.close()


def capture_image(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3])
    sock.close()
    return res


def stop_server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    mess = {'command': 'stop_server', 'parameter': 'None'}
    message = json.dumps(mess).encode('utf-8')
    sock.sendall(message)
    sock.close()


def get_ISO(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3])
    sock.close()
    print(res)
    return res


def get_white_balance(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3])
    sock.close()
    print(res)
    return res


def get_zoom(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3])
    sock.close()
    print(res)
    return res


def get_exposure(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3])
    sock.close()
    print(res)
    return res


def get_flashcompensation(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3])
    sock.close()
    print(res)
    return res


def get_aperture(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3])
    sock.close()
    print(res)
    return res


def get_focusingpoint(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3])
    sock.close()
    print(res)
    return res


def get_shutterspeed(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3])
    sock.close()
    print(res)
    return res


def get_shootingmode(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3])
    sock.close()
    print(res)
    return res


def get_camera_setting(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3])
    sock.close()

    print('ISO', 'Current:' + str(res['ISO']['Current']), '|' + str(res['ISO']['Choice'])[1:-1])
    print('white_balance', 'Current:' + str(res['white_balance']['Current']), '|' + str(res['white_balance']['Choice'])[1:-1])
    print('exposure', 'Current:' + str(res['exposure']['Current']), '|' + str(res['exposure']['Choice'])[1:-1])
    print('flashcompensation', 'Current:' + str(res['flashcompensation']['Current']), '|' + str(res['flashcompensation']['Choice'])[1:-1])
    print('aperture', 'Current:' + str(res['aperture']['Current']), '|' + str(res['aperture']['Choice'])[1:-1])
    print('focusingpoint', 'Current:' + str(res['focusingpoint']['Current']), '|' + str(res['focusingpoint']['Choice'])[1:-1])
    print('shutterspeed', 'Current:' + str(res['shutterspeed']['Current']), '|' + str(res['shutterspeed']['Choice'])[1:-1])
    print('shootingmode', 'Current:' + str(res['shootingmode']['Current']), '|' + str(res['shootingmode']['Choice'])[1:-1])
    print('zoom', 'Current:' + str(res['zoom']['Current']), '|' + str(res['zoom']['Bottom']), str(res['zoom']['Top']))
    return res


def set_ISO(ip, port, parameter):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    return _send_command_(sock, inspect.stack()[0][3], parameter)


def set_white_balance(ip, port, parameter):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3], parameter)
    sock.close()
    return res


def set_zoom(ip, port, parameter):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3], parameter)
    sock.close()
    return res


def set_exposure(ip, port, parameter):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3], parameter)
    sock.close()
    return res


def set_flashcompensation(ip, port, parameter):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3], parameter)
    sock.close()
    return res


def set_aperture(ip, port, parameter):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3], parameter)
    sock.close()
    return res


def set_focusingpoint(ip, port, parameter):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3], parameter)
    sock.close()
    return res


def set_shutterspeed(ip, port, parameter):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3], parameter)
    sock.close()
    return res


def set_shootingmode(ip, port, parameter):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    res = _send_command_(sock, inspect.stack()[0][3], parameter)
    sock.close()
    return res


def _send_command_(sock, command, parameter='None'):
    mess = {'command': command, 'parameter': parameter}
    message = json.dumps(mess).encode('utf-8')
    sock.sendall(message)
    # Смотрим ответ
    data = sock.recv(4096)
    meas = data.decode('utf-8')
    meas = json.loads(meas)
    if 'get' in command:
        return meas['status']['Current']
    else:
        return meas['status']


def _execute_command_(command):
    return os.system(command)



if __name__ == '__main__':
    command_line_data = sys.argv
    # ip = '192.168.1.73'
    # port = 10002
    # sock = None
    # parameter = None
    ip = command_line_data[1]
    port = int(command_line_data[2])
    function_name = command_line_data[3]
    parameter = command_line_data[4]
    if parameter == 'None':
        # print(ip, port, function_name, parameter)
        globals()[function_name](ip, port)
    else:
        globals()[function_name](ip, port, parameter)
    # start_gphoto2(ip, port)
    # print(get_camera_setting(ip, port))
    # print(get_ISO(ip, port))
    # print(get_white_balance(ip, port))
    # print(get_zoom(ip, port))
    # print(get_exposure(ip, port))
    # print(get_flashcompensation(ip, port))
    # print(get_aperture(ip, port))
    # print(get_focusingpoint(ip, port))
    # print(get_shutterspeed(ip, port))
    # print(get_shootingmode(ip, port))
    #
    # print(set_ISO(ip, port, '80'))
    # print(set_white_balance(ip, port, 'Fluorescent'))
    # print(set_zoom(ip, port, '4'))
    # print(set_exposure(ip, port, '+2'))
    # print(set_flashcompensation(ip, port, '0'))
    # print(set_aperture(ip, port, '1.1'))
    # print(set_focusingpoint(ip, port, 'Multiple'))
    # print(set_shutterspeed(ip, port, '25'))
    # print(set_shootingmode(ip, port, 'AV'))
    #
    # print(get_ISO(ip, port))
    # print(get_white_balance(ip, port))
    # print(get_zoom(ip, port))
    # print(get_exposure(ip, port))
    # print(get_flashcompensation(ip, port))
    # print(get_aperture(ip, port))
    # print(get_focusingpoint(ip, port))
    # print(get_shutterspeed(ip, port))
    # print(get_shootingmode(ip, port))
    # print(capture_image(ip, port))
    # stop_server(sock)
