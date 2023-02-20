# SOH-from-EIS
State of Health of Li-ion batteries from Electrochemical Impedance Spectroscopy
the data taken from https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/wykht8y7tg-1.zip
first data is converted and cleaned into properly-formatted csv files. I also added it into a postgre SQL database using a python script. 
All the EIS data are combined into one file and used with GPR ML model to predict SoH with SoH, impedance, frenquency, and temperature data at hand. SoH values are calulated using nominal capacity and current Ah values.

![impedance_soh](https://user-images.githubusercontent.com/69943289/220211707-5efa3aa7-4b40-4761-ac46-2bb4932c3717.jpg)

![predict](https://user-images.githubusercontent.com/69943289/219979696-e989ce2c-4a56-425b-8c02-bb50b3be4c60.png)

![postgresql](https://user-images.githubusercontent.com/69943289/220211952-e3171a1c-eae7-43df-849f-fc87f95ea0d5.jpg)
