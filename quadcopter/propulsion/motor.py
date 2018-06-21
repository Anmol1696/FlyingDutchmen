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

def get_thrust_per_motor(total_mass, velocity, drag_coff, area_of_frame, density_of_air, g=9.8):
    total_drag = 0.5*density_of_air*velocity**2*area_of_frame*drag_coff
    thrust_per_motor = (total_mass*g + total_drag)/4.0

    return thrust_per_motor
