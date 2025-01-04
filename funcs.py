from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc


def change_volume(value):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume.iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = volume.GetMasterVolumeLevelScalar()

    if isinstance(value, str):
        if value.startswith('+'):
            change = float(value[1:]) / 100
        elif value.startswith('-'):
            change = -float(value[1:]) / 100
        elif value.isnumeric():
            change = float(value) / 100
            current_volume = 0
        else:
            raise ValueError("Некорректный формат значения")
    else:
        raise ValueError("Значение должно быть строкой")

    new_volume = current_volume + change
    new_volume = max(0.0, min(new_volume, 1.0))
    volume.SetMasterVolumeLevelScalar(new_volume, None)

# Примеры использования:
# change_volume('+10')  # Повысить громкость на 10%
# change_volume('-10')  # Понизить громкость на 10%
# change_volume('10')   # Установить громкость на 10%


def change_brightness(value):
    current_brightness = int(sbc.get_brightness()[0])

    if isinstance(value, str):
        if value.startswith('+'):
            change = int(value[1:])
            new_brightness = current_brightness + change
        elif value.startswith('-'):
            change = int(value[1:])
            new_brightness = current_brightness - change
        elif value.isnumeric():
            new_brightness = int(value)
        else:
            raise ValueError("Некорректный формат значения")
    else:
        raise ValueError("Значение должно быть строкой")

    new_brightness = max(0, min(new_brightness, 100))

    sbc.set_brightness(new_brightness)


# Примеры использования:
# change_brightness('+10')  # Повысить яркость на 10 единиц
# change_brightness('-10')  # Понизить яркость на 10 единиц
# change_brightness('50')   # Установить яркость на 50 единиц


def  get_brightness():
    return int(sbc.get_brightness()[0])