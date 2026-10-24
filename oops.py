class Student():
    def __init__(self,name):
        self.name=name
#         print("adding new name")
s1=Student("hassan")
print(s1.name)
class Person():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg score is",sum/3)
s1=Person("hassan",[86,98,87])
s1.get_avg()
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("DOG is barking")
class Duck(Animal):
    def duck(self):
        print("duck is eating")
d=Dog()
e=Duck()
d.eat()
d.bark()
e.duck()
class Animal:
    def eat(self):
        print("Animalis eating")
class Dog(Animal):
    def bark(self):
        print("dog id barking")
class Duck(Animal):
    def duck(self):
        print("duck is eating")
p=Dog()
d=Duck()
a=Animal()
a.eat()
d.duck()
p.bark()
class Father:
    def drive(self):
        print("Father can driving")
class Mother:
    def cook(self):
        print("Mother can cook")
class Child(Father,Mother):
    pass
child=Child()
child.drive()
child.cook()
class Teacher:
    def teacher(self):
        print("Teacher teach students")
class Researcher:
    def researcher(self):
     print("Researcher does research")
class Professor(Teacher,Researcher):
    def lecture(self):
        print("professor gives a lecture")
p1=Professor()
p1.teacher()
p1.researcher()
p1.lecture()
class Computer:
    def show_computer(self,brand):
        print("computer brand is",brand)
class Ai:
    def ai_model(self,model):
        print("Ai model",model)
class AIRobot(Computer,Ai):
    def robot_name(self,name):
        print("robot name",name)
robot=AIRobot()
robot.show_computer("Dell")
robot.ai_model("Gpt")
robot.robot_name("Robox")
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def show_info(self):
        print(f"my name is {self.name} , age is{self.age} and my marks is {self.marks}" )
        if self.marks>=400:
            print(self.marks,"pass") 
s1=Student("hassan",16,500)
s1.show_info()
class Singer:
    def __init__(self,singer):
        self.singer=singer
        
class Actor:
    def __init__(self,actor):
        self.actor=actor
class Both(Singer,Actor):
    def __init__(self, singer,actor):
        Singer.__init__(self,singer)
        Actor.__init__(self,actor)
        
b1=Both("billie eilish","tom haland")
print(b1.singer)
print(b1.actor)
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
class Athelete:
    def __init__(self,sport):
        self.sport=sport
class StudentAthelete(Student,Athelete):
    def __init__(self, name, roll_no,sport):
        Student.__init__(self,name,roll_no)
        Athelete.__init__(self,sport)
st=StudentAthelete("hassan","25","cricket")
print(st.name)
print(st.roll_no)
print(st.sport)
# polymorphism
class Name:
    def show_info(self):
        print("Hassan")
class Age(Name):
    def show_info(self):
        print(16)
class Study(Age):
    def show_info(self):
        print("AI/ml")
s1=Name()
s1.show_info()
s2=Age()
s2.show_info()
s3=Study()
s3.show_info()
class Father:
    def __init__(self):
        print("Father constructor")
    def driving(self):
        print("Father can drive")
class Mother:
    def __init__(self):
        print("Mother constructor")
    def cooking(self):
        print("Mother can cook")
class Child(Father,Mother):
    pass
c=Child()
c.driving()
c.cooking()
class Name:
    @staticmethod
    def show_info():
        print("my name is hassan")
Name.show_info()
class Calculator:
    def add(self,a,b,c=0):
        return a+b+c    
c=Calculator()
print(c.add(2,3))
print(c.add(2,3,4))
class Student:
# protected
    def __init__(self,name,age,houseno):
        self.__name=name
        self.age=age
        self.houseno=houseno
    def show_info(self):
        print(self.__name)
s1=Student("Haasan",16,402)
s1.show_info()
# public
print(s1.age)
# protected
class Info(Student):
    def method(self):
        print(self.houseno)
I1=Info("Hassan",16,402)
I1.method()
# oop assignment
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display_info(self):
        print(self.name,self.age,self.marks)
        if self.marks>=50:
            print("pass",self.marks)
s1=Student("hassan",16,400)
s1.display_info()
class Hassan(Student):
    def method():
        print("i love python") 
h1=Hassan
h1.method()




        

    

        
    

    


        
        




        
          
        

    
        

        
         
        
