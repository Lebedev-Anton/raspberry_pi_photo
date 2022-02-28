import time

from server_communicator.request_api import get_commands, del_command, post_command
from basic_camera_functions.camera_enumerations import ISO, CaptureType, WhiteBalance
from basic_camera_functions.function import CameraControl
from os import listdir, remove


def main_loop():
    camera = CameraControl()
    camera._set_base_path()
    camera._execute_command_('gphoto2 --auto-detect')
    while True:
        commands = get_commands()
        for command in commands:
            if command.get('command') == 'capture_image':
                camera.capture_image(CaptureType.Save)
                files = listdir()
                jpg_file = [file for file in files if file.endswith('.JPG')][-1]
                with open(jpg_file, 'rb') as fb:
                    post_command(command={'command': 'save_file'}, file={'files': fb})
                remove(jpg_file)
            elif command.get('command') == 'set_ISO':
                camera.set_ISO(ISO[command.get('parameter')])
            elif command.get('command') == 'set_white_balance':
                camera.set_white_balance(WhiteBalance[command.get('parameter')])
            del_command(command.get('id'))
        time.sleep(0.5)


if __name__ == '__main__':
    main_loop()
