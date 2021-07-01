import pandas as pd
import os
from pathlib import Path

directory = "./CIC_dataset"
output_path = "shortened_data"
base_path = Path(output_path)
base_path.mkdir(exist_ok=True)




def row_func(row, skip):
    
    if row % skip == 0:
        return False
    else:
        return True
    


for entry in os.scandir(directory):
    data = pd.read_csv(entry, skiprows= lambda x: row_func(x,5), header=None)
    data = data.drop(columns=[0])
    
    
    print(data)
    
    
    data.to_csv("{}/{}".format(output_path, entry.name, 'wb'))