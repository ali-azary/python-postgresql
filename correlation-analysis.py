import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

# Load the EIS data from the CSV file
data = pd.read_csv('EIS.csv',index_col=0)
# print(data.columns)
# print(data.head(10))
CN=2.9
data['SoH'] = pd.to_numeric((CN+data['AhAccu'])/CN*100,errors='coerce')
# Extract the impedance values and frequency data
data['Zreal1'] = pd.to_numeric(data['Zreal1'], errors='coerce')
data['Zimg1'] = pd.to_numeric(data['Zimg1'], errors='coerce')
data['ActFreq'] = pd.to_numeric(data['ActFreq'], errors='coerce')
data['U1'] = pd.to_numeric(data['U1'], errors='coerce')

data.to_csv('test.csv')
exit()
data=data[['U1','Zreal1','Zimg1','ActFreq','Resistance','Capacitance','Inductance']]
# Calculate the correlation matrix
corr_matrix = data.corr()

# Visualize the correlation matrix using a heatmap
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True)
plt.title('Correlation Matrix')
plt.show()

# Select highly correlated features with SOC for further analysis
soc_corr_features = corr_matrix['U1'][abs(corr_matrix['U1']) > 0.5].index.tolist()
print('Highly correlated EIS features with SOC of the battery:', soc_corr_features)

