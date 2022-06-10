import re
s='''
82%
95%
7.9 CGPA a
8 CGPA
'''
#print(help(re))

pattern1=re.compile(r"\d\d%")

p2=re.compile('\d.\d CGPA|\d CGPA')
matches=pattern1.finditer(s)
m2=p2.finditer(s)


for i in matches:
    print(s[i.span()[0]:i.span()[1]])
for i in m2:
    print(float(s[i.span()[0]:i.span()[1]].rstrip(" CGPA")))