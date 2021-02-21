m=[1,1,1,1,2,2,2,2,2,2,5,5,5,3,3,7,7]
n= len(m)
earthquake=[]
for j in range(1,7):
    number = 0
    for i in range (0,n):
        if m[i]== j:
            number= number+1
    earthquake.append(number)
    print('number of earthquake at mag', j,' is: ', number)
print(earthquake)