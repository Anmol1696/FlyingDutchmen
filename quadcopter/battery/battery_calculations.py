"""
    File constists of all the functions that are used for battery calculations
"""

import random

def amp_draw(battery_capacity, discharge_rate):
    return battery_capacity*discharge_rate

def power_calculations(battery_choosen, arm_length):
    power_required = (arm_length/491.0)*13648.0
    return power_required

