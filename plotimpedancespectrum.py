import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('EIS.csv',index_col=0)
CN=2.9
df['SoH'] = pd.to_numeric((CN+df['AhAccu'])/CN*100,errors='coerce')

# Group the data by SoH values
groups = df.groupby(df['SoH'].round(0))
for name, group in groups:
    print(f'SoH: {name}, Rows: {len(group)}')
# Define the SoH values of interest
soh_values = [30, 50, 70, 90]

# Loop over each SoH value and create a scatter plot for that group
for soh in soh_values:
    group = groups.get_group(soh)
    plt.scatter(group['Zreal1'], -1*group['Zimg1'], label=soh)

# Add labels and legend
plt.xlabel('Zreal1')
plt.ylabel('Zimg1')
plt.legend(title='SoH', loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
# Show the plot
plt.savefig('impedance_soh.jpg')