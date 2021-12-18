class Calculator:
    def __init__(self,num1=0):
        self.num1=num1
    def infisum(self,*n):
        self.result=0
        for i in n:
            self.result=self.result+i
        print(self.result)
    def infimultiply(self,*n):
        self.result=1
        for i in n:
            self.result=self.result*i
        print(self.result)
    def infisubtract(self,*n):
        self.result=n[0]
        for i in range(len(n)-1):
            self.result=self.result-n[i+1]
        print(self.result)
    def __truediv__(self,other):
        print(self.num1/other.num1)
k=Calculator()
k.infisum(4,5,2,8,3)
k.infimultiply(3,2,8,1,7)
k.infisubtract(5,3,8,2,1)
k=Calculator(8)
l=Calculator(3)
k/l
'''Output:-
22
336
-9
2.6666666666666665
'''

        
