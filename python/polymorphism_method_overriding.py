class parent:
    def shiv(self):
        print("shivshankar ghantewar")
    def marry(self):
        print("gajanan kasewar") 

class child(parent):
    def marry(self):
        super().marry()    # super() is used to call methods from the parent class inside a child class.
        print("gaurav patil")  

c=child()
c.shiv()
c.marry() # it override the parent method






class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


class employee(person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)  # super() is used to call methods from the parent class inside a child class.
        self.eno=eno
        self.esal=esal

    def display(self):
        print("\nname: ",self.name)
        print("age: ",self.age)
        print("employee number ",self.eno)
        print("employee salary",self.esal)

e1=employee("shiv",23,1,50000)
e1.display()        
e2=employee("shivshankar",23,2,60000)
e2.display()        