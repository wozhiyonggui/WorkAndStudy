import numpy as np
import pandas as pd
import xlwings as xw

data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a1', 'a2', 'a3'], index=['r1', 'r2', 'r3'])
a = data[['a1', 'a2']]
print(a)
b = data.iloc[1:2]
print(b)

'''data.to_excel('1.xlsx', sheet_name='1')'''















