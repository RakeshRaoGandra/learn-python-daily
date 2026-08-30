# object oriented programming
# class,object,encapsilation,polymorphism
#inheritance , abstraction

#
# class : class is a blue print 
# Objects
# creating the calss and object
class Madam:
    # creating a consistor
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def student_details(self):
        print(f'hi {self.name},your roll number is{self.roll_no}')

    def ece (self):
        print("ece")
    def cse(self):
        print("computer")
# calling the object of any method 
student =Madam("nandini",234)
student.ece()
student.student_details()