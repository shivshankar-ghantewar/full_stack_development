#  allows a new class (child/derived class) to inherit attributes and methods from an existing class (parent/base class). 


# single inheriance
class parent:
    def show(self):
        print("hi parent class")

class child(parent):
    def display(self):
        print("hi child class")

c1=child()
c1.show()
c1.display()



# multilevel inheriance
class grandparent:
    def run(self):
        print("hi grandparent class")

class parent(grandparent):
    def show(self):
        print("hi parent class")

class child(parent):
    def display(self):
        print("hi child class")

c1=child()
c1.run()     
c1.show()
c1.display()  


# multiple inheritance
class grandparent:
    def run(self):
        print("hi grandparent class")

class parent:
    def show(self):
        print("hi parent class")

class child(parent,grandparent):
    def display(self):
        print("hi child class")

c1=child()
c1.run()     
c1.show()
c1.display()  


# hirarchical inheritance
class grandparent:
    def run(self):
        print("hi grandparent class")

class parent(grandparent):
    def show(self):
        print("hi parent class")

class child(grandparent):
    def display(self):
        print("hi child class")

c1=child()
c1.run()     
c1.display()  

p1=parent()
p1.show()
p1.run()


# hybrid inheritance
class grandparent:
    def run(self):
        print("hi grandparent class")

class parent(grandparent):
    def show(self):
        print("hi parent class")

class child(parent,grandparent):
    def display(self):
        print("hi child class")

c1=child()
c1.run()     
c1.show()
c1.display() 

p1=parent()
p1.show()
p1.run()






