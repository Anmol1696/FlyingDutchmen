"""
    Codes for fixing the structure of the quad
"""

import random

def fixing_structure(input_data, data=False):
    arm_length = random.randint(430, 500)
    frame_weight = arm_length*2.06/491.0

    if data == True:
        return 491.0, 2.06
    return arm_length, frame_weight

