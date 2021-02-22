import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelFile
m= pd.read_excel(r'C:\Users\DELL\Desktop\b value\data.xlsx')
print(m)
earthquake=[]
for j in np.arange(0.1,10.0, 0.1):
    number= m.count(j)
    earthquake.append(number)
    print('number of earthquake at mag', j,' is: ', number)
print(earthquake)