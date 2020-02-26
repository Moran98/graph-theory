# Aaron Moran
# Practice using classes in Python

class Student:
    # Member variables
    name = None
    age = None
    course = None

    print("GMIT")
    print("----")

    def __init__(self, name=None, age=None, course=None):
        self.name= name
        self.age = age
        self.course = course
    
    # Constructor to fill out details
    def form(self):
        self.name = input("Enter your name : ")
        self.age = input("Enter your age : ")
        self.course = input("Enter your course : ")

# Create a student object
s1 = Student()
s1.form()
print("----------------------------------------")
print("Your name is : ", s1.name)
print("Your age is : ", s1.age)
print("Your course is : ", s1.course)
s1 = Student(name='Aaron', age=20, course='Software')
print(s1)
