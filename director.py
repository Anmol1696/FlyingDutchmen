"""
    This script includes the data for performing iterations for fixed XDSM
"""

from quadcopter.structure.cantilever_beam       import fixing_structure
from quadcopter.propulsion.propeller            import fixing_propeller
from quadcopter.battery.battery_calculations    import power_calculations
from ndm.barenet.net_finalization               import choosing_net
from ndm.platform.platform_calculations         import main_platform

import json
import time

def read_json_file(file_name):
    with open(file_name) as file_open:
        json_data = json.load(file_open)

    return json_data

def each_iteration(input_data):
    arm_length, frame_weight = fixing_structure(input_data)
    print 'Arm length ->', arm_length, ' Frame Weight ->', frame_weight
    fixed_propeller = fixing_propeller(input_data, 'quadcopter/propulsion/input_pera.json')
    power_required = power_calculations(input_data, arm_length)
    print 'Total power required ->', power_required
    net_area = choosing_net(input_data, arm_length)
    print 'Net Area ->', net_area
    platform_length, platform_base, platform_height, platform_angle = main_platform(net_area/2)
    print 'Platform ->\n'
    print 'Platform length->', platform_length, 'Base ->', platform_base, 'Height ->', platform_height, 'Angle ->', platform_angle

def main(input_file_name):
    input_data = read_json_file(input_file_name)

    print "First Iteration......"
    each_iteration(input_data)

    for iteration in range(1,10):
        print 'Iteration ->', iteration
        try:
            each_itereation(input_data)
        except:
            time.sleep(1)

    print '--**--'*12
    print 'Final Iteration'
    arm_length, frame_weight = fixing_structure(input_data, True)
    print 'Arm length ->', arm_length, ' Frame Weight ->', frame_weight
    fixed_propeller = fixing_propeller(input_data, 'quadcopter/propulsion/input_para.json')
    power_required = power_calculations(input_data, arm_length)
    print 'Total power required ->', power_required
    net_area = choosing_net(input_data, arm_length)
    print 'Net Area ->', net_area
    platform_length, platform_base, platform_height, platform_angle = main_platform(net_area/2)
    print 'Platform ->'
    print 'Platform length->', platform_length, 'Base ->', platform_base, 'Height ->', platform_height, 'Angle ->', platform_angle

if __name__ == "__main__":
    main('optimization_inputs.json')
    
