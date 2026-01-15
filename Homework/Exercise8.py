import pandas as pd
import numpy as np

#Exercise 1
mat1=pd.read_csv('example.csv',index_col=0)
print(mat1)

mat2=mat1.apply(lambda x: x+5) #bonus of 5
mat2[mat2>30]=30 #over 30 = 30
print(mat2)

mat2.to_csv('bonus_scores.csv') #save data

mat2.plot(subplots=True, kind='hist') #plot histogram

#Exercise 2
mat3=pd.read_csv('cars.csv',index_col=0)
print(mat3)

mat4=mat3.drop(1993,axis='rows') #drop row 3
print(mat4)

mat4.insert(1,"Price",[8000, 6500, 6800, 7500, 7300, 7000, 9000, 6500, 7800]) #newcolumn named Price
print(mat4)

print("mean length=",mat4["Length"].mean())#average length

print("median price=",mat4["Price"].median())#median price

mat5=mat4.drop(mat4[mat4.Price<7000].index)#contains only rows where Price>7000
print(mat5)

mat5.sort_values(by=['Price'],inplace=True,ascending=False)#sort descending by Price
print(mat5)

#Exercise 3
arr=np.random.randint(100,size=(50,50)) #random matrix
print(arr)

np.savetxt("random_ints.csv",arr,delimiter=",") #save to file
arr2=np.genfromtxt("random_ints.csv",delimiter=",") #read w numpy
print("numpy mean=",np.mean(arr2))
print("numpy stdv=",np.std(arr2))

arr3=pd.read_csv('random_ints.csv',header=None)#read with pandas
print("pandas mean=",arr3.stack().mean())
print("pandas stdv=",arr3.stack().std())