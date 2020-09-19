import pandas as pd
import numpy as np

##一维数组
date = pd.Series([1, 3, 5, np.nan, 6, 8])

##日期
date2 = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=date2, columns=list('ABCD'))
print(df.to_numpy())

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=date2).shift(2)
print(s)