import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import ExcelFile
m= pd.read_excel(r'C:\Users\DELL\Desktop\b value\data.xlsx')
print(m)
n= len(m)
earthquake=[]
j= 0.1
for j in range(0.1,10.0, 0.1):
    number = 0
    for i in range (0,n):
        if m[i]== j:
            number= number+1
    earthquake.append(number)
    print('number of earthquake at mag', j,' is: ', number)
print(earthquake)