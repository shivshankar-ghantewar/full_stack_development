#oops why=> define in organize way.
# class=> bluepint,template,plan
#object=> 
#user-defined => defined by user
# self =instance variable

# class and objects
class student :
    def __init__(self,name,rollno,marks):
        self.name=name  # instance variable
        self.rollno=rollno   # instance variable
        self.marks=marks # instance variable

    def talk(self):
        print(self.name)
        print(self.rollno)
        print(self.marks)

s1=student("Durga",101,89)
s1.talk()        

        
# constructor with no-parameter

class student: 
    def __init__(self):
        self.name="shivshankar ghantewar"
        self.profession="full stack python developer with gen ai"
        print("my name is: ",self.name)
        print("my profession is: ",self.profession)

s1=student() 


# constructor with parameter

class student: 
    def __init__(self,name,job):
        self.name=name
        self.profession=job
        print("my name is: ",self.name)
        print("my profession is: ",self.profession)

s1=student("gaurav","python developer")    


