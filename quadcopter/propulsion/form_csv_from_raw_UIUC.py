"""
    Script forms a CSV file with columns -> D | Pitch | Omega | J | C_t | C_p | eta
    We use Pandas for formation of a Raw csv file with unprocessed data
"""

import pandas
import sys
import os

def get_j_ct_cp_eta_from_txt(folder_name, file_name):
    with open(folder_name + file_name) as file_open:
        all_lines = file_open.readlines()
    
    final_rows = [map(float, line.strip().split()) for line in all_lines[1:]]
    
    return final_rows

def read_files_and_form_csv(raw_txt_folder_name, columns, output_file_name):
    all_file_names = os.listdir(raw_txt_folder_name)

    data_list = []

    for file_name in all_file_names:
        try:
            file_split = file_name[:-4].split('_')
            print file_split  
            if not file_split[-1].isdigit():
                continue

            j_ct_cp_eta = get_j_ct_cp_eta_from_txt(raw_txt_folder_name, file_name)

            d, pitch = map(float, file_split[1].split('x'))
            omega = int(file_split[-1])
            company = file_split[0]

            for each_row in j_ct_cp_eta:
                print "Row -> ", [d,pitch,omega]+each_row
                data_list.append([d,pitch,omega]+each_row+[company])
        except:
            pass

    print "Now forming DataFrame"
    data_frame = pandas.DataFrame.from_records(data_list, columns=columns)
    print "Writing to File"
    data_frame.to_csv(output_file_name, index=False)

if __name__ == "__main__":
    data_folder_name = "raw_data/UIUC-propDB/volume-2/data/"
    columns = ['d', 'pitch', 'omega', 'j', 'ct', 'cp', 'eta', 'company']
    output_file_name = "processed_data_2/raw_data.csv"

    read_files_and_form_csv(data_folder_name, columns, output_file_name)
    

