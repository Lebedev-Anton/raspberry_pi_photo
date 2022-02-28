import requests
from gphoto2_runner.Config import base_url


def get_commands():
    response = requests.get(url=base_url)
    if response.status_code == 200:
        return response.json()
    else:
        return response


def del_command(id_command):
    response = requests.delete(url=base_url, json={'id': id_command})
    return response


def post_command(command=None, file=None):
    response = requests.post(url=base_url, json=command, files=file)
    if response.status_code == 200:
        return response
    else:
        return response


if __name__ == '__main__':
    # command = {'command': 'set_ISO', 'parameter': 'ISO_400', 'status': False}
    command = {'command': 'capture_image', 'parameter': 'None', 'status': False}
    print(del_command(14))

