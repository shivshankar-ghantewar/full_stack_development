# method overloading
class new_class:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print("total sum=",total)


n=new_class()
n.sum(10,20)        
n.sum(10,20,30)        
n.sum(10,20,40)        