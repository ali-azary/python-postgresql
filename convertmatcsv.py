import os
import fnmatch
from scipy.io import loadmat
import pandas as pd
import sys
import numpy as np
from datetime import datetime

# Define the folder to search
folder_path = 'Panasonic 18650PF Data'

# Define the pattern to match against
pattern = '*.mat'

'''
Data columns:
TimeStamp (timestamp in MM/DD/YYYY HH:MM:SS AM format)
Voltage (measured cell terminal voltage, sense leads welded directly to battery terminal)
Current (measure current in amps)
Ah (measured amp-hours, with Ah counter reset before each charge, test, or drive cycle)
Wh (measured watt-hours, with Wh counter reset after each charge, test, or drive cycle)
Power (measure power in watts)
Battery_Temp_degC (battery case temperature, at middle of battery, in degrees Celsius measured with a thermocouple, measurement corrected for thermocouple offset at lower temperatures)
Time (time in seconds, starts at zero at beginning of each data file)
Chamber_Temp_degC (measured chamber temperature in degrees Celsius)
'''

# Loop through all the files and folders in the specified folder
for root, dirs, files in os.walk(folder_path):
    # Loop through all the files in this folder
    for filename in fnmatch.filter(files, pattern):
        # Construct the full file path
        file_path = os.path.join(root, filename)
        file_name = os.path.splitext(file_path)[0] + '.csv'
        # Do something with the file path (e.g. print it)
        print(file_path)
        
        mat=loadmat(file_path)
        data=mat[list(mat.keys())[-1]][0]
        data = [d[:,0] for d in data[0]]
        df = pd.DataFrame(np.array(data).T, columns=['TimeStamp', 'Voltage', 'Current', 'Ah', 'Wh', 'Power', 'Battery_Temp_degC', 'Time', 'Chamber_Temp_degC'])
        df.TimeStamp = [x[0] for x in df.TimeStamp]
        try:
            df['TimeStamp'] = pd.to_datetime(df['TimeStamp'], format='%m/%d/%Y %I:%M:%S %p')
        except:
            df['TimeStamp'] = pd.to_datetime(df['TimeStamp'], format='%m/%d/%Y', errors='coerce')

        df.to_csv(file_name)