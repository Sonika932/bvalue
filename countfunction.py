import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from pandas import ExcelFile
m= pd.read_excel(r'C:\Users\DELL\Desktop\b value\data.xlsx')
print(m)
magnitude= np.arange(0.1,7.1,0.1)
print(magnitude)
earthquake=[]
for j in magnitude:
    number= np.count_nonzero(m==j)
    earthquake.append(number)
    print('number of earthquake at mag', j,' is: ', number)
print(earthquake)
n= len(earthquake)
cummulative=[]
a=0
for i in earthquake:
    a=a+i
    cummulative.append(a)
print('cummulative number of earthquakes:', cummulative)
y=[]
for i in cummulative:
    if i==0:
        b=0
        y.append(b)
    else:
        b= math.log10(i)
        y.append(b)
print(y)
plt(magnitude,y)
