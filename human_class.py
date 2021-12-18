class Human:
    def __init__(self,name=None,sex=None,age=None,height=None,weight=None,colour=None,character=None):
        self.name=name
        self.sex=sex
        self.age=age
        self.height=height
        self.weight=weight
        self.colour=colour
        self.character=character
    def display(self):
        print('Name=',self.name,'Sex=',self.sex,'Age=',self.age,'Height=',self.height,'Weight=',self.weight,'Colour=',self.colour,'Character=',self.character)
class Employee(Human):
    def display(self):
        print("Employee details:\n")
        super().display()
class Student(Human):
    def display(self):
        print("Student details:\n")
        super().display()
class Govt_emp(Employee):
    def display(self):
        print("Govt",end=" ")
        super().display()
class Private_emp(Employee):
    def display(self):
        print("Private",end=" ")
        super().display()
a=Employee()
a.name='David'
a.age='19'
a.sex='male'
a.height='5.6'
a.weight='65'
a.colour='Black'
a.character='Good'
a.display()
a=Student()
a.name='David'
a.age='19'
a.sex='male'
a.height='5.6'
a.weight='65'
a.colour='Black'
a.character='Good'
a.display()
a=Govt_emp()
a.name='David'
a.age='19'
a.sex='male'
a.height='5.6'
a.weight='65'
a.colour='Black'
a.character='Good'
a.display()
a=Private_emp()
a.name='David'
a.age='19'
a.sex='male'
a.height='5.6'
a.weight='65'
a.colour='Black'
a.character='Good'
a.display()

'''Output:-

Employee details:

Name= David Sex= male Age= 19 Height= 5.6 Weight= 65 Colour= Black Character= Good
Student details:

Name= David Sex= male Age= 19 Height= 5.6 Weight= 65 Colour= Black Character= Good
Govt Employee details:

Name= David Sex= male Age= 19 Height= 5.6 Weight= 65 Colour= Black Character= Good
Private Employee details:

Name= David Sex= male Age= 19 Height= 5.6 Weight= 65 Colour= Black Character= Good

'''
