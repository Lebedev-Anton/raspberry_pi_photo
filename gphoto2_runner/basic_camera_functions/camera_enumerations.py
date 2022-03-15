from enum import Enum


class ISO(Enum):
    AUTO = 0
    ISO_80 = 1
    ISO_100 = 2
    ISO_200 = 3
    ISO_400 = 4
    ISO_800 = 5
    ISO_1600 = 6


class CaptureType(Enum):
    Base = 'base'
    Save = 'save'


class WhiteBalance(Enum):
    Auto = 0
    Daylight = 1
    Cloudy = 2
    Tungsten = 3
    Fluorescent = 4
    Fluorescent_H = 5
    Unknown = 6
    Custom = 7


class ShootingMode(Enum):
    Auto = 0
    TV = 1
    AV = 2
    Manual = 3

