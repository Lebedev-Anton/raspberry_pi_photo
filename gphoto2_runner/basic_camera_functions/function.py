import os
from .camera_enumerations import ISO, CaptureType, WhiteBalance, ShootingMode


class CameraControl:
    def capture_image(self, type_capture):
        if type_capture == CaptureType.Base:
            command = 'gphoto2 --capture-image'
        else:
            command = 'gphoto2 --capture-image-and-download'
        return self._execute_command_(command)

    def get_ISO(self):
        command = f'gphoto2 --get-config /main/imgsettings/iso'
        return self._execute_command_(command)

    def get_white_balance(self):
        command = f'gphoto2 --get-config /main/imgsettings/whitebalance'
        return self._execute_command_(command)

    def get_zoom(self):
        command = f'gphoto2 --get-config /main/capturesettings/zoom'
        return self._execute_command_(command)

    def get_exposure(self):
        command = f'gphoto2 --get-config /main/capturesettings/exposurecompensation'
        return self._execute_command_(command)

    def get_flashcompensation(self):
        command = f'gphoto2 --get-config /main/capturesettings/flashcompensation'
        return self._execute_command_(command)

    def get_aperture(self):
        command = f'gphoto2 --get-config /main/capturesettings/aperture'
        return self._execute_command_(command)

    def get_focusingpoint(self):
        command = f'gphoto2 --get-config /main/capturesettings/focusingpoint'
        return self._execute_command_(command)

    def get_shutterspeed(self):
        command = f'gphoto2 --get-config /main/capturesettings/shutterspeed'
        return self._execute_command_(command)

    def get_shootingmode(self):
        command = f'gphoto2 --get-config /main/capturesettings/shootingmode'
        return self._execute_command_(command)

    def set_ISO(self, iso):
        iso = ISO[iso]
        command = f'gphoto2 --set-config /main/imgsettings/iso={iso.value}'
        return self._execute_command_(command)

    def set_white_balance(self, wb):
        wb = WhiteBalance[wb]
        command = f'gphoto2 --set-config /main/imgsettings/whitebalance={wb.value}'
        return self._execute_command_(command)

    def set_zoom(self, value):
        value = int(value)
        if value < 0:
            value = 0
        if value > 19:
            value = 19
        command = f'gphoto2 --set-config /main/capturesettings/zoom={value}'
        return self._execute_command_(command)

    def set_exposure(self, value):
        value = int(value)
        if value < 0:
            value = 0
        if value > 12:
            value = 12
        command = f'gphoto2 --set-config /main/capturesettings/exposurecompensation={value}'
        return self._execute_command_(command)

    def set_flashcompensation(self, value):
        value = int(value)
        if value < 0:
            value = 0
        if value > 12:
            value = 12
        command = f'gphoto2 --set-config /main/capturesettings/flashcompensation={value}'
        return self._execute_command_(command)

    def set_aperture(self, value):
        value = int(value)
        if value < 0:
            value = 0
        if value > 54:
            value = 54
        command = f'gphoto2 --set-config /main/capturesettings/aperture={value}'
        return self._execute_command_(command)

    def set_focusingpoint(self, value):
        value = int(value)
        if value < 0:
            value = 0
        if value > 1:
            value = 1
        command = f'gphoto2 --set-config /main/capturesettings/focusingpoint={value}'
        return self._execute_command_(command)

    def set_shutterspeed(self, value):
        value = int(value)
        if value < 0:
            value = 0
        if value > 75:
            value = 75
        command = f'gphoto2 --set-config /main/capturesettings/shutterspeed={value}'
        return self._execute_command_(command)

    def set_shootingmode(self, mode):
        mode = ShootingMode[mode]
        command = f'gphoto2 --set-config /main/imgsettings/whitebalance={mode.value}'
        return self._execute_command_(command)

    def _set_base_path(self):
        path = os.path.join(os.getcwd(), 'photo')
        command = f'gphoto2 --filename {path}'
        return self._execute_command_(command)

    def _execute_command_(self, command):
        return os.system(command)
