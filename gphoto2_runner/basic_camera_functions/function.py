import os
from camera_enumerations import ISO, CaptureType


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

    def set_ISO(self, iso):
        command = f'gphoto2 --set-config /main/imgsettings/iso={iso.value}'
        return self._execute_command_(command)

    def _set_base_path(self):
        path = os.path.join(os.getcwd(), 'photo/test.JPEG')
        command = f'gphoto2 --filename {path}'
        print(command)
        return self._execute_command_(command)

    def _execute_command_(self, command):
        return os.system(command)


if __name__ == '__main__':
    camera = CameraControl()
    camera._set_base_path()
    print(camera._execute_command_('gphoto2 --auto-detect'))
    print(camera.set_ISO(ISO.ISO_80))
    print(camera.capture_image(CaptureType.Save))

    print(camera.set_ISO(ISO.ISO_400))
    print(camera.capture_image(CaptureType.Save))

    print(camera.set_ISO(ISO.ISO_1600))
    print(camera.capture_image(CaptureType.Save))


