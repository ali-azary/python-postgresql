import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = pd.read_csv('EIS.csv',index_col=0)
CN=2.9
data['SoH'] = pd.to_numeric((CN+data['AhAccu'])/CN*100,errors='coerce')

data[['Zreal1', 'Zimg1', 'ActFreq','ChamberT']] = data[['Zreal1', 'Zimg1', 'ActFreq','ChamberT']].astype(float)



X = data[['Zreal1', 'Zimg1','ActFreq','ChamberT']]
y = data['SoH']

# Drop NaN values from X and y
X = X.dropna()
y = y.dropna()

if X.shape[0] < y.shape[0]:
    y = y[:X.shape[0]] # crop y to the same length as X
else:
    X = X[:y.shape[0]] # crop X to the same length as y


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

kernel = 1.0 * RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0)) \
    + WhiteKernel(noise_level=1.0, noise_level_bounds=(1e-10, 1e+1))

gpr = GaussianProcessRegressor(kernel=kernel, alpha=0.1, n_restarts_optimizer=10, random_state=42)
gpr.fit(X_train, y_train)

y_pred = gpr.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("Mean squared error: {:.2f}".format(mse))

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.plot([0, 1], [0, 1], transform=ax.transAxes, ls="--", c=".3")
ax.set_xlabel('Actual SoH')
ax.set_ylabel('Predicted SoH')
plt.savefig('predict.jpg')
