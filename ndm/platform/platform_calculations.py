"""
    Script consists of all the fucntions related to platform box
"""

import math

def required_horizontal_velocity(fishnet_area, height_of_operation, g=9.8):
    return (g*math.sqrt(fishnet_area))/(2.0*math.sqrt(2.0*height_of_operation))

def get_height_of_platform(horizontal_velocity, platform_angle, g=9.8):
    """
        Platform angle is in degrees
    """
    angles_velocity = horizontal_velocity/math.cos(platform_angle*math.pi/180.0)
    return (7.0*angles_velocity**2)/(10.0*g)

def main_platform(fishnet_area, height_of_operation=25, g=9.8):
    """
        This is the ouput that gives all the outputs
    """
    platform_angle = 45.0
    horizontal_velocity = required_horizontal_velocity(fishnet_area, height_of_operation)
    platform_height = get_height_of_platform(horizontal_velocity, platform_angle)
    platform_length = platform_height/math.sin(platform_angle*math.pi/180.0)
    platform_base = platform_height/math.tan(platform_angle*math.pi/180.0)

    return platform_length, platform_base, platform_height, platform_angle

if __name__ == "__main__":
    fishnet_area = 29.43/2.0
    height_of_operation = 25

    l,b,h,a = main_platform(fishnet_area, height_of_operation)
    
    print 'Platform'
    print 'Length ->', l, 'Base ->', b, ' height ->', h, ' angle ->', a
