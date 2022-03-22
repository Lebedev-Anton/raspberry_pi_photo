import os
import sys
from io import StringIO
# from .camera_enumerations import ISO, CaptureType, WhiteBalance, ShootingMode


class OutputInterceptor(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


class CameraControl:
    ISO = {}
    white_balance = {}
    shooting_mode = {}
    zoom = {}
    exposure = {}
    flashcompensation = {}
    aperture = {}
    focusingpoint = {}
    shutterspeed = {}
    shootingmode = {}

    def capture_image(self, type_capture):
        if type_capture == 'Base':
            command = 'gphoto2 --capture-image'
        else:
            command = 'gphoto2 --capture-image-and-download'
        return self._execute_command_(command)

    def get_camera_setting(self):
        camera_setting = {}
        camera_setting['IS0'] = self.get_ISO()
        camera_setting['white_balance'] = self.get_white_balance()
        camera_setting['zoom'] = self.get_zoom()
        camera_setting['exposure'] = self.get_exposure()
        camera_setting['flashcompensation'] = self.get_flashcompensation()
        camera_setting['aperture'] = self.get_aperture()
        camera_setting['focusingpoint'] = self.get_focusingpoint()
        camera_setting['shutterspeed'] = self.get_shutterspeed()
        camera_setting['shootingmode'] = self.get_shootingmode()
        return {'Current': camera_setting}

    def get_ISO(self):
        command = f'gphoto2 --get-config /main/imgsettings/iso'
        self._execute_command_(command)
        with open('test.py', 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.ISO = self._pars_data_(data)
        return self.ISO

    def get_white_balance(self):
        command = f'gphoto2 --get-config /main/imgsettings/whitebalance'
        self._execute_command_(command)
        with open('test.py', 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.white_balance = self._pars_data_(data)
        return self.white_balance

    def get_zoom(self):
        command = f'gphoto2 --get-config /main/capturesettings/zoom'
        self._execute_command_(command)
        with open('test.py', 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.zoom = self._pars_data_(data)
        return self.zoom

    def get_exposure(self):
        command = f'gphoto2 --get-config /main/capturesettings/exposurecompensation'
        self._execute_command_(command)
        with open('test.py', 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.exposure = self._pars_data_(data)
        return self.exposure

    def get_flashcompensation(self):
        command = f'gphoto2 --get-config /main/capturesettings/flashcompensation'
        self._execute_command_(command)
        with open('test.py', 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.flashcompensation = self._pars_data_(data)
        return self.flashcompensation

    def get_aperture(self):
        command = f'gphoto2 --get-config /main/capturesettings/aperture'
        self._execute_command_(command)
        with open('test.py', 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.aperture = self._pars_data_(data)
        return self.aperture

    def get_focusingpoint(self):
        command = f'gphoto2 --get-config /main/capturesettings/focusingpoint'
        self._execute_command_(command)
        with open('test.py', 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.focusingpoint = self._pars_data_(data)
        return self.focusingpoint

    def get_shutterspeed(self):
        command = f'gphoto2 --get-config /main/capturesettings/shutterspeed'
        self._execute_command_(command)
        with open('test.py', 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.shutterspeed = self._pars_data_(data)
        return self.shutterspeed

    def get_shootingmode(self):
        command = f'gphoto2 --get-config /main/capturesettings/shootingmode'
        self._execute_command_(command)
        with open('test.py', 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.shootingmode = self._pars_data_(data)
        return self.shootingmode

    def set_ISO(self, value):
        if not self._is_readonly_(self.ISO):
            if value in self.ISO['Choice'].keys():
                command = f'gphoto2 --set-config /main/imgsettings/iso={int(self.ISO["Choice"][value])}'
                self._execute_command_(command)
                answer = 'Done'
            else:
                answer = 'Значение параметра не доступно'
        else:
            answer = 'Параметр доступен только для чтения'
        return answer

    def set_white_balance(self, value):
        if not self._is_readonly_(self.white_balance):
            if value in self.white_balance["Choice"].keys():
                command = f'gphoto2 --set-config /main/imgsettings/whitebalance={int(self.white_balance["Choice"][value])}'
                self._execute_command_(command)
                answer = 'Done'
            else:
                answer = 'Значение параметра не доступно'
        else:
            answer = 'Параметр доступен только для чтения'
        return answer

    def set_zoom(self, value):
        value = int(value)
        if not self._is_readonly_(self.zoom):
            bottom = int(self.zoom['Bottom'])
            top = int(self.zoom['Top'])
            if value < bottom:
                value = bottom
            if value > top:
                value = top
            command = f'gphoto2 --set-config /main/capturesettings/zoom={value}'
            self._execute_command_(command)
            answer = 'Done'
        else:
            answer = 'Параметр доступен только для чтения'
        return answer

    def set_exposure(self, value):
        if not self._is_readonly_(self.exposure):
            if value in self.exposure["Choice"].keys():
                command = f'gphoto2 --set-config /main/capturesettings/exposurecompensation={int(self.exposure["Choice"][value])}'
                self._execute_command_(command)
                answer = 'Done'
            else:
                answer = 'Значение параметра не доступно'
        else:
            answer = 'Параметр доступен только для чтения'
        return answer

    def set_flashcompensation(self, value):
        if not self._is_readonly_(self.flashcompensation):
            if value in self.flashcompensation["Choice"].keys():
                command = f'gphoto2 --set-config /main/capturesettings/flashcompensation={int(self.flashcompensation["Choice"][value])}'
                self._execute_command_(command)
                answer = 'Done'
            else:
                answer = 'Значение параметра не доступно'
        else:
            answer = 'Параметр доступен только для чтения'
        return answer

    def set_aperture(self, value):
        if not self._is_readonly_(self.aperture):
            if value in self.aperture["Choice"].keys():
                command = f'gphoto2 --set-config /main/capturesettings/aperture={int(self.aperture["Choice"][value])}'
                self._execute_command_(command)
                answer = 'Done'
            else:
                answer = 'Значение параметра не доступно'
        else:
            answer = 'Параметр доступен только для чтения'
        return answer

    def set_focusingpoint(self, value):
        if not self._is_readonly_(self.focusingpoint):
            if value in self.focusingpoint["Choice"].keys():
                command = f'gphoto2 --set-config /main/capturesettings/focusingpoint={int(self.focusingpoint["Choice"][value])}'
                self._execute_command_(command)
                answer = 'Done'
            else:
                answer = 'Значение параметра не доступно'
        else:
            answer = 'Параметр доступен только для чтения'
        return answer

    def set_shutterspeed(self, value):
        if not self._is_readonly_(self.shutterspeed):
            if value in self.shutterspeed["Choice"].keys():
                command = f'gphoto2 --set-config /main/capturesettings/shutterspeed={int(self.shutterspeed["Choice"][value])}'
                self._execute_command_(command)
                answer = 'Done'
            else:
                answer = 'Значение параметра не доступно'
        else:
            answer = 'Параметр доступен только для чтения'
        return answer

    def set_shootingmode(self, value):
        if not self._is_readonly_(self.shootingmode):
            if value in self.shootingmode["Choice"].keys():
                command = f'gphoto2 --set-config /main/capturesettings/shootingmode={int(self.shootingmode["Choice"][value])}'
                self._execute_command_(command)
                answer = 'Done'
            else:
                answer = 'Значение параметра не доступно'
        else:
            answer = 'Параметр доступен только для чтения'
        return answer

    def _set_base_path(self):
        path = os.path.join(os.getcwd(), 'photo')
        command = f'gphoto2 --filename {path}'
        return self._execute_command_(command)

    def _pars_data_(self, data):
        data_dict = {}
        choice = {}
        for line in data:
            if 'Current' in line:
                data_dict['Current'] = line[line.find(':') + 1:].strip()
            elif 'Choice' in line:
                line_data = line[line.find(':') + 1:].split()
                key = line_data[1]
                value = line_data[0]
                choice[key] = value
                data_dict['Choice'] = choice
            elif 'END' in line:
                return data_dict
            else:
                line_data = line.split(':')
                key = line_data[0].strip()
                value = line_data[1].strip()
                data_dict[key] = value

    def _execute_command_(self, command):
        command = command + ' > test.py'
        return os.system(command)

    def _is_readonly_(self, parameter_dict):
        readonly = parameter_dict['Readonly']
        return int(readonly)


if __name__ == '__main__':
    camera = CameraControl()
    camera.get_camera_setting()

    print('ISO', camera.ISO)
    print('white_balance', camera.white_balance)
    print('shooting_mode', camera.shootingmode)
    print('zoom', camera.zoom)
    print('exposure', camera.exposure)
    print('flashcompensation', camera.flashcompensation)
    print('aperture', camera.aperture)
    print('focusingpoint', camera.focusingpoint)
    print('shutterspeed', camera.shutterspeed)
    print('shootingmode', camera.shootingmode)
    print(camera.set_ISO('400'))
    print(camera.set_white_balance('Cloudy'))
    print(camera.set_zoom('3'))
    print(camera.set_exposure('-2/3'))
    print(camera.set_flashcompensation('+1/3'))
    print(camera.set_aperture('1.8'))
    print(camera.set_focusingpoint('Multiple'))
    print(camera.set_shutterspeed('15'))
    print(camera.set_shootingmode('TV'))
