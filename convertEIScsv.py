import os
import fnmatch
import csv

folder_path = "Panasonic 18650PF Data"

for root, dirs, files in os.walk(folder_path):
    for dir in dirs:
        if dir == "EIS":
            eis_folder_path = os.path.join(root, dir)
            for filename in fnmatch.filter(os.listdir(eis_folder_path), "*.csv"):
                csv_path = os.path.join(eis_folder_path, filename)
                
                print(csv_path)
                
                with open(csv_path,'r') as file:
                    lines=file.readlines()
                for i in range(len(lines)):
                    lines[i] = lines[i].replace(';', ',')
                with open(csv_path, 'w', newline='') as new_file:
                    writer = csv.writer(new_file)
                    for line in lines:
                        writer.writerow(line.strip().split(','))               
                