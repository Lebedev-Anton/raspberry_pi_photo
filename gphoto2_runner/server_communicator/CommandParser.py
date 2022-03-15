import json
import os
import signal
import subprocess

from gphoto2_runner.basic_camera_functions.function import CameraControl


class ParsCommand:
    command = 'capture_image'
    parameter = 'None'
    camera = CameraControl()

    def __init__(self):
        self.camera._set_base_path()
        self.camera._execute_command_('gphoto2 --auto-detect')
        self.kill_gphoto2_process()

    def kill_gphoto2_process(self):
        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            if b'gvfsd-gphoto2' in line:
                pid = int(line.split(None,1)[0])
                os.kill(pid, signal.SIGKILL)

    def set_command(self, command):
        self.command = command

    def set_parameter(self, parameter):
        self.parameter = parameter

    def run_command(self):
        if self.command == 'capture_image':
            self.camera.capture_image('None')
            path = os.path.join(os.getcwd())
            path = os.path.abspath(path)
            answer = {'command': 'capture_image', 'status': path}
        elif self.command == 'set_ISO':
            self.camera.set_ISO(self.parameter)
            answer = {'command': 'set_ISO', 'status': 'Done'}
        elif self.command == 'set_white_balance':
            self.camera.set_white_balance(self.parameter)
            answer = {'command': 'set_white_balance', 'status': 'Done'}
        elif self.command == 'set_zoom':
            self.camera.set_zoom(self.parameter)
            answer = {'command': 'set_zoom', 'status': 'Done'}
        elif self.command == 'set_exposure':
            self.camera.set_exposure(self.parameter)
            answer = {'command': 'set_exposure', 'status': 'Done'}
        elif self.command == 'set_flashcompensation':
            self.camera.set_flashcompensation(self.parameter)
            answer = {'command': 'set_flashcompensation', 'status': 'Done'}
        elif self.command == 'set_aperture':
            self.camera.set_aperture(self.parameter)
            answer = {'command': 'set_aperture', 'status': 'Done'}
        elif self.command == 'set_focusingpoint':
            self.camera.set_focusingpoint(self.parameter)
            answer = {'command': 'set_focusingpoint', 'status': 'Done'}
        elif self.command == 'set_shutterspeed':
            self.camera.set_shutterspeed(self.parameter)
            answer = {'command': 'set_shutterspeed', 'status': 'Done'}
        elif self.command == 'set_shootingmode':
            self.camera.set_shootingmode(self.parameter)
            answer = {'command': 'set_shootingmode', 'status': 'Done'}
        else:
            answer = {'command': self.command, 'status': 'error command'}
        return json.dumps(answer).encode('utf-8')


def command_parser(json_data):
    command = json_data['command']
    parameter = json_data['parameter']
    pars_command = ParsCommand()
    pars_command.set_command(command)
    pars_command.set_parameter(parameter)
    return pars_command.run_command()
