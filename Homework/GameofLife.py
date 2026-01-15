import numpy as np
import matplotlib.pyplot as plt

arr=np.genfromtxt("ships.txt").transpose()
#arr=np.random.randint(2,size=(50,50))
width=arr.shape[1]
height=arr.shape[0]
newarr=np.genfromtxt("ships.txt").transpose()

plt.axis([0,width-1,0,height-1])
plt.imshow(arr, interpolation='nearest')
plt.pause(0.5)
for n in range(1,100): #iterations
    for i in range(0,height-1): #array rows
        for j in range (0,width-1): #array columns
            count=arr[i-1,j-1]+arr[i+1,j+1]+arr[i-1,j]+arr[i,j-1]+arr[i+1,j]+arr[i,j+1]+arr[i-1,j+1]+arr[i+1,j-1]
            if (arr[i,j]==1): #if alive
                if (count==2 or count==3):
                    newarr[i,j]=1
                elif (count>3):
                    newarr[i,j]=0
                else:
                    newarr[i,j]=0
                    
            else: #if dead
                if (count==3):
                    newarr[i,j]=1
                else:
                    newarr[i,j]=0
                    
        #arr[i,0]=arr[i,width-1]
        #arr[i,width-1]=arr[i,0]
    arr=newarr.copy()
    plt.axis([0,width-1,0,height-1])
    plt.imshow(arr, interpolation='nearest')
    plt.pause(0.001)
plt.show()

'''
            if (j!=0):
                count=count+arr[i,j-1]
                if (i!=0):
                    count=count+arr[i-1,j-1]
                if (i!=width-1):
                    count=count+arr[i+1,j-1]
            if (j!=width-1):
                count=count+arr[i,j+1]
                if (i!=0):
                    count=count+arr[i-1,j+1]
                if (i!=width-1):
                    count=count+arr[i+1,j+1]
            if (i!=0):
                count=count+arr[i-1,j]
            if (i!=width-1):
                count=count+arr[i+1,j]
'''