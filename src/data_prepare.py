import pandas as pd
import os
# pd.read_csv(r'../data/Project_Data_EE4C12_S&S_EMG.csv').to_csv('data.csv', index=False)
print(os.getcwd())
data_raw = pd.read_csv(r'data\Project_Data_EE4C12_S&S_EMG.csv')
data_raw.head()


