import numpy as np

class MyMatrix:
    
    def __init__(self,matrix,N=3):
        self.N=N
        self.matrix=np.random.randint(10,size=(self.N,self.N))
        print(self.matrix)
        
    def inverse(self):
        return np.linalg.inv(self.matrix)
    
    def determinant(self):
        return np.linalg.det(self.matrix)
        
    def eigenvalues(self):
        return np.linalg.eig(self.matrix)

N=4
print("matrix1:")
matrix1=MyMatrix(4) #creates a square matrix
print("matrix2:")
matrix2=MyMatrix(4)
print("matrix inv:")
print(matrix1.inverse())
print("matrix det:")
print(matrix1.determinant())
print("matrix eigen:")
print(matrix1.eigenvalues())
print("matrix sum:")
#print(matrix1+matrix2)
print("matmul:")
#print(matrix1*matrix2) 