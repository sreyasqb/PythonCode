import sqlite3
class employee:
    count=0
    def __init__(self,name,number,pay):
        self.name=name
        self.number=number
        self.pay=pay
    @classmethod
    def from_string(cls,emp_string):
        name,number,pay=emp_string.split('-')
        return cls(name,number,pay)
    @staticmethod
    def validate(temp):
        if len(temp.number)== 10:return "valid"
        else: return "invalid"
    def raise_pay(self):
        self.pay=int(self.pay)+5

class developer(employee):
    def __init__(self,name,number,pay,lang):
        super().__init__(name,number,pay)
        self.lang=lang

s="Joe-9190231010-90"
s2="Kams-9886444150-100"
emp1=employee.from_string(s)
dev1=developer('acd',"12","567","python")
print(dev1.lang)
#emp2=employee.from_string(s2)

# print(emp1.name,emp1.number,emp2.name,emp2.number)
# print(employee.validate(emp1),employee.validate(emp2))
# emp1.raise_pay()
# employee.count=2
# print(emp1.count)
# print(emp1.pay)

