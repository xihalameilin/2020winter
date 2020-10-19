import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
data = pd.read_csv("totalTime_9.csv", index_col=0)
plot.scatter(data, np.zeros(data.shape[0]))
plot.show()