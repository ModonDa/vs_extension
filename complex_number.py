class Complex_number:
    def __init__(self,real,img):
        self.real=real
        self.imag=img
    def __mul__(self,other):
        return Complex_number(self.real*other.real-self.imag*other.imag,self.real*other.imag+self.imag*other.real)
    def __str__(self):
        if self.imag>0:
            return ('{}+{}i').format(self.real,self.imag)
        else:
            return ('{}{}i').format(self.real,self.imag)
    def __add__(self,other):
        return Complex_number(self.real+other.real,self.imag+other.imag)
    def __truediv__(self,other):
        return Complex_number((self.real*other.real+self.imag*other.imag)/(pow(other.real,2)+pow(other.imag,2)),
                              (self.imag*other.real-self.real*other.imag)/(pow(other.real,2)+pow(other.imag,2)))
    def __sub__(self,other):
        return Complex_number(self.real-other.real,self.imag-other.imag)
                                                                                                                 
        
a=Complex_number(2,3)
b=Complex_number(3,-5)
print(a-b)
print(a+b)
print(a*b)
print(a/b)
''' Output:-
-1+8i
5-2i
21-1i
-0.2647058823529412+0.5588235294117647i
'''
