class Employee:
    email=""
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __repr__(self):
        return self.name+' '+str(self.age)+' '+self.email
    def __str__(self):
        return self.name+' '+str(self.age)+' '+self.email

e=Employee("rohan",12)
e.email="bye"
print(e.email)
print(e)