import sqlite3
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @staticmethod
    def adapt(p):
        return "%f;%f" % (p.x, p.y)
    def __repr__(self):
        return f"({self.x}, {self.y})"
    @classmethod
    def conv(cls,string):
        x, y = map(float, string.split(b';'))
        return cls(x, y)

sqlite3.register_adapter(Point, Point.adapt)
sqlite3.register_converter("point", Point.conv)

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()

cur.execute("""CREATE TABLE Points (
                id INTEGER PRIMARY KEY NOT NULL,
                p point NOT NULL
                );""")

p1 = Point(4.0, 5.0)
p2 = Point(5.0, 4.0)
cur.execute("INSERT INTO points (p) VALUES (?)", (p1,))
cur.execute("INSERT INTO points (p) VALUES (?)", (p2,))

# cur.execute("SELECT ")

cur.execute("SELECT * FROM Points")
l=cur.fetchall()
print(l)
print(l[0][1].x)
con.commit()
con.close()
