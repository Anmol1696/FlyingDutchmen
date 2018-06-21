"""
    This file contains cost function calculation
"""

import math

def get_number_of_rounds(range_diameter, height_of_operration, field_angle):
    return math.ceil(range_diameter/(2.0*height_of_operration*math.tan(field_angle*math.pi/(2.0*180.0))))

def time_calculation(num_of_rounds, height_of_operration, field_angle, velocity):
    """
        Returns the cost function value for the exploration phase
        This minimizes the time taken for exploration
        field_angle is in degrees
    """
    final_result = 0

    for i in range(num_of_rounds):
        temp_num = (2*math.pi*height_of_operration*math.tan(field_angle*math.pi/360.0)*(2*i - 1))
        final_result += temp_num/(velocity*1.0)

    return final_result

def exploration_phase_cost(range_diameter, height_of_operration, field_angle, velocity):
    number_of_rounds = int(get_number_of_rounds)
    return time_calculation(number_of_rounds, height_of_operration, field_angle, velocity)

if __name__ == "__main__":
    """
        Testing above functions
    """
    range_diameter = 1000
    height_of_operration = 20
    field_angle = 120
    velocity = 10

    number_of_rounds = int(get_number_of_rounds(range_diameter, height_of_operration, field_angle))
    result = time_calculation(number_of_rounds, height_of_operration, field_angle, velocity)

    print 'Number of rounds ->', number_of_rounds
    print 'Cost function value ->', (result)/(60*60.0)
