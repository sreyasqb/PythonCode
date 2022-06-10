import sqlite3
class Employee:
    def __init__(self,id,name,pay,age):
        self.name=name
        self.pay=pay
        self.age=age
        self.id=id
    @staticmethod
    def adapt(E):
        return "%d-%s-%d-%d"%(E.id,E.name,E.pay,E.age)
    def __repr__(self):
        return f"({self.id},{self.name}, {self.pay}, {self.age})"
    @classmethod
    def conv(cls,string):
        id,name,pay,age=map(float,string.split('-'))
        cls(id,name,pay,age)

sqlite3.register_adapter(Employee, Employee.adapt)
sqlite3.register_converter("emp", Employee.conv)

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()
cur.execute("""CREATE TABLE emps (
                id INTEGER PRIMARY KEY NOT NULL,
                employee emp NOT NULL
                );""")

emp1=