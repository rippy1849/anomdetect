import os
import pandas as pd
from pathlib import Path
import numpy as np

CIC_data_folder = "./CIC_dataset"
output_folder = "./shortened_data"
base_path = Path(output_folder).mkdir(exist_ok=True)


def skipfunc(index_num):
    if index_num%8 == 0:
        return False
    else:
        return True


for entry in os.scandir(CIC_data_folder):
    input_data = pd.read_csv(entry,skiprows=lambda x: skipfunc(x), header=None)
    #input_data = input_data.drop([0])
    print(input_data)
    with open("{}/{}".format(output_folder, entry.name), 'wb') as outfile:
        input_data.to_csv(outfile)




    
    
    