import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import os
import fnmatch
import csv

folder_path = "Panasonic 18650PF Data"
EISfiles=[]
for root, dirs, files in os.walk(folder_path):
    for dir in dirs:
        if dir == "EIS":
            eis_folder_path = os.path.join(root, dir)
            for filename in fnmatch.filter(os.listdir(eis_folder_path), "*.csv"):
                csv_path = os.path.join(eis_folder_path, filename)
                EISfiles.append(csv_path)

data = pd.concat((pd.read_csv(f, skiprows=29) for f in EISfiles), ignore_index=True)
data = data[pd.to_numeric(data['Step'],errors='coerce').notnull()]
data.to_csv('EIS.csv')