import gphoto2 as gp
camera = gp.Camera()
camera.init()
text = camera.get_summary()

print(camera.get_config().set_info)
print('____________________')
x = camera.capture()
for attr in dir(x):
    if not attr.startswith('_'):  # Если не внутренний и не служебный
        print(attr, getattr(x, attr))