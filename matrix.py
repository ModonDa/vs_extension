from sympy import *
import numpy as np
class Matrix_op:
    def __init__(self):
        self.m1=Matrix([[3,2,6],[5,7,-2],[9,4,1]])
        self.m2=Matrix([[7,1,3],[3,9,2],[8,4,5]])
        self.inverse()
        self.add()
        self.subtract()
        self.multiply()
    def inverse(self):
        print("\nInverse is:\n")
        print(self.m1.inv())
        print('\n')
        print(self.m2.inv())
    def add(self):
        print("\nAddition is:\n")
        print(np.add(self.m1,self.m2))
    def subtract(self):
        print("\nSubtractiion is:\n")
        print(np.subtract(self.m1,self.m2))
    def multiply(self):
        print("\nMultiplication is:\n")
        print(np.dot(self.m1,self.m2))
Matrix_op()
        
'''Output:-

Inverse is:

Matrix([[-15/259, -22/259, 46/259], [23/259, 51/259, -36/259], [43/259, -6/259, -11/259]])


Matrix([[37/80, 7/80, -5/16], [1/80, 11/80, -1/16], [-3/4, -1/4, 3/4]])

Addition is:

[[10 3 9]
 [8 16 0]
 [17 8 6]]

Subtractiion is:

[[-4 1 3]
 [2 -2 -4]
 [1 0 -4]]

Multiplication is:

[[75 45 43]
 [40 60 19]
 [83 49 40]]

 '''
