"""
    Script has all the functions for deciding the motors
"""

import math

def motor_power_required(thrust, density_of_air, diameter_of_propeller):
    area_of_rotor_disk = math.pi*diameter_of_propeller**2/4.0
    return math.sqrt(thrust**3/(2.0*density_of_air*area_of_rotor_disk))

def motor_induced_velocity(thrust, density_of_air, diameter_of_propeller):
    area_of_rotor_disk = math.pi*diameter_of_propeller**2/4.0
    return math.sqrt(thrust/(2.0*density_of_air*area_of_rotor_disk))

