import enum
import numbers

class Unit(enum.Enum):
    Meters = 0
    Centimeters = 1
    Inches = 2
    Foot = 3
    Yard = 4

    def __eq__(self, __o):
        if self.__class__ is __o.__class__:
            return self == __o
        try:
            return self.value == __o.value
        except:
            pass
        try:
            if isinstance(__o, numbers.Real):
                return self.value == __o
            if isinstance(__o, str):
                return self.name == __o
        except:
            pass
        return TypeError

def get_cm_multiplier(target):
    conversion = {
        'Meters': 0.01,
        'Centimeters': 1,
        'Inches': 0.393701,
        'Foot': 0.0328084,
        'Yard': 0.0109361
    }
    return conversion[target]

def get_m_multiplier(target):
    conversion = {
        'Meters': 1,
        'Centimeters': 100,
        'Inches': 39.3701,
        'Foot': 3.28084,
        'Yard': 1.09361
    }
    return conversion[target]

def get_in_multiplier(target):
    conversion = {
        'Meters': 0.0254,
        'Centimeters': 2.54,
        'Inches': 1,
        'Foot': 0.0833333,
        'Yard': 0.0277778
    }
    return conversion[target]

def get_ft_multiplier(target):
    conversion = {
        'Meters': 0.3048,
        'Centimeters': 30.48,
        'Inches': 12,
        'Foot': 1,
        'Yard': 0.333333
    }
    return conversion[target]

def get_yrd_multiplier(target):
    conversion = {
        'Meters': 0.9144,
        'Centimeters': 91.44,
        'Inches': 36,
        'Foot': 3,
        'Yard': 1
    }
    return conversion[target]