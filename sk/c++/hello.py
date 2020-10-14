import pandas as pd
import numpy as np


data = pd.read_csv(r"C:\Users\hp\PycharmProjects\2020winter\sk\c++\csv\totalTime.csv", index_col=0)
data = data['totalTime']
data = np.array(data).reshape(-1, 1)
print(data)
