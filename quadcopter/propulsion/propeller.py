"""
    Using the data from the Raw CSV file we will form another file which satisfy the points
"""

import pandas
import json

def read_data(raw_csv_file):
    rawdata_frame = pandas.read_csv(raw_csv_file)

    return rawdata_frame

def form_optimal_csv_file(rawdata_frame, output_filename, parameter_filename, columns):
    with open(parameter_filename) as file_open:
        para = json.load(file_open)
    
    final_list = []

    for index, data in rawdata_frame.iterrows():
        if data['d'] > para['max_size_in_inches']:
            continue
        vel = data['j']*data['omega']*data['d']*para['inch_to_meter']/60.0
        power = data['cp']*para['rho']*(data['omega']/60.0)**3*(data['d']*para['inch_to_meter'])**5

        temp_lhs = ((para['m']*para['g']) + (para['rho']*vel**2*para['s']*para['cd']/2))/para['num_rotors']
        temp_rhs = data['ct']*para['rho']*(data['omega']/60.0)**2*(data['d']*para['inch_to_meter'])**4
        if temp_lhs <= temp_rhs:
            print 'power -> ', power
            row = [data['d'], data['pitch'], data['omega'], vel, power, data['j'], data['ct'], data['cp'], data['eta'], data['company']]
            final_list.append(row)
    print 'Solution number ->', len(final_list)
    final_dataframe = pandas.DataFrame.from_records(final_list, columns=columns)
    final_dataframe.to_csv(output_filename, index=False)

if __name__ == "__main__":
    raw_csv_file = "quadcopter/propulsion/data/raw_data.csv"
    output_filename = "quadcopter/propulsion/processed_data/optimal_data.csv"
    parameter_filename = "input_para.json"
    columns = ['d', 'pitch', 'omega', 'velocity', 'power', 'j', 'ct', 'cp', 'eta', 'company']
    df = read_data(raw_csv_file)
    form_optimal_csv_file(df, output_filename, parameter_filename, columns)

