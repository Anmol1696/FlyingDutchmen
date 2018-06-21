"""
    File constists of all the functions that are used for battery calculations
"""

def amp_draw(battery_capacity, discharge_rate):
    return battery_capacity*discharge_rate
