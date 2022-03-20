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
        if self.command == 'stop_server':
            return 'stop_server'
        else:
            if 'get' in self.command:
                status = getattr(self.camera, self.command)()
            else:
                status = getattr(self.camera, self.command)(self.parameter)
            answer = {'command': self.command, 'status': status}
        return json.dumps(answer).encode('utf-8')


def command_parser(json_data):
    command = json_data['command']
    parameter = json_data['parameter']
    pars_command = ParsCommand()
    pars_command.set_command(command)
    pars_command.set_parameter(parameter)
    return pars_command.run_command()
